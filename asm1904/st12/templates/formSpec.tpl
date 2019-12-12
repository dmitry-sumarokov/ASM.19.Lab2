<form action='/AddItemSpecialist' method=POST>
    <h2><p>Специалист:</p></h2>
    <font size=4 face="Courier">
        <p><input type=hidden name=id value={{id}}></p>
        <p>Имя: <input type=text name=Fname value="{{Fname}}"></p>
        <p>Фамилия: <input type=text name=Sname value="{{Sname}}"></p>
        <p>Email: <input type=text name=Email value="{{Email}}"></p>
        <p><input type=submit value=" Ok "></p>
    </font>
</form>