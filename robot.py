# -*- coding: utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='abcdefghijklmn', enable_session=False)

@robot.handler
def echo(message):
    return 'Hello World!'

application = robot.wsgi
