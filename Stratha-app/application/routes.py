from flask import Flask, render_template
from application import app
from application.models import Training_week

@app.route('/')
def homepage():
    trainingData = Training_week.query.all()
    return render_template('home.html', title="Stratha Home", training=trainingData)