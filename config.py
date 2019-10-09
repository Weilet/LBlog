from collections import defaultdict
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    @property
    def SECRET_KEY(self):
        return os.environ.get('SECRET_KEY') or \
               'Lily-is-cool'

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    @property
    def DEBUG(self):
        return True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.environ.get('SQLALCHEMY_DATABASE_URI') or \
            'sqlite:///' + os.path.join(basedir, 'dev.db')

    @property
    def SQLALCHEMY_TRACK_MODIFICATIONS(self):
        return True

    @property
    def CKEDITOR_ENABLE_CODESNIPPET(self):
        return True

    @property
    def CKEDITOR_ENABLE_MARKDOWN(self):
        return True

    @property
    def CKEDITOR_PKG_TYPE(self):
        return 'full'


config = defaultdict(DevelopmentConfig, {
    'development': DevelopmentConfig()
})

