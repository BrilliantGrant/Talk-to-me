from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import TalkForm,doctorForm,docdetails,patient_form
from .. import db
from ..models import Talks,DocTalk,Doctor_details,Patient


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'



    return render_template('ChatApp.html',title=title)
@main.route('/talk', methods=['GET', 'POST'])

def post_comment():
    ''' function to post comments '''
    form = TalkForm()
    talks = Talks.query.all()

    

    if form.validate_on_submit():
        body = form.body.data
        new_body = Talks(body=body)
        new_body.save_talks()
        return redirect(url_for('main.post_comment'))
    return render_template('talks.html', comment_form=form,talks=talks)

@main.route('/doc',methods=['GET', 'POST'])
def doc_details():
    docde = docdetails()
    if docde.validate_on_submit():
        license = docde.license.data
        phone_number = docde.phone_number.data
        profile_pic_path = docde.profile_pic_path.data
        bio = docde.bio.data
        
        new_body = Doctor_details(license=license,phone_number=phone_number,profile_pic_path=profile_pic_path,bio=bio)
        new_body.save_docdetails()
        return redirect(url_for('main.view_patient  '))
    
    return render_template('doctordetails.html',docde=docde)

@main.route('/view-doc')
def view_docdetails():

    print()

    docdetails = Doctor_details.query.all()
    print(docdetails)
    if docdetails is None:
        abort(404)


    return render_template  ('view-docdetails.html',docdetails=docdetails)
@main.route('/user',methods=['GET', 'POST'])
def user():
    userform = patient_form()
    if userform.validate_on_submit():
        body = userform.body.data
        sad = userform.sad.data
        feeling = userform.feeling.data
        mood = userform.mood.data

        new_user = Patient(body=body,sad=sad,feeling=feeling,mood=mood)
        new_user.save_patients()
        return redirect(url_for('main.view_docdetails'))

    return render_template('patient.html', userform=userform)

@main.route('/view-patient')
def view_patient():
    patient = Patient.query.all()

    print(patient)

    if patient is None:
        abort (404)

    return render_template('view-patient.html' ,patient = patient )