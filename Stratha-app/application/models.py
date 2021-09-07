from application import db

class Training_week(db.Model):
    __tablename__ = "training"
    training_week_id = db.Column(db.Integer, primary_key = True)
    cycles = db.relationship('Cycling', backref='training-week', lazy=True)
    cycle_distance = db.Column(db.Float, nullable = False)

class Cycling(db.Model):
    __tablename__ = "cycling"
    cycle_id = db.Column(db.Integer,  primary_key = True)
    training_week = db.Column(db.Integer, db.ForeignKey('training.training_week_id'), nullable = False)
    date = db.Column(db.String(10), nullable = False)
    distance = db.Column(db.Float, nullable = False)
    trSession = db.Column(db.String(25), nullable = False)
    comment = db.Column(db.String(250), nullable = False)