from bottle import Bottle, run, route, debug, template, request

import sae
from sae.storage import Bucket
from datetime import date

app = Bottle()

@app.route('/')
def  submit_diary():
	return template("welcome.tpl")




@app.route('/', method='POST')
def save_diary():	
	if request.forms.get('delete_all') == '':
		bucket = Bucket("diarypool")
		bucket.put_object("DiaryPool.txt", '')
		return template("welcome.tpl")

	else:
		bucket = Bucket("diarypool")
		history = bucket.get_object_contents("DiaryPool.txt")

		diary_submit = request.forms.get('mydiary')
		if not diary_submit == '':
			history = history +str(date.today()) + "|---" + str(diary_submit)+"\n"
			bucket.put_object("DiaryPool.txt", history)
		
		history_line = history.split("\n")
		
		return template("show_history.tpl", history=history_line)


# @app.route('/', method='GET')
# def clear_diary():
# 	if request.GET.get('delete_all','').strip():
# 		bucket = Bucket("diarypool")
# 		bucket.put_object("DiaryPool.txt", '')
# 	return template("welcome.tpl")

application = sae.create_wsgi_app(app)