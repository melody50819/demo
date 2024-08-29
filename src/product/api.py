from apiflask import APIBlueprint, Schema
from .schema import ProductPost
from .query import _create_product, _get_all_products, _update_product, _delete_product

bp = APIBlueprint('product', __name__, url_prefix='/product')


@bp.get('')
@bp.output(ProductPost, status_code=200)
def get_all_product():

    try:
        data = _get_all_products()
        return {'data': data, 'message': 'Succesfully list'}
    except Exception as e:
        print(e)


@bp.post('')
@bp.input(ProductPost, location='json')
@bp.output(Schema, status_code=201)
def create_product(json_data: dict):
    try:
        _create_product(data=json_data)
        return {'data': {}, 'message': 'Succesfully created'}
    except Exception as e:
        print(e)


@bp.put('/<int:id>')
@bp.output(Schema, status_code=204)
def update_product(id: str, json_data: dict):
    try:
        _update_product(id, data=json_data)
        return {'data': {}, 'message': 'Succesfully updated'}
    except Exception as e:
        print(e)


@bp.delete('/<int:id>')
@bp.output(Schema, status_code=204)
def delete_product(id: str):
    try:
        _delete_product(id)
        return {'data': {}, 'message': 'Succesfully deleted'}
    except Exception as e:
        print(e)
