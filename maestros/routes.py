from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Maestros 
import forms

maestros_bp=Blueprint('maestros',__name__)

#getall - index
@maestros_bp.route('/maestros',methods=['GET'])
def maestros_index():
    create_from=forms.UserFormM(request.form)
    mae = Maestros.query.all()

    return render_template("maestros.html", form=create_from, mae=mae )

#registrar
@maestros_bp.route("/insertarM",methods=['GET','POST'])
def insertarM():
	create_fromM=forms.UserFormM(request.form)
	if request.method=='POST':

		mae=Maestros(matricula=create_fromM.matricula.data,
			   	     nombre=create_fromM.nombre.data,
			   	     apellidos=create_fromM.apellidos.data,
					 email=create_fromM.email.data,
					 especialidad=create_fromM.especialidad.data
					  )
		db.session.add(mae)
		db.session.commit()
		return redirect(url_for('maestros.insertarM'))
	return render_template("insertarM.html",form=create_fromM)

#modificar
@maestros_bp.route("/modificarM",methods=['GET','POST'])
def modificarM():
	create_fromM=forms.UserFormM(request.form)
	if request.method=='GET':
		matricula =request.args.get('matricula') 
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_fromM.matricula.data=request.args.get('matricula')
		create_fromM.nombre.data=mae1.nombre
		create_fromM.apellidos.data=mae1.apellidos
		create_fromM.especialidad.data=mae1.especialidad
		create_fromM.email.data=mae1.email

	if request.method=='POST':
		matricula = create_fromM.matricula.data
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		mae1.matricula = matricula 
		mae1.nombre = str.rstrip(create_fromM.nombre.data) 
		mae1.apellidos = create_fromM.apellidos.data
		mae1.especialidad = create_fromM.especialidad.data
		mae1.email = create_fromM.email.data 
		db.session.add(mae1)
		db.session.commit()
		return redirect(url_for('maestros.insertarM'))

	return render_template("modificarM.html",form=create_fromM )

#detalles 
@maestros_bp.route("/detallesM",methods=['GET','POST'])
def detalles():
	nombre = ""
	apellidos = "" 
	especialidad = ""
	email = ""
	create_fromM=forms.UserFormM(request.form)
	if request.method=='GET':
		matricula =request.args.get('matricula') 
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula =request.args.get('matricula') 
		nombre=mae1.nombre
		apellidos=mae1.apellidos
		especialidad=mae1.especialidad
		email=mae1.email

	return render_template("detallesM.html",form=create_fromM,nombre=nombre,apellidos=apellidos,especialidad=especialidad,email=email )


#eliminar
@maestros_bp.route("/eliminarM",methods=['GET', 'POST'])
def eliminarM():
	create_fromM=forms.UserFormM(request.form)
	if request.method=='GET':
		matricula =request.args.get('matricula') 
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_fromM.matricula.data=request.args.get('matricula')
		create_fromM.nombre.data=mae1.nombre
		create_fromM.apellidos.data=mae1.apellidos
		create_fromM.especialidad.data=mae1.especialidad
		create_fromM.email.data=mae1.email
	if request.method=='POST':
		matricula = create_fromM.matricula.data
		mae1 = Maestros.query.get(matricula)
		db.session.delete(mae1)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template("eliminarM.html",form=create_fromM)

