#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template,redirect, request, flash
from models.department import Department
from models.city import City
from models.sport import Sport
from models.user import User
from models.event import Event
from models import storage
from flask_login import login_user, login_required, logout_user, login_manager
from flask_login import login_required, current_user
from flask_login import LoginManager

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""

    storage.close()


@app.route('/motiv_events', strict_slashes=False)
@login_required
def events():
    """Renders the template of motiv_events.html."""

    departments = storage.all(Department).values()
    events = storage.all(Event).values()
    users = storage.all(User).values()
    sports = storage.all(Sport).values()
    return render_template('motiv_events.html', departments=departments,
                           sports=sports, events=events, users=users,
                           current_user_id=current_user.id)


@app.route('/motiv_users', strict_slashes=False)
@login_required
def users():
    """Renders the template of motiv_users.html."""

    departments = storage.all(Department).values()
    events = storage.all(Event).values()
    users = storage.all(User).values()
    sports = storage.all(Sport).values()
    return render_template('motiv_users.html', departments=departments,
                           sports=sports, events=events, users=users)


@app.route('/motiv_profile', strict_slashes=False)
@login_required
def profile():
    """Renders the template of motiv_profile.html."""

    return render_template('motiv_profile.html', name=current_user.username,
                           current_user_id=current_user.id)


@app.route('/motiv_login', strict_slashes=False)
def login():
    """Renders the template of motiv_login.html."""

    return render_template('motiv_login.html')


@app.route('/motiv_login', methods=['POST'], strict_slashes=False)
def login_post():
    """Login system. If the passwrod is not correct, the user
    can't access to the profile page."""

    username = request.form.get('username')
    password = request.form.get('password')

    user = None
    for usr in storage.all(User).values():
        if usr.password == password and usr.username == username:
            login_user(usr, remember=True)
            return redirect("http://0.0.0.0:5000/motiv_profile")

    if not user or user.password != password:
        flash('Please check your login details and try again.')
        return redirect("http://0.0.0.0:5000/motiv_login")


@app.route('/motiv_signup', strict_slashes=False)
def sigup():
    """Motiv is alive !"""

    return render_template('motiv_signup.html')


@app.route('/motiv_signup', methods=['POST'], strict_slashes=False)
def sigup_post():
    """Method to sign up !"""

    """Get all the information the user entered as input"""
    username = request.form.get('username')
    password = request.form.get('password')
    bio = request.form.get('bio')
    department = request.form.get('department')
    city = request.form.get('city')
    sport = request.form.get('sports')
    sports = sport.split(" ")

    """Associate the user to an existing location
    or to a new location if it doesn't exist"""
    c_id = None
    for c in storage.all(City).values():
        if c.name == city:
            c_id = c.id

    d_id = None
    for d in storage.all(Department).values():
        if d.name == department:
            d_id = d.id

    if not d_id:
        new_dep = Department(name=department)
        new_dep.save()
        d_id = new_dep.id

    if not c_id:
        new_city = City(name=city, department_id=d_id)
        new_city.save()
        c_id = new_city.id

    """Only unique usernames are allowed"""
    for u in storage.all(User).values():
        if u.username == username:
            flash('Username already exists')
            return redirect("http://0.0.0.0:5000/motiv_signup")

    """Create the user"""
    new = User(username=username, password=password, city_id=c_id, bio=bio)

    """Link the user to his sports"""
    all_sports = []
    for sport in storage.all(Sport).values():
        all_sports.append(sport.name)
    for sport in sports:
        if sport not in all_sports:
            flash('Invalid sport. Please put spaces between each sport.')
            return redirect("http://0.0.0.0:5000/motiv_signup")
    for sport in storage.all(Sport).values():
        if sport.name in sports:
            new.sports.append(sport)
    new.save()
    storage.save()

    return redirect("http://0.0.0.0:5000/motiv_login")


@app.route('/motiv_logout', strict_slashes=False)
@login_required
def logout():
    """Logout system."""
    logout_user()
    return redirect("http://0.0.0.0:5000/motiv_login")


@app.route('/user_update/<user_id>', methods=['POST'], strict_slashes=False)
def user_update(user_id):
    """ With this method, the user can update his information."""

    username = request.form.get('username')
    bio = request.form.get('bio')
    department = request.form.get('department')
    city = request.form.get('city')
    sport = request.form.get('sports')
    sports = sport.split(" ")

    user = storage.get(User, user_id)

    if username != "":
        user.username = username
        user.save()

    if bio != "":
        user.bio = bio
        user.save()

    if city != "":
        c_id = None
        for c in storage.all(City).values():
            if c.name == city:
                c_id = c.id

    if department != "":
        d_id = None
        for dep in storage.all(Department).values():
            if dep.name == department:
                d_id = dep.id

    if department != "" and city != "":
        if not d_id:
            new_dep = Department(name=department)
            new_dep.save()
            d_id = new_dep.id

        if not c_id:
            new_city = City(name=city, department_id=d_id)
            new_city.save()
            c_id = new_city.id

        user.city_id = c_id
        user.save()

    if sport != "":
        sport_cpy = sports.copy()
        sports = []
        all_sports = []
        for sport in storage.all(Sport).values():
            all_sports.append(sport.name)
        for sport in sport_cpy:
            if sport not in all_sports:
                continue
            else:
                sports.append(sport)

        for sport in storage.all(Sport).values():
            if sport.name in sports:
                user.sports.append(sport)
        user.save()

    return redirect("http://0.0.0.0:5000/motiv_profile")


if __name__ == '__main__':
    login_manager = LoginManager()
    login_manager.login_view = 'http://0.0.0.0:5000/motiv_login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return storage.get(User, user_id)
    app.secret_key = 'some secret key'
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
