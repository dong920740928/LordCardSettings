#-*- coding: utf-8 -*-
########################################################################
# File Name: hello.py
# Auhtor: dong920740928
# Mail: dong920740928@gmail.com
# Created Time: Thu Aug  3 22:45:47 2017
#########################################################################

#!/usr/bin/python

import json
import socket
import os
import time
from flask import Flask, request, render_template, send_from_directory

SETTINGS_FILE_NAME="/home/yizhe/workplace/LordCardSettings/settings.json"
SERVER_SCRIPT="/home/yizhe/workplace/team2/server/LordCardServer"
APK_FILE_NAME="resources/lordcard.apk"

arguments = [
    "lordHP",
    "monkeyHP",
    "tangMonkHP",
    "lordCardsNum",
    "monkeyCardsNum",
    "tangMonkCardsNum",
    "lordMaxPower",
    "monkeyMaxPower",
    "tangMonkMaxPower",
    "playCardCD",
    "drawCardCD",
    "luckyCardLive",
    "luckyChance",
    "luckyDamageFactor",
    "candidateNum",
    "monkeyStickDamageFactor",
    "monkeyStickDamageBase",
    "startGameDelay",
    "skillDelay",
    "reconnectDelay",
    "chooseRolesDelay",
    "scrollDuration",
    "scrollAddCD",
    "drawCardRP",
    "tangMonkFrozenDuration"
    ]

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
        if "reset" in request.args:
            #reset server
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(bytes("exit\n", "utf-8"), ("localhost", 14444))
                s.close()
            except socket.error:
                print("error when send to server:")
            time.sleep(0.3)
        else:
            #change arguments
            for argument_name, argument_value in request.args.items(): 
                if argument_name in settings:
                    settings[argument_name] = argument_value
                    settings_file = open(SETTINGS_FILE_NAME, "w")
                    settings_file.write(json.dumps(settings))
                    settings_file.close()

    return render_template("settings.html", arguments=arguments, settings=settings)

@app.route('/download', methods=['GET'])
def get_apk():
    return render_template("download.html", file_name=APK_FILE_NAME)

@app.route('/resouces/<path:file_name>', methods=['GET'])
def get_file(file_name):
    return send_from_directory(APK_FILE_NAME, APK_FILE_NAME)

if __name__ == '__main__':
    app.run()
