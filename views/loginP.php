<html>
<head>
<title>Login</title>
</head>
<body>
<?php
$usuario="TuUsuario";
$contraseña="TuContraseña";
$user=$_POST['user'];
$pass=$_POST['pass'];

if ($user!=$usuario)
{
echo "Usuario incorrecto";
}
elseif ($pass!=$contraseña)
{
echo "Contraseña incorrecta";
}
else
{
echo <a href="/CrudDB.html">Lista De Datos</a>;
}
?>
</body>