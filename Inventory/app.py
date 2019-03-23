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

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    price = db.Column(db.String, unique=False)
    amount = db.Column(db.String, unique=False)

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    @property
    def serialize(self):
        """Return object data in easily serialized format"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'amount': self.amount,
        }

@app.route('/', methods=['POST', 'PUT', 'GET'])
def items():
    if request.method == 'POST':
        if not request.json:
            abort(400)

        item = Item(request.json['name'], request.json['price'], request.json['amount'])
        db.session.add(item)
        db.session.commit()
        return jsonify(item.serialize), 201

    elif request.method == 'GET':
        if request.args.get('id') is not None:
            query = Item.query.get(request.args.get('id'))
            return jsonify(query.serialize), 200

        query = Item.query.all()
        return jsonify([item.serialize for item in query]), 200

    elif request.method == 'PUT':
        print(request.json.get('id'))
        if not request.json or request.json.get('id') is None:
            abort(400)
        query = Item.query.get(request.json['id'])
        print(query)
        query.name = request.json['name']
        query.price = request.json['price']
        query.amount = request.json['amount']
        db.session.commit()
        return jsonify(query.serialize), 200


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
