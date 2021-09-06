from application import db

class Training_week(db.Model):
    __tablename__ = "training"
    training_week_id = db.Column(db.Integer, primary_key = True)
    cycles = db.relationship('cycling', backref = 'training-week')
    cycle_distance = db.Column(db.Float, nullable = False)

class Cycling(db.Model):
    __tablename__ = "cycling"
    cycle_id = db.Column(db.Integer, primary_key = True)
    training_week = db.Column(db.Integer, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    distance = db.Column(db.Float, db.ForeignKey('training.training_week_id'), nullable = False)
    comment = db.Column(db.String(250), nullable = False)