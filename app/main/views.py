from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import TalkForm,doctorForm
from .. import db
from ..models import Talks,DocTalk


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'



    return render_template('index.html',title=title)
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
def doc_see():
    talks = Talks.query.all()
    form = doctorForm()

    

    if form.validate_on_submit():
        body = form.body.data
        new_body = DocTalk(body=body)
        new_body.save_doctalks()
        return redirect(url_for('main.doc_see'))
    
    return render_template('doctor.html',talks=talks,doctorForm=form)


    