from apiflask import APIFlask
from utils import BaseResponse
from product.api import bp as product_bp

app = APIFlask(__name__, docs_ui='elements')
app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse
app.config['BASE_RESPONSE_DATA_KEY'] = 'data'

# register
app.register_blueprint(product_bp)


@app.route('/')
def health():

    return f'Hello world!', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
