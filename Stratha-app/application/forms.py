from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, ValidationError, Length
from wtforms import StringField, IntegerField, DecimalField, DateField, SelectField, SubmitField

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
    date = StringField("Date (xx/xx/xxxx): ", validators=[DataRequired(), Length(min=10, max=10)])
    
    def validate_date(form, date):
        vDate = date.data
        if vDate[2] != "/":
            raise ValidationError("Invalid Date Format Entered, Please Use xx/xx/xxxx")
        elif vDate[5] != "/":
            raise ValidationError("Invalid Date Format Entered, Please Use xx/xx/xxxx")

    distance = DecimalField("Distance (Miles): ")
    trSession = SelectField("Training Session: ", choices=[
        ("easy", "Easy"),
        ("tempo", "Tempo"),
        ("sprints", "Sprints"),
        ("hills", "Hills"),
        ("endurance", "Endurance"),
    ])
    comment = StringField("Comment: ", validators=[Length(max=250)])

    def validate_comment(form, comment):
        specialchars = '$£!%^&*?=-\/'
        comment = comment.data
        for i in comment:
            for c in specialchars:
                if i == c:
                    raise ValidationError("Use of special characters is forbidden for comments")
    
    submit = SubmitField("Submit")