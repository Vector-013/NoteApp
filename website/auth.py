from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = False)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        if len(email) < 4:
            flash("Email must be greater than 4 chars", category="error")
            
        elif len(firstName) < 2:
            flash("too short name", category="error")
            
        elif len(password1) < 7:
            flash("password to short", category="error")
        elif password1 != password2:
            flash("Passwords dont match", category="error")
        else:
            
            new_user = User(email = email, password=generate_password_hash(password1), first_name = firstName)
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")
            return redirect(url_for("views.home"))
    
    return render_template("sign_up.html")
