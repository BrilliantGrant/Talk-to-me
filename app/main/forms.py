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