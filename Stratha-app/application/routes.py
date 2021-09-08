from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import Training_week, Cycling
from application.forms import addCycleForm, editCycleForm

@app.route('/')
def homepage():
    allTraining = Training_week.query.all()
    return render_template('home.html', title="Stratha Home", training=allTraining)

@app.route('/Cycling', methods=['POST', 'GET'])
def cyclepage():
    form = addCycleForm()
    allCycles = Cycling.query.order_by(Cycling.training_week).all()
    
    #Adding up total cycling miles
    totalDistance = 0
    for cycle in allCycles:
        totalDistance += cycle.distance
    formatDistance = "{:.4f}".format(totalDistance)
    #Validating form and entering into database    
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
    return render_template('cycling.html', form=form, title="Cycling Training", cycling=allCycles, formatDistance=formatDistance)

@app.route('/EditCycle/<int:id>', methods=['POST', 'GET'])
def editCycle(id):
    allCycles = Cycling.query.order_by(Cycling.training_week).all()
    editing = Cycling.query.get(id)
    form = editCycleForm()
    
    #Updating database with edit
    if form.validate_on_submit():
        editing.training_week = form.trWeek.data
        editing.date = form.date.data
        editing.distance = form.distance.data
        editing.trSession = form.trSession.data
        editing.comment = form.comment.data
        db.session.commit()
        return redirect(url_for('cyclepage'))

    #Prepopulating form with editing data    
    elif request.method == 'GET':
        form.trWeek.data = editing.training_week
        form.date.data = editing.date
        form.distance.data = editing.distance
        form.trSession.data = editing.trSession
        form.comment.data = editing.comment
    return render_template('editCycling.html', form=form, title="Cycling Training", cycling=allCycles, cycleId=id)

@app.route('/DeleteCycle/<int:id>', methods=['POST', 'GET'])
def deleteCycle(id):
    
    #Delete entry from database
    editing = Cycling.query.get(id)
    db.session.delete(editing)
    db.session.commit()
    return redirect(url_for('cyclepage'))