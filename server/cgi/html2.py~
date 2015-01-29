#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
val1 = form.getvalue('name')
val2 = form.getvalue('family')
val3 = form.getvalue('birthdate')
val4 = form.getvalue('main hobby')


 
print('''Content-type: text/html

<!DOCTYPE html> 
<html>
<body>
<form method="get" action ="html.py">
Birthdate: <input type="text" name="birthdate"><br>
main hobby: <input type="text" name="main hobby"><br>
<input type="submit" value="Send">
</form>

<div>

Name: %s     </br>
Family: %s   </br>

</div>


</body>
</html>
''' % (val1, val2)
)
