# -*- coding: utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='abcdefghijklmn', enable_session=False)

application = robot.wsgi

@robot.filter('a')
def echo(message):
	return 'www.4g-cmcc.com'

@robot.handler
def echo(message):
    return 'Hello World!'

