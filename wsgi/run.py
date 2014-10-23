#!/usr/bin/env python
import os
import re
import datetime
from flask import Flask, render_template, redirect, url_for, request, session
from config import DB_CONFIG
import pymongo_safe
from pprint import pprint
# import httplib2

from dashboard import dashboard_app
# from servers.controller import bp_app as servers_app
# from gateways.controller import bp_app as gateways_app
# from networks.controller import bp_app as networks_app

# user: admin
# password: iop-098


app = Flask('G12')
app.config.from_object('config')
# database
# conn = pymongo_safe.MongoHandler(DB_CONFIG)
# app.db = conn['portal'].portal

# Blueprints...
# -------------------------------------------------------------------------------------------------------------------
app.register_blueprint(dashboard_app)
# app.register_blueprint(servers_app)
# app.register_blueprint(gateways_app)
# app.register_blueprint(networks_app)


# @app.before_request
# def before_request():
#     if request.endpoint is None and app.static_regex.match(request.path):
#         path_split = request.path.split('/')
#         for static_folder in ('css', 'font', 'img', 'js'):
#             try:
#                 return redirect(os.path.join('/static', '/'.join(path_split[path_split.index(static_folder):])))
#             except:
#                 continue
#
#     if 'username' not in session and request.endpoint not in ('login_form', 'login_submit', 'static'):
#         return redirect(url_for('login_form'))


@app.before_request
def before_request():
    pass
    # print request.endpoint
    # print session

    # if request.endpoint != 'static':
    #     if request.endpoint not in ('user.login_form', 'user.login_submit') and 'authorized' not in session:
    #         return redirect(url_for('user.login_form'))

    # if request.endpoint in ('user.login_form', 'user.login_submit') and 'authorized' in session:
    #     return redirect(url_for('user.login_form'))

    # print('-------------------BEFORE REQUEST-------------------')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])