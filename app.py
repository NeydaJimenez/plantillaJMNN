from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_segura_123" 


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

@app.route('/acerca')
def acerca():
    return render_template('acerca.html', title="Acerca de...")


@app.route("/registrando", methods=("GET", "POST"))
def registro():
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
            return redirect(url_for('registro_exitoso', nombre=nombreCompleto))

    return render_template("registrando.html", error=error, title="Registro")

@app.route('/registro_exitoso/<nombre>')
def registro_exitoso(nombre):
    return render_template('registro_exitoso.html', nombre=nombre)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario and contrasena:
            session['usuario'] = usuario
            return redirect(url_for('inicio'))
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template('login.html', title="Iniciar Sesión", error=error)


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
