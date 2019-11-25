""" API models.  See repo.py for database models """

from datetime import datetime, date
from pydantic import BaseModel, UrlStr
from typing import Optional, List


class RatingRequest(BaseModel):
    """ a request for a new monitor, which must include a name and an endpoint """
    rating_code: str
    feature: str
    url: Optional[UrlStr]
