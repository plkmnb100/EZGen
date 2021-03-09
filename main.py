from flask import Flask, render_template, request
from flask import session, redirect, url_for, abort
import sqlite3
import os
import random
import string

app = Flask(__name__)

cwdir =  f"{os.path.dirname(__file__)}/"

def is_expired(time):
    ServerTime = datetime.datetime.now()
    ExpireTime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
    if ((ExpireTime - ServerTime).total_seconds() > 0):
        return False
    else:
        return True

def get_expiretime(time):
    ServerTime = datetime.datetime.now()
    ExpireTime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
    if ((ExpireTime - ServerTime).total_seconds() > 0):
        Total = (ExpireTime - ServerTime)
        days = Total.days
        hours = Total.seconds // 3600
        minutes = Total.seconds // 60 - hours * 60
        return str(round(days)) + "일 " + str(round(hours)) + "시간"
    else:
        return False

def make_expiretime(days):
    ServerTime = datetime.datetime.now()
    ExpireTime_STR = (ServerTime + timedelta(days=days)).strftime('%Y-%m-%d %H:%M')
    return ExpireTime_STR

def add_time(now_days, add_days):
    ExpireTime = datetime.datetime.strptime(now_days, '%Y-%m-%d %H:%M')
    ExpireTime_STR = (ExpireTime + timedelta(days=add_days)).strftime('%Y-%m-%d %H:%M')
    return ExpireTime_STR

def RandomString(length):
    string_pool = string.ascii_letters + string.digits

    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)

    return result

@app.route("/", methods=["GET", "POST"])
def quick_signin():
    