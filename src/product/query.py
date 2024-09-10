from src.utils import shared_engine
from sqlalchemy import text


def _create_product(data: dict):

    stmt = '''INSERT INTO `product`.`product`
                (`code`, `name`, `category`, `size`, `unit_price`, `inventory`, `color`)
                VALUES (:code, :name, :category, :size, :unit_price, :inventory, :color);
            '''
    try:
        with shared_engine.connect() as conn:
            conn.execute(text(stmt), parameters=data)
            conn.commit()
    except:
        conn.rollback()
        raise


def _get_all_products():

    stmt = '''SELECT * FROM `product`.`product`;'''
    try:
        with shared_engine.connect() as conn:
            result = conn.execute(text(stmt))
            return [dict(row) for row in result.fetchall()]
    except:
        raise


def _update_product(product_id: int, data: dict):
    stmt = '''UPDATE `product`.`product`
                SET code = :code, name = :name, category = :category, 
                    size = :size, unit_price = :unit_price, 
                    inventory = :inventory, color = :color
                WHERE id = :id;
            '''
    try:
        with shared_engine.connect() as conn:
            with conn.begin():
                data['id'] = product_id
                conn.execute(text(stmt), data)
    except:
        raise


def _delete_product(product_id: int):
    stmt = '''DELETE FROM `product`.`product` WHERE id = :id;'''
    try:
        with shared_engine.connect() as conn:
            with conn.begin():
                result = conn.execute(text(stmt), {'id': product_id})
                return result.rowcount
    except:
        raise
