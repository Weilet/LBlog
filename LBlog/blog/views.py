from flask import flash, render_template, redirect, request, url_for
from flask_login import login_required
from . import blog_bp
from .forms import CategoryForm, PostForm
from .models import Post, Category
from LBlog import db


@blog_bp.route('/')
def index():
    posts = Post.query.order_by(db.desc(Post.id)).all()
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/friend')
def friend():
    return render_template('blog/friend.html')


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/search/', methods=['GET'])
def search():
    keyword = request.args['keyword']
    posts = Post.query.filter(Post.title.contains(keyword) | Post.body.contains(keyword)).all()
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/post', methods=['GET', 'POST'])
@login_required
def add_post():
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
    return render_template('blog/add_post.html', post_form=post_form)


@blog_bp.route('/post/del/<int:post_id>', methods=['POST'])
@login_required
def del_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    flash('删除成功', 'info')
    return redirect(url_for('blog.index'))


@blog_bp.route('/post/show/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('blog/show_post.html', post=post)


@blog_bp.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post_form = PostForm()
    post = Post.query.filter_by(id=post_id).first_or_404()
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.body = post_form.body.data
        db.session.commit()
        return redirect(url_for('blog.index'))
    post_form.title.data = post.title
    post_form.body.data = post.body
    post_form.category.data = post.category
    return  render_template('blog/add_post.html', post_form=post_form)


@blog_bp.route('/category', methods=['GET', 'POST'])
@login_required
def add_category():
    category_form = CategoryForm()
    categories = Category.query.all()
    if category_form.validate_on_submit():
        category = Category(name=category_form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('添加目录成功', 'info')
        return redirect(url_for('blog.add_category'))
    return render_template('blog/category.html', category_form=category_form, categories=categories)


@blog_bp.route('/category/del/<int:category_id>', methods=['POST'])
@login_required
def del_category(category_id):
    category = Category.query.filter_by(id=category_id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    flash('删除目录成功', 'info')
    return redirect(url_for('blog.add_category'))


@blog_bp.route('/category/edit/<int:category_id>', methods=['POST'])
@login_required
def edit_category(category_id):
    new_name = request.form['new_name']
    if Category.query.filter_by(name=new_name).first_or_404():
        flash('目录已存在', 'warning')
        return redirect(url_for('blog.add_category'))
    category = Category.query.filter_by(id=category_id).first_or_404()
    category.name = new_name
    db.session.commit()
    flash('修改目录成功', 'info')
    return redirect(url_for('blog.add_category'))



