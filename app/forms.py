from flask.ext.wtf import Form
from wtforms import BooleanField, PasswordField, DateTimeField, validators
from wtforms import DecimalField, TextField, IntegerField, DateField, SelectField, FloatField
from wtforms.validators import Required, Length, NumberRange
from wtforms.fields.html5 import DateField
import datetime
from datetime import date, timedelta


class LoginForm(Form):
    #add email field or username field
    password = PasswordField('Password', [
        validators.Required(),    
    ])
    username_or_email = TextField('Username or Email Address', [validators.Length(min=4, max=35)])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),    
    ])
    confirm = PasswordField('Repeat Password', [  
    validators.EqualTo('password', message='Passwords must match')
    ])

class ProfileForm(Form):

    calorie_goal = IntegerField(
        'Calories', 
        [validators.NumberRange(
            min=500, 
            max=10000,
            message="Enter the number of calories between 500 and 10,000.")]
        )
    protein_goal = IntegerField(
        'Protein', 
        [validators.NumberRange(
            min=1, 
            max=100,
            message="Enter the percentage of your calories to consume as protein.")]
        )
    carbohydrate_goal = IntegerField(
        'Carbohydrate',
        # [validators.NumberRange(
        #     min=1, 
        #     max=300,
        #     message="Enter the number of Carbohydrate grams between 1 and 300.")]
        )
    fat_goal = IntegerField(
        'Fat',
        [validators.NumberRange(
            min=1, 
            max=100,
            message="Enter an integer between 1 and 100 as a percentage of your Calorie Goal")]
        )
    

    #research how to validate a datefield
    birthday = DateField(
        # 'Enter your Birthday in this format: Year - Month - Day',
        # [validators.NumberRange(
        #     min=datetime.date.today() - datetime.timedelta(days=45657),
        #     max=datetime.date.today())]
        'Select your birthday.',
        validators=[]
        )

    
    weight_unit = SelectField('Weight Unit: ', choices=[
        ('weight_in_pounds', 'Pounds'),
            # [validators.NumberRange(
            # min=2, 
            # max=1000,
            # message="Enter an integer between 2 and 1000")]),
        ('weight_in_kilograms', 'Kilograms'),
            # [validators.NumberRange(
            #     min=1, 
            #     max=454,
            #     message="Enter a number between 1 and 454")])
        ('weight_in_stones', 'Stones')], 
            # [validators.NumberRange(
            #     min=2, 
            #     max=71)]), 
        validators=[validators.Required(
                message='Make a Selection')]     
        )

    weight = IntegerField(
        'Weight:', 
        [validators.NumberRange(
            min=1, 
            max=1000,
            message="Enter a number between and including 1 and 1000")]
        )

    # weight_goal = IntegerField(
    #     'Weight Goal',
    #     [validators.NumberRange(
    #         min=1,
    #         max=1000,
    #         message="Enter a number between and including 1 and 1000")]
    #     )
    
    height_in_feet = SelectField('Feet', choices=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9', '9'),
        ('10','10'),
        ('11', '11'),
        ('12', '12')],
        )
    height_in_inches = SelectField('Inches', choices=[
        ('1','1'),
        ('1.5','1.5'),
        ('2','2'),
        ('2.5','2.5'),
        ('3','3'),
        ('3.5','3.5'),
        ('4','4'),
        ('4.5','4.5'),
        ('5','5'),
        ('5.5','5.5'),
        ('6','6'),
        ('6.5','6.5'),
        ('7','7'),
        ('7.5','7.5'),
        ('8','8'),
        ('8.5','8.5'),
        ('9', '9'),
        ('9.5','9.5'),
        ('10','10'),
        ('10.5','10.5'),
        ('11', '11'),
        ('11.5','11.5'),
        ('12','12')],     
        )

        
    height_in_centimeters = FloatField(
        'Centimeters', 
        [validators.NumberRange(
            min=0, 
            max=300,
            message="Enter a number between and including 0 and 300")]
        )
    
    gender = SelectField('Gender', choices=[
        ('male','Male'), 
        ('female', 'Female'), 
        ('female pregnant', 'Female Pregnant'), 
        ('female lactating', 'Female Lactating')], 
        validators=[validators.Required(
            message='Make a Selection')]
        )


    activity_level = SelectField('Activity Level', choices=[
        ('inactive', 'Inactive: Less than 2 hours of moving'),
        ('average', 'Average: Walking or Standing 2-4 or more hours per day'),
        ('active', 'Active: Physically Active 4 or more hours per day')],
        validators=[validators.Required(
            message='Make a Selection')]
        )

    #     (('inactive', 'Inactive: Less than 2 hours of moving')), (.30),
    #     (('average', 'Average: Walking or Standing 2-4 or more hours per day')), (.50),
    #     (('active', 'Active: Physically Active 4 or more hours per day')), (.75)],
    #     [validators.Required()]
    #     )
    


    # weight_change_weekly = SelectField('Weight Change Weekly', choices=[
    #     (('lose -2.0 lbs or -.91 kg or -.14 stones per week', 'Lose -2.0lbs/-.91kg/-.14 Stones per Week')),(-7000),
    #     (('lose -1.5 lbs or -.68 kg or -.11 stones per week', 'Lose -1.5lbs/-.68kg/-.11 Stones per Week')), (-5250),
    #     (('lose -1.0 lbs or -.45 kg or -.07 stones per week', 'Lose -1.0lbs/-.45kg/-.07 Stones per Week')), (-3500),
    #     (('lose -.5 lbs or -.23 kg or -.03 stones per week', 'Lose -.5 lbs/-.23kg/-.03 Stones per Week')), (-1750),
    #     (('maintain', 'Maintain')), (1)
    #     (('gain .5 lbs or .23 kg or .03 stones per week', 'Gain .5 lbs/.23kg/.03 Stones per Week')), (1750),
    #     (('gain 1.0 lbs or .45 kg or .07 stones per week', 'Gain 1.0lbs/.45kg/.07 Stones per Week'), (3500),
    #     (('gain 1.5 lbs or .68 kg or .11 stones per week', 'Gain 1.5lbs/.68kg/.11 Stones per Week'), (5250),
    #     (('gain 2.0 lbs or .91 kg or .14 stones per week', 'Gain 2.0lbs/.91kg/.14 Stones per Week')], (7000),
    #     [validators.Required()]
    #     )

#finish the changes.
    weekly_change_level = SelectField('Weekly Change Level', choices=[
        ('minus_two_pounds', 'Lose -2.0lbs/-.91kg/-.14 Stones per Week'),
        ('minus_one_and_one_half_pounds', 'Lose -1.5lbs/-.68kg/-.11 Stones per Week'),
        ('minus_one_pound', 'Lose -1.0lbs/-.45kg/-.07 Stones per Week'),
        ('minus_one_half_pound', 'Lose -.5 lbs/-.23kg/-.03 Stones per Week'),
        ('maintain', 'Maintain'),
        ('plus_one_half_pound', 'Gain .5 lbs/.23kg/.03 Stones per Week'),
        ('plus_one_pound', 'Gain 1.0lbs/.45kg/.07 Stones per Week'), 
        ('plus one_and_one_half_pound', 'Gain 1.5lbs/.68kg/.11 Stones per Week'),
        ('plus_two_pounds', 'Gain 2.0lbs/.91kg/.14 Stones per Week')],
        validators=[validators.Required(
            message='Make a Selection')]
    )



    
    
    







    




