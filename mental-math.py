#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:13:23 2020

@author: fraifeld-mba
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import random
import operator
import time
app = Flask(__name__)

class challenge():
    def __init__(self):
        self.a = random.randint(0,10)
        self.b = random.randint(1,10)
        self.sign = ['+','-','*','/'][random.randint(0,3)]
        ops = { "+": operator.add, 
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv}
        self.answer = ops[self.sign](self.a,self.b)
    
@app.route('/')
def index():
    return redirect(url_for('show_challenge'))


    
@app.route('/challenge',methods = ['POST', 'GET'])
def show_challenge():
    if request.method == 'GET':
        return render_template('challenge.html',challenge=challenge())
    if request.method == 'POST':
          result = request.form
          return render_template("check.html",result = result)


  
    
if __name__ == "__main__":
    app.run()


    