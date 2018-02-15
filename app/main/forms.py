from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from wtforms.validators import Required


class TalkForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    body = TextAreaField('',validators=[Required()])
    submit = SubmitField('send')

class doctorForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    body = TextAreaField('',validators=[Required()])
    submit = SubmitField('send')

class docdetails(FlaskForm):
    license = StringField('enter your license', validators=[Required()])
    phone_number = StringField('enter your phone number', validators=[Required()]) 
    profile_pic_path = StringField('enter the url of your photo', validators=[Required()])
    bio = StringField('enter your bio',validators=[Required()])
    submit = SubmitField('save')

class patient_form(FlaskForm):
    body = StringField('share your story with us', validators=[Required()])
    sad = StringField('what makes you sad easily?', validators=[Required()])
    feeling = StringField('how are you feeling today?', validators=[Required()])
    mood = StringField('doyou wanna talk or call a doctor?', validators=[Required()])
    submit = SubmitField('save')