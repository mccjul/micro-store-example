from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'test',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String, unique=False)
    customer = db.Column(db.String)
    amount = db.Column(db.String, unique=False)

    def __init__(self, item_id, customer, amount):
        self.customer = customer
        self.item_id = item_id
        self.amount = amount

    @property
    def serialize(self):
        """Return object data in easily serialized format"""
        return {
            'id': self.id,
            'item_id': self.item_id,
            'customer': self.customer,
            'amount': self.amount,
        }

@app.route('/', methods=['POST', 'GET'])
def items():
    if request.method == 'POST':
        if not request.json:
            abort(400)

        order = Order(request.json['item_id'], request.json['customer'], request.json['amount'])
        db.session.add(order)
        db.session.commit()
        return jsonify(order.serialize), 201

    elif request.method == 'GET':
        query = Order.query.all()
        return jsonify([item.serialize for item in query]), 200


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5001)
