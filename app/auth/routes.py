from flask import render_template, request,flash,redirect,url_for

from app.auth import auth_bp
from app.auth.forms import RegistrationForm
from app.auth.models import User

@auth_bp.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()
    if form.validate_on_submit(): #post request and validate form
        user = User.create_user(
            form.name,
            form.email,
            form.password
        )
        flash('Registration Successful')
        return redirect(url_for('auth_bp.login_user'))

    return render_template('registration.html', form=form)


@auth_bp.route('/login',methods=['GET','POST'])
def login_user():
    return render_template('login.html')