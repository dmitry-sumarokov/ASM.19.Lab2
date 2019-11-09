ID: {{number}}<br>
Name: {{items[number]._name}}<br>
Gender: {{items[number]._gender}}<br>
Age: {{items[number]._age}}<br>
Colour: {{items[number]._colour}}<br>
This cat's saying: {{ items[number]._cat.do_meow() }}<br>
<a href="/DeleteItem/{{number}}">Del</a><br>
<a href="/ShowForm/{{number}}">Edit</a><br>
<a href="/DoMeow/{{number}}">Do special meow</a><br>
