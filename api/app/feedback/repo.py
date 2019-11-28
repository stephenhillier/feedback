""" ratings repo: database tables and operations for ratings """
import datetime
import logging
from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey, MetaData, Integer, desc, text
from sqlalchemy.sql import select
from sqlalchemy.orm import relationship
from databases import Database
from app.db.base_class import BaseTable

from app.feedback.models import RatingRequest, RatingSummary

logger = logging.getLogger("api")

metadata = MetaData()


class RatingCode(BaseTable):
    """ codes for valid ratings """
    __tablename__ = "rating_code"

    rating_code = Column(String, primary_key=True)
    description = Column(String, nullable=False)
    ratings = relationship("Rating", back_populates="rating")

class Feature(BaseTable):
    """ a feature for which feedback is being gathered """

    __tablename__ = "feature"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False, index=True, unique=True)
    ratings = relationship("Rating", back_populates="feature")
    feedback = relationship("Feedback", back_populates="feature")
    create_time = Column(DateTime, nullable=False,
                         server_default=text('now()'))

class Rating(BaseTable):
    """ a rating represents basic feedback given by a user (postive / neutral / negative) """
    __tablename__ = "rating"

    id = Column(BigInteger, primary_key=True)
    rating_code = Column(String, ForeignKey('rating_code.rating_code'), nullable=False)
    feature_id = Column(String, ForeignKey('feature.id'), nullable=False)
    feature = relationship("Feature", back_populates="ratings")
    rating = relationship("RatingCode", back_populates="ratings")
    feedback = relationship("Feedback", back_populates="rating")
    create_time = Column(DateTime, nullable=False,
                         server_default=text('now()'))
    url = Column(String, nullable=False)

class Feedback(BaseTable):
    """ feedback is a comment provided by a user """
    __tablename__ = "feedback"

    id = Column(BigInteger, primary_key=True)
    comment = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False,
                         server_default=text('now()'))
    rating_id = Column(BigInteger, ForeignKey(
        'rating.id'), nullable=True)
    rating = relationship("Rating", back_populates="feedback")
    feature_id = Column(String, ForeignKey('feature.id'), nullable=False)
    feature = relationship("Feature", back_populates="feedback")
    url = Column(String, nullable=False)

rating = Rating.__table__
feedback = Feedback.__table__
feature = Feature.__table__

async def get_ratings(db: Database):
    """ get ratings summary """


    q = """
    
    WITH rated_features AS (
        SELECT
            f.name as feature_name,
            SUM(
                CASE
                    WHEN r.rating_code = 'positive' then 1
                    WHEN r.rating_code = 'negative' then -1
                    ELSE 0 END
            ) as ratings_sum
        FROM
            feature as f
        INNER JOIN
            rating as r ON r.feature_id = f.id
        GROUP BY
            feature_name
        ORDER BY ratings_sum desc
    ) SELECT DISTINCT
        FIRST_VALUE(feature_name) OVER w AS most_positive,
        FIRST_VALUE(ratings_sum) OVER w AS most_positive_rating,
        LAST_VALUE(feature_name) OVER w AS most_negative,
        LAST_VALUE(ratings_sum) OVER w AS most_negative_rating,
        (
            SELECT count(*) FROM rating WHERE rating_code = 'positive'
        ) AS overall_positive,
        (
            SELECT count(*) FROM rating WHERE rating_code = 'negative'
        ) AS overall_negative,
        (
            SELECT count(*) FROM rating WHERE rating_code = 'neutral'
        ) AS overall_neutral,
        (
            SELECT count(*) FROM rating
        ) AS overall_ratings
    FROM rated_features
    WINDOW w AS ();
    """

    summary = await db.fetch_one(query=q)
    return RatingSummary(**summary)

async def add_feature(db: Database, feature_name: str):
    """ adds a new feature with a given name """
    feat_q = feature.insert()
    values = { "name": feature_name}
    new_feature = await db.execute(query=feat_q, values=values)
    return new_feature

async def add_rating(db: Database, rating_req: RatingRequest):
    """ add a rating """

    # look up the feature for this rating (if it exists)
    feature_q = select([feature.c.id]).where(feature.c.name == rating_req.feature)
    feat = await db.execute(query=feature_q)

    # if the feature doesn't exist yet, create it now.
    if feat is None:
        feat = await add_feature(db, rating_req.feature)

    query = rating.insert()
    values = {"rating_code": rating_req.rating_code, "feature_id": feat, "url": rating_req.url}
    new_rating = await db.execute(query=query, values=values)
    return new_rating
