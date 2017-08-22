from flask import Flask

from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.config.from_object('instance.config.DevelopConfig')

from app.views import *

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
