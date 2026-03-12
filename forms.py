from wtforms import Form 
from wtforms import StringField, IntegerField, DateField, EmailField, SelectField

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

class UserFormC(Form):

    id = IntegerField("ID", [
        validators.DataRequired(message="El campo es requerido"),
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"), 
    ])
    
    descripcion = StringField("Descripcion",[
        validators.DataRequired(message="El campo es requerido")
    ])
   
    maestro_id = SelectField("Maestro", coerce=int, validators=[
        validators.DataRequired(message="El campo es requerido")
    ])

class UserFormI(Form):

    alumno_id = SelectField("Alumno", [validators.DataRequired(message="El campo es requerido")])

    curso_id = SelectField('Curso', [validators.DataRequired(message="El campo es requerido")]) 

    fecha_inscripcion = DateField('fecha Inscripcion', [validators.DataRequired(message="El campo es requerido")])

    