from flask import *
from sqlalchemy import *
from sqlalchemy.orm import *
from flask_sqlalchemy import *
import os
from db import li 
from db import app
#===========================================================================

@app.route('/<value>', methods=['GET'])
def find(value):
    quea = li.query.filter_by(db_output=value).first()
    if quea is None:
        print("NONE")
        return render_template('index.html')

    else:
        print("YES")
        return redirect(quea.input, code=302)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

#===============================================================================================
@app.route('/admin', methods=['GET', 'POST'])
def admin():
	return "admin page"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
