from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/searchstate')
def searchstate():
   return render_template('searchstate.html')
@app.route('/update')
def updatemain():
   return render_template('update.html')


@app.route('/range')
def range():
   return render_template('range.html')


@app.route('/searchkey')
def searchkey():
   return render_template('searchkey.html')


@app.route('/searchroom')
def searchroom():
   return render_template('searchroom.html')

@app.route('/statesearch', methods=['POST','GET'])
def statesearch():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    field=request.form['state']
    print(field)
    querry="Select * from names WHERE field3 =  '"+field+"' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/keysearch', methods=['POST','GET'])
def keysearch():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    field=request.form['key']
    print(field)
    querry="Select * from names WHERE field5 like '%"+field+"%' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/roomsearch', methods=['POST','GET'])
def roomsearch():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    field=request.form['room']
    print(field)
    querry="Select * from names WHERE field1 ='"+field+"' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list2.html",rows = rows)

@app.route('/namesearch', methods=['POST','GET'])
def list():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    field=request.form['name']
    print(field)
    querry="Select * from names WHERE field2 =  '"+field+"' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/all', methods=['POST','GET'])
def fulllist():
    conn = sqlite3.connect('names.db')
    cur = conn.cursor()
    querry="Select * from names where field2 !='Name'   "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/keyupdate',methods=['POST','GET'])
def update():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['no'])
        querry="UPDATE names SET field1 = '"+keyword+"'   WHERE field2 ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from names WHERE field2 =  '"+name+"' "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)


@app.route('/roomnumber', methods=['GET', 'POST'])
def roomnumber():
    if (request.method=='POST'):
        conn = sqlite3.connect('names.db')
        cur = conn.cursor()
        start= str(request.form['start'])
        end= str(request.form['end'])
        querry="select * from names WHERE  room  BETWEEN '"+start+"' AND '"+end+"' "
        cur.execute(querry)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.debug=True
    app.run()
    