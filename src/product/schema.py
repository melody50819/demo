from apiflask import Schema
from apiflask.fields import String, Integer


class ProductPost(Schema):
    code = String(required=True)
    name = String(required=True)
    category = String(required=True)
    size = String()
    unit_price = Integer(required=True)
    inventory = Integer(required=True)
    color = String()


# class ProductIn(Schema):
#     id = String(required=True)
