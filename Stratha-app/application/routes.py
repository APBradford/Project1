from flask import Flask
from application import app

@app.route('/')
def homepage():
    return "Welcome to Stratha!"