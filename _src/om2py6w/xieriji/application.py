from bottle import Bottle, run, route, debug, template, request


from datetime import date
import boto3
s3 = boto3.resource('s3')


application = Bottle()

@application.route('/')
def  submit_diary():
	return template("welcome.tpl")




@application.route('/', method='POST')
def save_diary():	
	if request.forms.get('delete_all') == '':
		bucket = s3.Bucket("xieriji ")
		bucket.put_object("DiaryPool.txt", '')
		return template("welcome.tpl")

	else:
		bucket = s3.Bucket("diarypool")
		history = bucket.Object("DiaryPool.txt")

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
if  __name__ == "__main__":
	application.run(debug=True)