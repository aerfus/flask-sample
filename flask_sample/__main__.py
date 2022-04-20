#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path

from flask import Flask, render_template

DEVELOPMENT_ENV  = True

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('index.html')

def main():
    app.run(debug=DEVELOPMENT_ENV)

if __name__ == '__main__':
    main()
