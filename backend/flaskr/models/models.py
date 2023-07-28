from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
import uuid

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
        return "<{} {}>".format(self.__class__.__name__, self.id)

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# User model
class User(db.Model, MixinBase):
    __tablename__ = "users"

    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128))
    announcements = db.relationship("Announcement")

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["announcements"] = [announcement.to_dict() for announcement in self.announcements]
        return base_dict


# Game model
class Game(db.Model, MixinBase):
    __tablename__ = "games"

    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    game_type = db.Column(db.String(64))
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)


# GameNight model
class GameNight(db.Model, MixinBase):
    __tablename__ = "game_nights"

    date = db.Column(db.DateTime, server_default=func.now())
    games = db.relationship("GameNightGame")
    attendance = db.relationship("Attendance")

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["games"] = [game_night_game.game.name for game_night_game in self.games]
        base_dict["attendance"] = [attendance.to_dict() for attendance in self.attendance]
        return base_dict


# GameNightGame model
class GameNightGame(db.Model, MixinBase):
    __tablename__ = "game_night_games"

    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    game_night = db.relationship("GameNight") # this is redundant, but it's here for the sake of clarity
    game_id = db.Column(UUID, db.ForeignKey("games.id"))
    game = db.relationship("Game") # this is redundant, but it's here for the sake of clarity

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["game_night_date"] = self.game_night.date
        base_dict["game_name"] = self.game.name
        return base_dict


# Attendance model
class Attendance(db.Model, MixinBase):
    __tablename__ = "attendance"

    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    user = db.relationship("User") # this is redundant, but it's here for the sake of clarity
    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    game_night = db.relationship("GameNight") # this is redundant, but it's here for the sake of clarity
    status = db.Column(db.String(10))  # statuses: Attending, Not Attending, Maybe

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["username"] = self.user.username
        base_dict["game_night_date"] = self.game_night.date
        return base_dict


# Announcement model
class Announcement(db.Model, MixinBase):
    __tablename__ = "announcements"

    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    user = db.relationship("User") # this is redundant, but it's here for the sake of clarity
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
        base_dict["user_name"] = self.user.username
        base_dict["is_active"] = self.is_active
        return base_dict
    


def init_app(app: Flask):
    db.init_app(app)
