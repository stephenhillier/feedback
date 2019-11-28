""" API models.  See repo.py for database models """

from datetime import datetime, date
from pydantic import BaseModel, UrlStr
from typing import Optional, List


class RatingRequest(BaseModel):
    """ a request for a new monitor, which must include a name and an endpoint """
    rating_code: str
    feature: str
    url: Optional[UrlStr]

class RatingSummary(BaseModel):
    """ a summary of all ratings, showing the most positive feature, most negative etc."""
    most_positive: str
    most_positive_rating: int
    overall_positive: int
    overall_negative: int
    overall_neutral: int
    overall_ratings: int
    most_negative: str
    most_negative_rating: int
    
    class Config:
        orm_mode = True