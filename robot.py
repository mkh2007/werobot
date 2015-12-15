# -*- coding: utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='abcdefghijklmn', enable_session=True)

@robot.handler
def echo(message):
    return 'Hello World!'

robot.run()
