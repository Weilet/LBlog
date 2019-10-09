from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from . import blog_bp
from .forms import CategoryForm, PostForm
from .models import Post, Category
from LBlog import db


@blog_bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/friend')
def friend():
    return render_template('blog/friend.html')


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/post', methods=['GET', 'POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.body.data
        category = Category.query.get(post_form.category.data)
        post = Post(title=title, body=body, category=category)
        db.session.add(post)
        db.session.commit()
        flash('发布成功', 'success')
        return redirect(url_for('blog.index'))
    return render_template('blog/post.html', post_form=post_form)


@blog_bp.route('/post/show/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('blog/show_post.html', post=post)


@blog_bp.route('/category', methods=['GET', 'POST'])
@login_required
def new_category():
    category_form = CategoryForm()
    categories = Category.query.all()
    if category_form.validate_on_submit():
        category = Category(name=category_form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('添加成功')
        return redirect(url_for('blog.new_category'))
    return render_template('blog/category.html', category_form=category_form, categories=categories)


@blog_bp.route('/category/del/<int:category_id>', methods=['POST'])
@login_required
def del_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('blog.new_category'))




