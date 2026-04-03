from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

from src.schemas import UserRights


Base = declarative_base()


class User(Base):
    # __table_args__ = {"schema": "sakila"}
    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rights = db.Column(db.String(10), default=UserRights(), nullable=False)

    full_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    last_update = db.Column(db.DateTime, server_default=db.func.now())


def load_models(engine):
    Base.metadata.create_all(engine)
