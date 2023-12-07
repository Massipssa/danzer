from flask_sqlalchemy import SQLAlchemy

from danzer_anonymizer.danzer_anonymizer.models.base import Base

db = SQLAlchemy()


class Expectation(Base):
    __tablename__ = 'expectations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, name: str, id: str):
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name
