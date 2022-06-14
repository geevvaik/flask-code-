import os
from pdb import set_trace
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import pdb
from flask import Flask
from flask import render_template
app = Flask('server app')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2021.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/northwind"
db = SQLAlchemy(app)

class Shippers(db.Model):
  shipperid = db.Column(db.Integer(), primary_key=True)
  companyname = db.Column(db.String(40), nullable = False)
  phone = db.Column(db.String(24))

  def __repr__(self):
    return 'companyname: '+str(self.companyname)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shippers')
def films():
  shippers = Shippers.query.all()


  # print(films[0].description)

  return render_template('shippers.html', shippers = shippers)

if __name__ == "__main__":
   app.run()

