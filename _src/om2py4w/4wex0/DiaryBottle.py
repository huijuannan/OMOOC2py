# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Usage:
'''
from bottle import run, route, debug, template, request
@route('/diary')
def  submit_diary():
	return '''
	<form action="/diary" method="post">
	<input name="mydiary" type="text">
	<br />
	<input type="submit" value="submit">
	</form>
	'''



@route('/diary', method='POST')
def save_diary():
	diary_submit = request.forms.get('mydiary')
	file = open("DiaryPool.txt","a")
	file.write(str(diary_submit)+"\n")
	file.close()

	file = open("DiaryPool.txt")
	history = file.readlines()
	file.close()
	for i in range(len(history)):
		history[i] = history[i] + '<br />'

	return history
	



if __name__ == "__main__":
	debug(True)
	run(host="localhost", port = 8080, reloader = True)
