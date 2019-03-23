from flask import Flask, jsonify, request, abort
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"
redis_store = FlaskRedis(app)

def add_to_cart(session, item, quantity=1):
    return redis_store.hset('cart:' + session, item, quantity)

def get_cart(session):
    cart_items = []
    b_cart = redis_store.hgetall('cart:' + session)
    for item in b_cart.keys():
        cart_items.append({"item": item.decode("utf-8"), "quantity": b_cart[item].decode("utf-8")})
    return cart_items

@app.route('/', methods=['POST', 'GET'])
def items():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        add_to_cart(request.json['session'], request.json['item'], request.json['quantity'])
        return jsonify({'success':True}), 201

    elif request.method == 'GET':
        if request.args.get('id') is not None:
            return jsonify(get_cart(request.args.get('id'))), 200

        return abort(400)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
