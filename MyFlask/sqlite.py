from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['address']
            city = request.form['city']
            pincode = request.form['pin']
            with sql.connect("database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students(name,addr,City,Pincode) VALUES (?,?,?,?)",
                               (nm, addr, city, pincode))
                conn.commit();
                msg = "Records successfully Added"
        except:
            conn.rollback()
            msg = "Problem in adding Records"
        finally:
            return render_template("result.html", msg=msg)
            conn.close()


@app.route('/list')
def list():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    cursor.execute('select * from students')
    rows = cursor.fetchall();
    return render_template("listForStudentRecordSql.html", rows= rows)


if __name__ == '__main__':
    app.run(debug=True)
