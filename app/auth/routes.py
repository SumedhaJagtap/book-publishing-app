from flask import render_template, request,flash,redirect,url_for
from flask_login import login_user,logout_user,login_required
from app.auth import auth_bp
from app.auth.forms import RegistrationForm,LoginForm
from app.auth.models import User

@auth_bp.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration Successful')
        return redirect(url_for('auth_bp.signin_user'))
    return render_template('registration.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def signin_user():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))
        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('catalog_bp.display_books'))
    return render_template('login.html', form=form)

@auth_bp.route('/logout',methods=['GET','POST'])
@login_required
def signout_user():
    logout_user()
    return redirect(url_for('catalog_bp.display_books'))
