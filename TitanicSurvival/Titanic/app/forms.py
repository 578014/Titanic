from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    Pclass = IntegerField('Class. Enter a number between 1 and 3, 1 = First Class',validators=[NumberRange(min=1, max=3)])
    Sex = IntegerField('Gender. 0=Male, 1=Female', validators=[NumberRange(min=0, max=1)])

    Age = FloatField('Enter age 0-3: 0=0-16, 1=16-32, 2=32-64, 3=64+ ', validators=[NumberRange(min=0, max=3)])
    Fare = FloatField('Enter Fare 0-3: 0=0-7.91, 1=7.91-14.454, 2=14.454-31, 3=31+', validators=[NumberRange(min=0, max=3)])

    Embarked = IntegerField('Embark. 0 = Southampton, 1 = Cherbourg, 2 = Queenstown',validators=[NumberRange(min=0, max=3)])

    submit = SubmitField('Submit')

