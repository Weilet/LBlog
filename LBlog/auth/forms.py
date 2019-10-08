from flask_wtf import FlaskForm
from wtforms import (IntegerField, StringField, BooleanField,
                     PasswordField, SubmitField)
from wtforms.validators import (DataRequired, Length, Email, Regexp)


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('记住我')
    submit = SubmitField('登陆')


class SettingForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired(), Length(1, 70)])
    submit = SubmitField('修改')
