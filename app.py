from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', title="Inicio")

@app.route('/animales')
def animales():
    return render_template('animales.html', title="Animales Exóticos")

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html', title="Vehículos Antiguos")

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', title="Las Maravillas del Mundo")

@app.route("/registrando", methods=("GET", "POST"))
def registrame():
    error = None
    if request.method == "POST":
        nombreCompleto = request.form["nombreCompleto"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPassword = request.form["confirmPassword"]
        fechaNacimiento = request.form["fechaNacimiento"]
        genero = request.form["genero"]

        if password != confirmPassword:
            error = "Las contraseñas no coinciden."
        else:
            return render_template("registro_exitoso.html", nombre=nombreCompleto)

    return render_template("registrando.html", error=error, title="Registro")
    
@app.route('/acerca')
def acerca():
    return render_template('acerca.html', title="Acerca de...")

if __name__ == '__main__':
    app.run(debug=True)
