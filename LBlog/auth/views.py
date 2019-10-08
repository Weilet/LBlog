from flask import (flash,
                   render_template, redirect, request,
                   url_for)
from flask_login import (login_required, login_user,
                         logout_user, current_user)
from . import auth_bp
from .forms import LoginForm, SettingForm
from .models import User
from LBlog import db


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
                next = url_for('auth.login')
            return redirect(next)
        flash('用户不存在或密码错误', 'warning')
    return render_template('auth/login.html', login_form=login_form)


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('登出成功', 'info')
    return redirect(url_for('blog.index'))


@auth_bp.route('/setting', methods=['GET', 'POST'])
@login_required
def setting():
    setting_form = SettingForm()
    if setting_form.validate_on_submit():
        current_user.username = setting_form.name.data
        db.session.commit()
        flash('个人信息修改成功', 'info')
        return redirect(url_for('blog.index'))
    return render_template('auth/setting.html', setting_form=setting_form)