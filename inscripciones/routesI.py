from flask import render_template, request, Blueprint, url_for, redirect
from models import db, Inscripciones, Alumnos, Curso
import forms 

insc_bp = Blueprint('inscripciones', __name__)

@insc_bp.route('/insertarIC', methods=['GET','POST'])
def ins_A():
    create_from = forms.UserFormI(request.form)
    create_from.alumno_id.choices = [(a.id, a.nombre) for a in Alumnos.query.all()]
    create_from.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]

    if request.method == 'GET':
        id = request.args.get('id')
        cur = Curso.query.get(int(id))
        create_from.curso_id.data = int(id)
        nombre = cur.nombre
        return render_template("insertarI.html", form=create_from, nombre=nombre)

    if request.method == 'POST':
        print("alumno_id:", create_from.alumno_id.data)
        print("curso_id:", create_from.curso_id.data)
        ya_inscrito = Inscripciones.query.filter_by(
            alumno_id=create_from.alumno_id.data,
            curso_id=create_from.curso_id.data
        ).first() 

        if ya_inscrito:
            error = "Este alumno ya está inscrito en este curso"
            return render_template('insertarI.html', form=create_from, error=error)

        ins = Inscripciones(
            curso_id=create_from.curso_id.data,
            alumno_id=create_from.alumno_id.data,
        )
        db.session.add(ins)
        db.session.commit()
        return redirect(url_for('cursos.cursos_vista'))

    return render_template('insertarI.html', form=create_from)