from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Curso, Maestros
import forms 

cursos_bp = Blueprint('cursos', __name__)

@cursos_bp.route('/Curso', methods=['GET'])
def cursos_vista():
    curso = Curso.query.all()
    create_from = forms.UserFormC(request.form)

    return render_template('curso.html', form=create_from, curso=curso)

@cursos_bp.route('/insertarC', methods=['GET','POST'])
def insertC():
    create_from = forms.UserFormC(request.form)

    create_from.maestro_id.choices = [
        (m.matricula, m.nombre) for m in Maestros.query.all()
    ]
    if request.method == 'POST':
        curso=Curso(nombre=create_from.nombre.data,
                    descripcion=create_from.descripcion.data,
                    maestro_id=create_from.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.cursos_vista'))
    return render_template('insertarC.html', form=create_from)

@cursos_bp.route('/modificarC', methods=['GET','POST'])
def editarC():
    create_from = forms.UserFormC(request.form)
    create_from.maestro_id.choices = [
         (m.matricula, m.nombre) for m in Maestros.query.all() 
         ]
    
    if request.method == 'GET': 
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id==id).first()
        create_from.id.data=request.args.get('id')
        create_from.nombre.data=cur.nombre
        create_from.descripcion.data=cur.descripcion
        create_from.maestro_id.data=cur.maestro_id
    
    if request.method == 'POST': 
        id = create_from.id.data
        cur = db.session.query(Curso).filter(Curso.id==id).first()
        cur.id = id
        cur.nombre = str.rstrip(create_from.nombre.data)
        cur.descripcion = create_from.descripcion.data
        cur.maestro_id = create_from.maestro_id.data
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.cursos_vista'))
    
    return render_template('modificarC.html', form=create_from)

@cursos_bp.route('/detallesC', methods=['GET'])
def detallesC():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id==id).first()
    return render_template('detallesC.html', curso=curso)


@cursos_bp.route('/eliminarC', methods=['GET','POST'])
def eliminarC():
    create_from = forms.UserFormC(request.form)
    create_from.maestro_id.choices = [
        (m.matricula, m.nombre) for m in Maestros.query.all()
    ]
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id==id).first()
        create_from.id.data = cur.id
        create_from.nombre.data = cur.nombre 
        create_from.descripcion.data = cur.descripcion
        create_from.maestro_id.data = cur.maestro_id

    if request.method == 'POST': 
        id = create_from.id.data
        cur = db.session.query(Curso).filter(Curso.id==id).first()
        db.session.delete(cur)
        db.session.commit()
        return redirect(url_for('cursos.cursos_vista'))
    return render_template('eliminarC.html', form=create_from)
