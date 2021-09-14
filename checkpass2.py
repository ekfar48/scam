# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def index():
    return '''
    соси
    '''
#http://127.0.0.1:5000/
if __name__ == "__main__":
    app.run(debug=False)
