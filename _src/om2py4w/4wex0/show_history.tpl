<!DOCTYPE html>
<html>
<head>
	<title>My Diary</title>
</head>
<body>
<div>
	<form action="/diary" method="post">
	<input name="mydiary" type="text">
	<br />
	<input type="submit" value="submit">
	</form>
</div>
<div>
	%for i in history:
	<p>{{i}}</p>
	%end
</div>
</body>
</html>