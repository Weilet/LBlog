from flask import render_template
from . import blog_bp
from flask_login import login_required
from .forms import CategoryForm, CommentForm
from .models import Post


@blog_bp.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/friend')
def friend():
    return render_template('blog/friend.html')


@blog_bp.route('/post')
@login_required
def post():
    pass


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')



