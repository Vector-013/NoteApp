from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECREY_KEY"] = "dni efjn isdjfn s"
    
    return app
