<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>My Diary</title>
	<link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
	<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
	<script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
<form class="form-horizontal" role="form" action="/diary" method="post">

<div class="form-group">
	<div class="col-sm-10">
		<input name="mydiary" type="text" class="form-control" placeholder="今天过得如何？">
	</div>
	</div>
	
<div class="form-group">
<div class="col-sm-offset-0 col-sm-10">
<button type="submit" class="btn btn-default">提交</button>
</div>
</div>
</form>
</div>



<div class="container">
	%for i in history:
	<p class="text-center">{{i}}</p>
	%end
</div>

</body>
</html>