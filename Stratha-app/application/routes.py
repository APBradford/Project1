from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import Training_week, Cycling
from application.forms import addCycleForm

@app.route('/')
def homepage():
    allTraining = Training_week.query.all()
    return render_template('home.html', title="Stratha Home", training=allTraining)

@app.route('/Cycling', methods=['POST', 'GET'])
def cyclepage():
    form = addCycleForm()
    allCycles = Cycling.query.order_by(Cycling.training_week).all()
    if form.validate_on_submit():
        cycle = Cycling(
            training_week = form.trWeek.data,
            date = form.date.data,
            distance = form.distance.data,
            trSession = form.trSession.data,
            comment = form.comment.data,
        )
        db.session.add(cycle)
        db.session.commit()
        return redirect(url_for('cyclepage'))
    else:
        print(form.errors)
    return render_template('cycling.html', form=form, title="Cycling Training", cycling=allCycles)
