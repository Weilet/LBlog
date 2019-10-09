from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import SubmitField, StringField, SelectField, TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, URL, Optional, Email
from .models import Category


class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 60)])
    category = SelectField('目录', coerce=int, default=1)
    body = CKEditorField('文章', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]


class CategoryForm(FlaskForm):
    name = StringField('目录名称', validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField('添加目录')

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('Name already exist.')

