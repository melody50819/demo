import os
from apiflask import Schema
from apiflask.fields import String, Integer, Field
from sqlalchemy import create_engine

MYSQL_DATABASE_URL = os.getenv('MYSQL_DATABASE_URL')

shared_engine = create_engine(MYSQL_DATABASE_URL)


class BaseResponse(Schema):
    message = String()
    status_code = Integer()
    data = Field()