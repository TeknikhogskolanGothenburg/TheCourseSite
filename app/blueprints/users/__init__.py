from bson import ObjectId
from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, login_required, current_user

from app.controllers.message_controller import create_message, get_all_messages_for_user, get_message_by_id

bp_user = Blueprint('bp_user', __name__)


@bp_user.before_request
def before_request():
    if not current_user.is_authenticated or not current_user.has_access('user'):
        return redirect(url_for('bp_open.index'))

@bp_user.get('/signout')
def signout_get():
    logout_user()
    return redirect(url_for('bp_open.index'))


@bp_user.get('/courses')
def courses_get():
    return render_template('courses.html')


@bp_user.get('/message')
def message_get():
    messages = get_all_messages_for_user()
    return render_template('message.html', messages=messages)


@bp_user.post('/message')
def message_post():
    to = request.form['to']
    message = request.form['message']
    create_message(to, message)
    return redirect(url_for('bp_user.message_get'))


@bp_user.get('/read_message/<message_id>')
def read_message(message_id):
    message = get_message_by_id(ObjectId(message_id))
    message.read = True
    message.save()
    message.message_body = message.message_body.replace('\n', '<br />')
    return render_template('single_message.html', message=message)
