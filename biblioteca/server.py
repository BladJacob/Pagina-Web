from flask import Flask, render_template

# LE DECIMOS A FLASK QUE LEA ARCHIVOS ESTÁTICOS DESDE 'templates'
app = Flask(__name__, static_folder='templates')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', titulo="UDL ICO", mensaje="Bienvenido a la Biblioteca Universitaria")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo="Servicios", mensaje="Conoce los servicios que ofrecemos.")

@app.route('/contactos')
def contactos():
    return render_template('contacto.html', titulo="Contactos", mensaje="Medios para comunicarte con nosotros.")

@app.route('/productos')
def productos():
    return render_template('catalogo.html', titulo="Productos", mensaje="Explora nuestro catálogo.")

if __name__ == '__main__':
    app.run(debug=True)