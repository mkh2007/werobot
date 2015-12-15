# -*- coding: utf-8 -*-
import werobot

robot = werobot.WeRoBot(token='abcdefghijklmn', enable_session=False)

application = robot.wsgi

@robot.filter('a')
def echo(message):
	return u'你好'

@robot.handler
def echo(message):
    return 'Hello World!'

