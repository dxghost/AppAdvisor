from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

'''
https://www.w3schools.com/css/tryit.asp?filename=trycss_forms
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form['firstname']
        print(name)
        cat = request.form["Categories"]

        with sql.connect('example.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Apps WHERE Appname LIKE ? AND Category Like ? ",('%'+name+'%','%'+cat+'%'))
            result = cur.fetchall()
            print(result)
            return render_template('result.html', result=result)


@app.route('/add')
def add():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
