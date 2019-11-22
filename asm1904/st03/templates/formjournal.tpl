<form action='/AddItemJournal' method=POST><br>
<input type=hidden name=id value={{id}}>
Title: <input type=text name=title value="{{title}}"><br>
Text: <textarea rows=10 cols=50 name=body>{{body}}</textarea><br>
Author: <input type=text name=author value="{{author}}"><br>
Year: <input type=text name=year value="{{year}}"><br>
<input type=submit value=" Ok "><br>
</form>