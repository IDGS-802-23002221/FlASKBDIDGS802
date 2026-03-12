from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Alumnos 
import forms

alumnos_bp=Blueprint('alumnos',__name__)

#getall - index
@alumnos_bp.route('/Alumnos',methods=['GET'])
def Alumnos_vista():
	alumno = Alumnos.query.all()
	create_from=forms.UserForm2(request.form)
	
	return render_template("Alumnos.html",form=create_from, alumno=alumno)

#registrar
@alumnos_bp.route("/insertarA",methods=['GET','POST'])
def insertarA():
	create_from=forms.UserForm2(request.form)
	if request.method=='POST':

		alumno=Alumnos(nombre=create_from.nombre.data,
			   	     apellidos=create_from.apellidos.data,
					 telefono=create_from.telefono.data,
					 email=create_from.email.data
					  )
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('alumnos.Alumnos_vista'))
	return render_template("insertarA.html",form=create_from)

#modificar
@alumnos_bp.route("/modificarA",methods=['GET','POST'])
def modificar():
	create_from=forms.UserForm2(request.form)
	if request.method=='GET':
		id =request.args.get('id') 
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_from.id.data=request.args.get('id')
		create_from.nombre.data=alum1.nombre
		create_from.apellidos.data=alum1.apellidos
		create_from.telefono.data=alum1.telefono
		create_from.email.data=alum1.email

	if request.method=='POST':
		id =create_from.id.data
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id = id 
		alum1.nombre = str.rstrip(create_from.nombre.data) 
		alum1.apellidos = create_from.apellidos.data
		alum1.telefono = create_from.telefono.data
		alum1.email = create_from.email.data 
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.Alumnos_vista'))

	return render_template("modificar.html",form=create_from )

#detalles 
@alumnos_bp.route("/detalles",methods=['GET','POST'])
def detalles():
	id = request.args.get('id')
	alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
	return render_template("detalles.html",alumno=alum)


#eliminar
@alumnos_bp.route("/eliminar",methods=['GET', 'POST'])
def eliminar():
	create_from=forms.UserForm2(request.form)
	if request.method=='GET':
		id =request.args.get('id') 
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_from.id.data=request.args.get('id')
		create_from.nombre.data=alum1.nombre
		create_from.apellidos.data=alum1.apellidos
		create_from.telefono.data=alum1.telefono
		create_from.email.data=alum1.email
	if request.method=='POST':
		id =create_from.id.data
		alum1 = Alumnos.query.get(id)
		db.session.delete(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.Alumnos_vista'))

	return render_template("eliminar.html",form=create_from )