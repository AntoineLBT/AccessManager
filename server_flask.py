#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    return "Hello !"

if __name__ == '__main__':
    app.run(debug=True)
