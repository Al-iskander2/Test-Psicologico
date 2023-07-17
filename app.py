import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import generate_password_hash

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///patients.db")

PASSWORD = "im"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def index_form():
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
        drogas = request.form.getlist("drogas")

        # Insertar paciente en la base de datos
        db.execute(
            "INSERT INTO patients (nombre, edad, drogas) VALUES (:nombre, :edad, :drogas)",
            nombre=nombre, edad=edad, drogas=", ".join(drogas)
        )

        # Obtener el ID del paciente recién insertado
        patient_id = db.execute("SELECT last_insert_rowid() AS id")[0]["id"]

        # Redirigir a la página de test con el ID del paciente
        return redirect(url_for("test", patient_id=patient_id))
    else:
        return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        submit_value = request.form.get("submit")
        patient_id = int(request.form.get("patient_id"))
        column_number = int(request.form.get("column_number"))

        if column_number is not None:
            column_name = f"imagen{column_number}"

            if submit_value == "Animales":
                value = "Animales"
            elif submit_value == "Seres humanos":
                value = "Seres humanos"
            elif submit_value == "Plantas":
                value = "Plantas"
            elif submit_value == "Órganos del cuerpo":
                value = "Órganos del cuerpo"

            query = "UPDATE patients SET {} = :value WHERE id = :patient_id;".format(column_name)
            db.execute(query, value=value, patient_id=patient_id)

        # Renderizar nuevamente la plantilla test.html con el mismo patient_id
        return render_template("test.html", patient_id=patient_id)

    elif request.method == "GET":
        patient_id = int(request.args.get("patient_id"))
        return render_template("test.html", patient_id=patient_id)


@app.route('/resultado', methods=['POST'])
def obtener_resultado():
    global resultado_global  # Accede a la variable global

    resultado = request.json['resultado']
    print('Resultado recibido:', resultado)

    resultado_global = resultado  # Almacena el resultado en la variable global

    return 'OK'

@app.route('/result', methods=['GET'])
def mostrar_resultado():
    resultado = request.args.get('resultado')
    return render_template('result.html', resultado=resultado)


@app.route("/history", methods=["GET", "POST"])
def history():
    if request.method == "POST":
        password = request.form.get("password")

        # Verificar si la contraseña ingresada es correcta
        if password == PASSWORD:
            # La contraseña es correcta, mostrar la página de historial
            patients = db.execute("SELECT * FROM patients")
            return render_template("history.html", patients=patients)
        else:
            # La contraseña es incorrecta, mostrar un mensaje de error
            flash("Contraseña incorrecta", "error")
            return redirect(url_for("index"))
    else:
        # Método GET, mostrar formulario para ingresar la contraseña
        return render_template("password_form.html")


if __name__ == "__main__":
    app.run(debug=True)
