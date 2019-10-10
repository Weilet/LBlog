from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, BooleanField,
                     PasswordField, SubmitField)
from wtforms.validators import (DataRequired, Length, EqualTo)


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('记住我')
    submit = SubmitField('登陆')


class SettingForm(FlaskForm):
    name = StringField('修改用户名', validators=[DataRequired(), Length(1, 70)])
    password1 = PasswordField('修改密码')
    password2 = PasswordField('确认密码', validators=[EqualTo('password1', '两次密码不相同')])
    submit = SubmitField('修改')
