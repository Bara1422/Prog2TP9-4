from flask import Flask
from modelos.entidades.PolizaInmueble import PolizaInmueble
from rutas.rutasPolizas import bp_polizas

app = Flask(__name__)
app.register_blueprint(bp_polizas)

if __name__ == '__main__':
    app.run(debug=True)