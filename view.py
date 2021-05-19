import sqlite3
from flask import Flask, render_template, url_for
import os
app = Flask(__name__)
#try:
  #conn = sqlite3.connect('new')
  #print ("Opened SQL DB")
#except Exception as e:
  #print("Error during connection :",str(e))
#results = conn.execute("SELECT * FROM Device")
#for row in results:
  #print (row)
  


@app.route('/employ')
def employ():

    conn = sqlite3.connect('new')
    #mycursor = conn.cursor(dictionary=True)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    results = conn.execute("SELECT * FROM Device")
    employees = results.fetchall()
    #print(employees)
    return render_template('home.html', employees=employees)

    conn.close()
    
