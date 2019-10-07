from flask import (flash,
                   render_template, redirect, request,
                   url_for)
from flask_login import (login_required, login_user,
                         logout_user, current_user)
from . import auth_bp
from .forms import LoginForm
from .models import User


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.verify_password(login_form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('blog.index')
            return redirect(next)
        flash('User is not exist or Password is wrong')
    return render_template('auth/login.html', login_form=login_form)


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'info')
    return redirect(url_for('auth.login'))

