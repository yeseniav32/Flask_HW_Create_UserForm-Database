from flask import Blueprint, render_template, request, flash, url_for, redirect

# Project file imports
from car_inventory.forms import UserLoginForm
from car_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # Add user into Database
            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully a user account for {email}.','user-created')
            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please check your form.')


    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)