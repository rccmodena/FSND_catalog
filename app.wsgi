#!/usr/bin/python3

import sys

sys.path.insert(0,"/var/www/catalog/catalog")
activate_this = '/var/www/catalog/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from catalog import app as application
application.secret_key = '##THIS_IS_THE_SECRET_KEY_FOR_THIS_APPLICATION##'

