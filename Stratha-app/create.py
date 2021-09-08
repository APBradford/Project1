from application import db
from application.models import Cycling, Training_week

#REMOVE FOR FINAL PRODUCT
db.drop_all()
#REMOVE FOR FINAL PRODUCT
db.create_all()

testtrain = Training_week(cycle_distance="15.3")
testtrain2 = Training_week(cycle_distance="405.3")
db.session.add(testtrain)
db.session.add(testtrain2)
db.session.commit()