#-*- coding: utf-8 -*-
########################################################################
# File Name: hello.py
# Auhtor: dong920740928
# Mail: dong920740928@gmail.com
# Created Time: Thu Aug  3 22:45:47 2017
#########################################################################

#!/usr/bin/python

SETTINGS_FILE_NAME="settings.json"
import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello!'


@app.route('/settings', methods=['GET'])
def view_settings():
    settings_file = open(SETTINGS_FILE_NAME, 'r')
    settings = json.load(settings_file)
    settings_file.close()
    if len(request.args) > 0:
        #change arguments
        for argument_name, argument_value in request.args.iteritems(): 
            if settings.has_key(argument_name):
                settings[argument_name] = argument_value
                settings_file = open(SETTINGS_FILE_NAME, "w")
                settings_file.write(json.dumps(settings))
                settings_file.close()

    return render_template("settings.html", settings=settings)

if __name__ == '__main__':
    app.run()
