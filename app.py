from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(80), unique=True, nullable=False)
  lname = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False)
  userpass = db.Column(db.String(20), unique=True, nullable=False)

  def __init__(self, fname, lname, email, userpass):
    self.fname = fname
    self.lname = lname
    self.email = email
    self.userpass = userpass

db.create_all()

# -- retrieve a single user
@app.route('/users/<id>', methods=['GET'])
def get_item(id):
  item = Item.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

# -- get all the users in the database
@app.route('/users', methods=['GET'])
def get_items():
  items = []
  for item in db.session.query(Item).all():
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

# -- create a new user
@app.route('/users', methods=['POST'])
def create_item():
  body = request.get_json()
  db.session.add(Item(body['fname'], body['lname'], body['email'], body['userpass']))
  db.session.commit()
  return "user created"

# -- update an existing user
@app.route('/users/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  db.session.query(Item).filter_by(id=id).update(
    dict(fname=body['fname'], lname=body['lname'], email=body['email'], userpass=body['userpass']))
  db.session.commit()
  return "user updated"

# -- delete an existing user
@app.route('/users/<id>', methods=['DELETE'])
def delete_item(id):
  db.session.query(Item).filter_by(id=id).delete()
  db.session.commit()
  return "user deleted"