<form action='/HireEmployee' method=POST>
<input type=hidden name=id value={{id}}>
Nickname: <input type=text name=nickname value="{{nickname}}"><br>
Experience: <input type=number name=exp value="{{exp}}"><br>
Sex: <input type=text name=sex value="{{sex}}"><br>
Age: <input type=number name=age value="{{age}}"><br>
Coffee's mugs per day: {{coffee}}<br>
<input type=submit value=" Hire "><br>
</form>