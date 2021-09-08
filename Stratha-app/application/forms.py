from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, Length
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField, DateTimeField
from datetime import datetime

class addCycleForm(FlaskForm):
    trWeek = SelectField("Training week: ", choices=[
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ])

    date = DateTimeField("Date: ", format='%Y-%m-%d %H:%M:%S', default=datetime.today, validators=[DataRequired()])

    #Custome validator to ensure date entered isnt in the future
    def validate_date(form, date):
        vDate = str(date.data)
        onlyDate = vDate[:10]
        year, month, day = onlyDate.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        currentYear = datetime.today().year
        currentMonth = datetime.today().month
        currentDay = datetime.today().day
        if year > currentYear:
            raise ValidationError("Liar! - You can't exercise in the future")
        elif month > currentMonth:
            raise ValidationError("Liar! - You can't exercise in the future")
        elif day > currentDay:
            raise ValidationError("Liar! - You can't exercise in the future")

    distance = DecimalField("Distance (Miles): ", places=2, validators=[DataRequired()])
    trSession = SelectField("Training Session: ", choices=[
        ("Easy", "Easy"),
        ("Tempo", "Tempo"),
        ("Sprints", "Sprints"),
        ("Hills", "Hills"),
        ("Endurance", "Endurance"),
    ])
    comment = StringField("Comment: ", validators=[Length(max=100)])

    #Preventing use of special characters to help protect against injection attacks
    def validate_comment(form, comment):
        specialchars = '$£!%^&*?=-\/'
        comment = comment.data
        for i in comment:
            for c in specialchars:
                if i == c:
                    raise ValidationError("Use of special characters is forbidden for comments")
    
    submit = SubmitField("Submit")

class editCycleForm(FlaskForm):
    trWeek = SelectField("Training week: ", choices=[
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ])
    date = DateTimeField("Date: ", format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])

    #Custome validator to ensure date entered isnt in the future
    def validate_date(form, date):
        vDate = str(date.data)
        onlyDate = vDate[:10]
        year, month, day = onlyDate.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        currentYear = datetime.today().year
        currentMonth = datetime.today().month
        currentDay = datetime.today().day
        if year > currentYear:
            raise ValidationError("Liar! - You can't exercise in the future")
        elif month > currentMonth:
            raise ValidationError("Liar! - You can't exercise in the future")
        elif day > currentDay:
            raise ValidationError("Liar! - You can't exercise in the future")

    distance = DecimalField("Distance (Miles): ", validators=[DataRequired()])
    trSession = SelectField("Training Session: ", choices=[
        ("Easy", "Easy"),
        ("Tempo", "Tempo"),
        ("Sprints", "Sprints"),
        ("Hills", "Hills"),
        ("Endurance", "Endurance"),
    ])
    comment = StringField("Comment: ", validators=[Length(max=100)])

    #Preventing use of special characters to help protect against injection attacks
    def validate_comment(form, comment):
        specialchars = '$£!%^&*?=-\/'
        comment = comment.data
        for i in comment:
            for c in specialchars:
                if i == c:
                    raise ValidationError("Use of special characters is forbidden for comments")
    
    submit = SubmitField("Submit")