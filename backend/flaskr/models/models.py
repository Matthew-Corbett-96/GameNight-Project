from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from sqlalchemy import select, case, func

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


# GameNightGame model
class GameNightGame(db.Model, MixinBase):
    __tablename__ = "game_night_games"

    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    game_id = db.Column(UUID, db.ForeignKey("games.id"))


# Attendance model
class Attendance(db.Model, MixinBase):
    __tablename__ = "attendance"

    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    status = db.Column(
        db.String(10)
    )  # Possible statuses: Attending, Not Attending, Maybe


# Announcement model
class Announcement(db.Model, MixinBase):
    __tablename__ = "announcements"

    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    content = db.Column(db.String(200))

    @hybrid_property
    def is_active(self) -> bool:
        return self.start_date <= datetime.now() <= self.end_date

    @is_active.expression
    def is_active(cls) -> bool:
        return select(
            case(
                [(func.now() >= cls.start_date & func.now() <= cls.end_date, True)],
                else_=False,
            )
        ).label("is_active")


def init_app(app: Flask):
    db.init_app(app)
