from LBlog import creat_app
from LBlog.auth import auth_bp
from LBlog.blog import blog_bp

app = creat_app('development')

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run()