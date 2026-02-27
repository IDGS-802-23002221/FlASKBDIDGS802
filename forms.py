from wtforms import Form 
from wtforms import StringField, IntegerField, DateField, EmailField

from wtforms import validators 

class UserForm2(Form):
    # lo que aparece en el html 
    id = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=1000, message="ingrese un valor valido")
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"), 
    ])
    
    apellidos = StringField("Apellidos",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email = EmailField("Email", [
        validators.DataRequired(message="El campo es requerido")
    ])
    telefono = IntegerField("Telefono", [
        validators.DataRequired(message="El campo es requerido")
    ])

    created_date = DateField("created_date", [
        validators.DataRequired(message="Ingrese un correo valido")
    ])


class UserFormM(Form):
    # lo que aparece en el html 
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"), 
    ])
    
    apellidos = StringField("Apellidos",[
        validators.DataRequired(message="El campo es requerido")
    ])
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="El campo es requerido")
    ])
    email = EmailField("Email", [
        validators.DataRequired(message="El campo es requerido")
    ])

    created_date = DateField("created_date", [
        validators.DataRequired(message="Ingrese un correo valido")
    ])
