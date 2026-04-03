from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    # __table_args__ = {"schema": "sakila"}
    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rights = db.Column(db.String(10), default=UserRights(), nullable=False)

    full_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(45), nullable=False)

    last_update = db.Column(
        db.TIMESTAMP,
        nullable=False,
        server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
