"""
Created on Wed Dec 16 16:51:59 2020

@author: hrishikesh mohan
"""

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/custom')
def custom():
    return render_template('custom.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/paris')
def paris():
    return render_template('paris.html') 

@app.route('/agra')
def agra():
    return render_template('agra.html')       

@app.route('/sydney')
def sydney():
    return render_template('sydney.html')

if __name__=="__main__":
    app.run()