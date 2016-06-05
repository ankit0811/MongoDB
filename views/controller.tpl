<!DOCTYPE html>
<html>
<head>
<title>Second Sample with Controller Eg.</title>
</head>
<body>
<ul>
%for i in Arr:
<li>{{i}}</li>
%end
<form action="/Selection" method="POST"> <!--The action should be same as bottle.post -->
What is your favourite thing?
<input type="text" name="thing" size=40 value=""><br>
<input type="Submit" value="Submit">
</form>
</ul>
</body>
</html>