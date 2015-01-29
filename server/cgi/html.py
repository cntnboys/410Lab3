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
<form method="get" action ="html2.py">
First name: <input type="text" name="name"><br>
Last name: <input type="text" name="family"><br>
<input type="submit" value="Send">
</form>

<div>

Birthdate: %s     </br>
Main hobby: %s   </br>

</div>


</body>
</html>
''' % (val3, val4)
)
