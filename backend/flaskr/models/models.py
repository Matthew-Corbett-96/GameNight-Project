from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import uuid
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self) -> str:
        return "<User {}>".format(self.username)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "email": self.email,
            "phone_number": self.phone_number,
            "password": self.password
        }


# Game model
class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    game_type = db.Column(db.String(64))
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)

    def __repr__(self) -> str:
        return "<Game {}>".format(self.name)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "game_type": self.game_type,
            "min_players": self.min_players,
            "max_players": self.max_players
        }


# GameNight model
class GameNight(db.Model):
    __tablename__ = "game_nights"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "<GameNight {}>".format(self.id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date
        }


# GameNightGame model
class GameNightGame(db.Model):
    __tablename__ = "game_night_games"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    game_id = db.Column(UUID, db.ForeignKey("games.id"))

    def __repr__(self):
        return "<GameNightGame {}>".format(self.id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "game_night_id": self.game_night_id,
            "game_id": self.game_id
        }

# Attendance model
class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    game_night_id = db.Column(UUID, db.ForeignKey("game_nights.id"))
    status = db.Column(
        db.String(10)
    )  # Possible statuses could be: Attending, Not Attending, Maybe

    def __repr__(self):
        return "<Attendance {}>".format(self.id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "game_night_id": self.game_night_id,
            "status": self.status
        }

# Announcement model
class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID, db.ForeignKey("users.id"))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    content = db.Column(db.String(200))

    def __repr__(self):
        return "<Announcement {}>".format(self.id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "content": self.content
        }
    
def init_app(app: Flask):
    db.init_app(app)
