from flask import *
from sqlalchemy import *
from sqlalchemy.orm import *
from flask_sqlalchemy import *
import os
import db
from db import User 
from db import app
#===========================================================================

@app.route('/<value>', methods=['GET'])
def find(value):
    que = User.query.filter_by(output=value).first()
    if que is None:
        return render_template('index.html')

    else:
        return redirect(que.input, code=302)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

#===============================================================================================
@app.route('/admin', methods=['GET', 'POST'])
def admin():
	return "admin page"

if __name__ == "__main__":
	app.run(host="0.0.0.0")