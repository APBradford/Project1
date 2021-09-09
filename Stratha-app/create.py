from application import db
from application.models import Cycling, Training_week

db.drop_all()

db.create_all()

#Create blank entries for the 12 training weeks
tw1 = Training_week(cycle_distance=0)
tw2 = Training_week(cycle_distance=0)
tw3 = Training_week(cycle_distance=0)
tw4 = Training_week(cycle_distance=0)
tw5 = Training_week(cycle_distance=0)
tw6 = Training_week(cycle_distance=0)
tw7 = Training_week(cycle_distance=0)
tw8 = Training_week(cycle_distance=0)
tw9 = Training_week(cycle_distance=0)
tw10 = Training_week(cycle_distance=0)
tw11 = Training_week(cycle_distance=0)
tw12 = Training_week(cycle_distance=0)
db.session.add(tw1)
db.session.add(tw2)
db.session.add(tw3)
db.session.add(tw4)
db.session.add(tw5)
db.session.add(tw6)
db.session.add(tw7)
db.session.add(tw8)
db.session.add(tw9)
db.session.add(tw10)
db.session.add(tw11)
db.session.add(tw12)
db.session.commit()