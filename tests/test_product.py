import pytest
from apiflask import APIFlask
from src.product.api import bp
from unittest.mock import patch


@pytest.fixture
def app():
    app = APIFlask(__name__)
    app.register_blueprint(bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_products(client, monkeypatch):

    def mock_get_all_products():
        return {
            'data': [{
                "id": 1,
                "code": "P001",
                "name": "Product 1",
                "category": "Category 1",
                "size": "M",
                "unit_price": 100,
                "inventory": 50,
                "color": "Red"
            }, {
                "id": 2,
                "code": "P002",
                "name": "Product 2",
                "category": "Category 2",
                "size": "L",
                "unit_price": 200,
                "inventory": 30,
                "color": "Blue"
            }],
            'message':
            'Succesfully list'
        }

    monkeypatch.setattr('src.product.query._get_all_products',
                        mock_get_all_products)

    response = client.get('/product')
    assert response.status_code == 200


def test_create_product(client):
    mock_data = {
        "code": "P003",
        "name": "New Product",
        "category": "New Category",
        "size": "S",
        "unit_price": 150,
        "inventory": 25,
        "color": "Green"
    }
    with patch('src.product.query._create_product') as mock_create:
        mock_create.return_value = None
        response = client.post('/product', json=mock_data)
        assert response.status_code == 201


def test_update_product(client):
    with patch('src.product.query._update_product') as mock_update:
        mock_update.return_value = None
        product_data = {
            "code": "P001",
            "name": "Updated Product",
            "category": "Updated Category",
            "size": "L",
            "unit_price": 180,
            "inventory": 40,
            "color": "Yellow"
        }
        response = client.put('/product/1', json=product_data)
        assert response.status_code == 204


def test_delete_product(client):
    with patch('src.product.query._delete_product') as mock_delete:
        mock_delete.return_value = 1
        response = client.delete('/product/1')
        assert response.status_code == 204
