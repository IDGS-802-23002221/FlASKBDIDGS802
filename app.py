from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from flask_migrate import Migrate
from maestros.routes import maestros_bp
from alumnos.routesA import alumnos_bp
from cursos.routesC import cursos_bp
from inscripciones.routesI import insc_bp
from models import db 
from models import Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(insc_bp)

db.init_app(app)
csrf=CSRFProtect(app)
migrate=Migrate(app,db)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.route("/", methods=['GET','POST'])
@app.route("/index")

def index():
	create_form=forms.UserForm2(request.form)
	#tem = Alumnos.query('select * from alumnos')
	alumno = Alumnos.query.all()
	return render_template("index.html", form=create_form,alumno=alumno)

	

if __name__ == '__main__':
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)

