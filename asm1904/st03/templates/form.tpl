<form action='/AddItem' method=POST>
<input type=hidden name=id value={{id}}>
Title: <input type=text name=title value="{{title}}"><br>
Text: <textarea rows=10 cols=50 name=body>{{body}}</textarea><br>
Author: <input type=text name=author value="{{author}}"><br>
<input type=submit value=" Ok "><br>
</form>