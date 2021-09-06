from application import db
from application.models import Cycling

#REMOVE FOR FINAL PRODUCT
db.drop_all()
#REMOVE FOR FINAL PRODUCT
db.create_all()

testcycle = Cycling(training_week="1", date="06/09/2021", distance="25.3", comment="Went Well")
db.session.add(testcycle)
db.session.commit()