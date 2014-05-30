from flask.ext.wtf import Form
from wtforms import BooleanField, PasswordField, DateTimeField, validators
from wtforms import DecimalField, TextField, IntegerField, DateField, SelectField
from wtforms.validators import Required, Length, NumberRange


class LoginForm(Form):
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    

class ProfileForm(Form):
    calorie_goal = DecimalField(
        'Calorie Goal', 
        [validators.NumberRange(
            min=500, 
            max=5000,
            errorMessage: "Enter an integer between 500 and 5000")]
        )
    protein_goal = DecimalField(
        'Protein Goal', 
        [validators.NumberRange(
            min=10, 
            max=200,
            errorMessage: "Enter an integer between 10 and 200")]
        )
    carbohydrate_goal = DecimalField(
        'Carbohydrate Goal',
        [validators.NumberRange(
            min=95, 
            max=1000,
            errorMessage: "Enter an integer between 95 and 1000")]
        )
    fat_goal = DecimalField(
        'Fat Goal',
        [validators.NumberRange(
            min=7, 
            max=167,
            errorMessage: "Enter an integer between 7 and 167")]
        )
    birthdate = DateField(
        'Your Birthday Year, Month and Day', 
        format='%Y/%m/%d', 
        [validators.NumberRange(
        min=DateTime.Today.AddYears(-120), 
        max=DateTime.Today,
        errorMessage: "Invalid Birthdate")]
        )
    weight = SelectField('Weight', choices=[
        (('weight_in_pounds', 'Weight in Pounds'),
            [validators.NumberRange(
            min=2, 
            max=1000,
            errorMessage: "Enter an integer between 2 and 200")]),
        (('weight_in_kilograms', 'Weight in Kilograms'),
            [validators.NumberRange(
                min=1, 
                max=454,
                errorMessage: "Enter a number between 1 and 454")])
        (('weight_in_stones', 'Weight in Stones'), 
            [validators.NumberRange(
                min=2, 
                max=71)]),       
        )
    height = SelectField('Height', choices=[
        ((('height_in_feet'),('height_in_inches')), 
        (('Height in Feet'),('Height in Inches')), 
            [validators.NumberRange(
                min=1, 
                max=12)])
        (('height_in_centimeters', 'Height in Centimeters'),
            [validators.NumberRange(
                min=1, 
                max=8)])
        )
    
    gender = SelectField('Gender', choices=[
        ('male','Male'), 
        ('female', 'Female'), 
        ('female pregnant', 'Female Pregnant'), 
        ('female lactating', 'Female Lactating')], 
        [validators.Required()]
        )


    activity_level = SelectField('Activity Level', choices=[
        (('inactive', 'Inactive: Less than 2 hours of moving')), (.30),
        (('average', 'Average: Walking or Standing 2-4 or more hours per day')), (.50),
        (('active', 'Active: Physically Active 4 or more hours per day')), (.75)],
        [validators.Required()]
        )
    weight_change_weekly = SelectField('Weight Change Weekly', choices=[
        (('lose -2.0 lbs or -.91 kg or -.14 stones per week', 'Lose -2.0lbs/-.91kg/-.14 Stones per Week')),(-7000),
        (('lose -1.5 lbs or -.68 kg or -.11 stones per week', 'Lose -1.5lbs/-.68kg/-.11 Stones per Week')), (-5250),
        (('lose -1.0 lbs or -.45 kg or -.07 stones per week', 'Lose -1.0lbs/-.45kg/-.07 Stones per Week')), (-3500),
        (('lose -.5 lbs or -.23 kg or -.03 stones per week', 'Lose -.5 lbs/-.23kg/-.03 Stones per Week')), (-1750),
        (('maintain', 'Maintain')), (1)
        (('gain .5 lbs or .23 kg or .03 stones per week', 'Gain .5 lbs/.23kg/.03 Stones per Week')), (1750),
        (('gain 1.0 lbs or .45 kg or .07 stones per week', 'Gain 1.0lbs/.45kg/.07 Stones per Week'), (3500),
        (('gain 1.5 lbs or .68 kg or .11 stones per week', 'Gain 1.5lbs/.68kg/.11 Stones per Week'), (5250),
        (('gain 2.0 lbs or .91 kg or .14 stones per week', 'Gain 2.0lbs/.91kg/.14 Stones per Week')], (7000),
        [validators.Required()]
        )

    
    







    




