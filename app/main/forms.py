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

class patientForm(FlaskForm):
    body = TextAreaField('How you feeling',validators=[Required()])
    comment = TextAreaField(' how would you describe your mood?',validators=[Required()])
    choice = TextAreaField('',validators=[Required()])
    submit = SubmitField('send')
    category =SelectField('choose from the following categories', choices=[('sad','sad'),('feeling','feeling'),('mood','mood')],validators=[Required()])