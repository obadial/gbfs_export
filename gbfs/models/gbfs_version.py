from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import JSON

from gbfs.extensions import db
from gbfs.models.base import TimestampMixin


class GbfsVersion(TimestampMixin, db.Model):
    __tablename__ = "gbfs_version"

    id = Column(Integer, primary_key=True)
    last_updated = Column(String, nullable=False)
    data = Column(JSON, nullable=False)

    def __repr__(self):
        return f"""<gbfs_version(id={self.id},
        last_updated={self.last_updated},
        data={self.data})>"""
