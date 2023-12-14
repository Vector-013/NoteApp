from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    ## app.config["SECREY_KEY"] = "dniefjnisdjfns"
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix= "/")
    app.register_blueprint(auth, url_prefix= "/")
    
    return app
