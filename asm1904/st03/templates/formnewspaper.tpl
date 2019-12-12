<form action='/AddItemNewspaper' method=POST>
<input type=hidden name=id value={{id}}>
Title: <input type=text name=title value="{{title}}"><br>
Text: <textarea rows=10 cols=50 name=body>{{body}}</textarea><br>
Author: <input type=text name=author value="{{author}}"><br>
Number: <input type=text name=number value="{{number}}"><br>
<input type=submit value=" Ok "><br>
</form>