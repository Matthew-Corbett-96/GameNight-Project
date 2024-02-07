from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
import uuid
from .tools import to_list, get_value_or_none

db = SQLAlchemy()

class MixinBase:
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __dict__(self) -> dict:
        return self.to_dict()

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# User model
class User(db.Model, MixinBase):
    __tablename__ = "users"

    auth0_id = db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user_roles.id"), nullable=True)
    role = db.relationship("UserRole", backref="users")
    is_active = db.Column(db.Boolean, default=True)
    # rsvp_logs

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["RSVPs"] = to_list(self.rsvp_logs)
        base_dict["role_name"] = get_value_or_none(self.role, "role_name")
        return base_dict


class UserRole(db.Model, MixinBase):
    __tablename__ = "user_roles"

    role_name = db.Column(db.String(50), unique=True, nullable=False)
    permissions = db.Column(db.String(200))  # This can be a comma-separated string of permissions or a JSON field
    # USERS

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["users"] = to_list(self.users, ["username", "id"])
        return base_dict

# Game model
class Game(db.Model, MixinBase):
    __tablename__ = "games"

    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    house_rules = db.Column(db.String(256), nullable=True)
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)


# GameNight model
class GameNight(db.Model, MixinBase):
    __tablename__ = "game_nights"

    date = db.Column(db.DateTime, server_default=func.now())
    rounds = db.relationship("Round", backref="game_night")
    # rsvp_logs 

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["Rounds"] = to_list([round.game for round in self.rounds], ["name"])
        base_dict["RSVPs"] = to_list(self.rsvp_logs)
        return base_dict


# Round model
class Round(db.Model, MixinBase):
    __tablename__ = "rounds"

    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    # game_night
    game_id = db.Column(UUID, db.ForeignKey("games.id"))
    game = db.relationship("Game")

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["game_night_date"] = get_value_or_none(self.game_night, "date")
        base_dict["game_name"] = get_value_or_none(self.game, "name")
        return base_dict


# Announcement model
class Announcement(db.Model, MixinBase):
    __tablename__ = "announcements"

    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    content = db.Column(db.String(200))

    @hybrid_property
    def is_active(self) -> bool:
        return self.end_date >= datetime.now() >= self.start_date 

    @is_active.expression
    def is_active(cls) -> bool:
        return func.now().between(cls.start_date, cls.end_date)
    
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["is_active"] = self.is_active
        return base_dict

# RSVPLog model
class RSVPLog(db.Model, MixinBase):
    __tablename__ = "rsvp_logs"
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    user_name = db.relationship("User", backref="rsvp_logs")
    game_night_id = db.Column(UUID(as_uuid=True), db.ForeignKey("game_nights.id"), nullable=False)
    game_night = db.relationship("GameNight", backref="rsvp_logs")
    response_date = db.Column(db.DateTime, server_default=func.now())
    response_status = db.Column(db.String(20)) # response_status can be YES, NO, or MAYBE

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["user_name"] = get_value_or_none(self.user_name, "username")
        base_dict["game_night_date"] = get_value_or_none(self.game_night, "date")
        return base_dict

# Notification model
class Notification(db.Model, MixinBase):
    __tablename__ = "notifications"
    message = db.Column(db.String(256))    
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    sent_date = db.Column(db.DateTime, server_default=func.now())
    channel = db.Column(db.String(20)) # channel can be sms, or website
    notification_type = db.Column(db.String(20)) # notification_type can be announcement, or reminder, or alert


def init_app(app: Flask):
    db.init_app(app)
