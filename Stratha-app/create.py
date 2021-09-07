from application import db
from application.models import Cycling, Training_week

#REMOVE FOR FINAL PRODUCT
db.drop_all()
#REMOVE FOR FINAL PRODUCT
db.create_all()

testtrain = Training_week(cycle_distance="15.3")
testtrain2 = Training_week(cycle_distance="405.3")
testcycle = Cycling(training_week="1", date="06/09/2021", distance="25.3", comment="Went Well", trSession="Easy")
testcycle2 = Cycling(training_week="2", date="10/09/2050", distance="222.3", comment="Well", trSession="Easy")
db.session.add(testcycle)
db.session.add(testcycle2)
db.session.add(testtrain)
db.session.add(testtrain2)
db.session.commit()