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
<header class="jumbotron" id="overview">
	<div class="container text-center">
	<h1 >Dear Diary</h1>
	
		<p class= "lead">Happiness is not determined by what's happening around you</p>
		<p class= "lead">but rather what's happening inside you</p>
	
	
	</div>
</header>

<div class="container">
<div class="row">
<form role="form" action="/" method="post">
<div class="input-group input-group-lg">
	
	<input  class="form-control" name="mydiary" type="text" placeholder="今天过得如何？">
	<span class="input-group-btn">
	<button type="submit" class="btn btn-default">提交</button>	
	</span>

</div>

</form>

<form action="/" method="post">
<button type="submit" name="delete_all" class="btn btn-default">清空日记本</button>
	
</form>
</div>
</div>


<div class="container">
<br/>
	%for i in history:
	<p class="text-left">{{i}}</p>
	%end
</div>

</body>
</html>