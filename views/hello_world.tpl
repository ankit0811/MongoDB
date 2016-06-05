<!DOCTYPE html>
<html>
<head>
<title>First Sample </title>
</head>
<body>
Welcome {{username}}
<ul>
%for i in arr:
<li>{{i}}</li>
%end
</ul>
</body>
</html>