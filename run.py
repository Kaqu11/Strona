from flask import Flask
from app.views import views


app = Flask(
    __name__,
    template_folder='app/templates',
    static_folder='app/static'
)

app.register_blueprint(views)


if __name__ == '__main__':
    app.secret_key = 'a206feaca73e86c740a2d017c1ead06d'

    app.debug = True

    app.run()