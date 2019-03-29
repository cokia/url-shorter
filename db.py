from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class li(db.Model):
    __table_name__ = 'table'
    db_id = db.Column(db.Integer, primary_key=True)
    db_input = db.Column(db.String(80), unique=True, nullable=False)
    db_output = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<li('{self.db_id}', '{self.db_input}', '{self.db_output}')>"

db.create_all()
