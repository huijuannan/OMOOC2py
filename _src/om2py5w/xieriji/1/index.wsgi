from bottle import Bottle, run, route, debug, template, request

import sae
from sae.storage import Bucket

app = Bottle()

@app.route('/')
def  submit_diary():
	return template("welcome.tpl")




@app.route('/', method='POST')
def save_diary():
	diary_submit = request.forms.get('mydiary')
	# file = open("DiaryPool.txt","a")
	# file.write(str(diary_submit)+"\n")
	# file.close()


	bucket = Bucket("diarypool")
	history = bucket.get_object_contents("DiaryPool.txt")
	history_line = history.split("\n")
	

	# file = open("DiaryPool.txt")
	# history = file.readlines()
	# file.close()
	
	return template("show_history.tpl", history=history_line)

application = sae.create_wsgi_app(app)