""" ratings repo: database tables and operations for ratings """
import datetime
import logging
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, MetaData, Integer, desc
from sqlalchemy.orm import relationship
from databases import Database
from app.db.base_class import BaseTable

logger = logging.getLogger("api")

metadata = MetaData()


class RatingCode(BaseTable):
    """ codes for valid ratings """
    __tablename__ = "rating_code"

    rating_code = Column(String, primary_key=True)
    description = Column(String, nullable=False)
    ratings = relationship("Rating", back_populates="rating")

class Rating(BaseTable):
    """ a rating represents basic feedback given by a user (postive / neutral / negative) """
    __tablename__ = "rating"

    id = Column(BigInteger, primary_key=True)
    rating_code = Column(String, ForeignKey('rating_code.rating_code'), nullable=False)
    rating = relationship("RatingCode", back_populates="ratings")
    feedback = relationship("Feedback", back_populates="rating")
    create_time = Column(DateTime, nullable=False,
                         default=datetime.datetime.utcnow)

class Feedback(BaseTable):
    """ feedback is a comment provided by a user """
    __tablename__ = "feedback"

    id = Column(BigInteger, primary_key=True)
    comment = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    rating_id = Column(BigInteger, ForeignKey(
        'rating.id'), nullable=True)
    rating = relationship("Rating", back_populates="feedback")


rating = Rating.__table__
feedback = Feedback.__table__

async def get_ratings(db: Database):
    """ get ratings summary """
    return []
