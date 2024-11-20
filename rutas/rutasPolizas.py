from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoPolizas
from modelos.entidades.PolizaInmueble import PolizaInmueble
from modelos.entidades.PolizaInmuebleEscolar import PolizaInmuebleEscolar

repo_polizas = obtenerRepoPolizas()

bp_polizas = Blueprint("bp_polizas", __name__)

@bp_polizas.route("/polizas", methods=["GET"])
def listar_polizas():
    lista_dicc = []
    for poliza in repo_polizas.obtenerTodas():
            lista_dicc.append(poliza.toDiccionario())
    return jsonify(lista_dicc), 200

@bp_polizas.route("/polizas", methods=["POST"])
def agregar_poliza():
        if request.is_json:
            diccDatos = request.get_json()
            if "numero" in diccDatos and "incendio" in diccDatos and "explosion" in diccDatos and "robo" in diccDatos:
                    if 'cantPersonas' in diccDatos and 'montoEquipamiento' in diccDatos and 'montoMobiliario' in diccDatos and 'montoPersona' in diccDatos:
                        poliza_creada = PolizaInmuebleEscolar.fromDiccionario(diccDatos)
                    else:
                        poliza_creada = PolizaInmueble.fromDiccionario(diccDatos)

                    if repo_polizas.existePolizaPorNumero(poliza_creada.obtenerNumero()):
                        respuesta = {"error": "Ya existe poliza con ese numero"}
                        codigoRespuesta = 400
                    else:
                        repo_polizas.agregarPoliza(poliza_creada)
                        respuesta = {"mensaje": "Poliza agregada correctamente"}
                        codigoRespuesta = 201
            else:
                  respuesta = {"error": "Faltan datos obligatorios"}
                  codigoRespuesta = 400
        else:
              respuesta = {"error": "Formato de datos incorrecto"}
              codigoRespuesta = 400
        return jsonify(respuesta), codigoRespuesta

@bp_polizas.route("/polizas/<int:numero>", methods=["GET"])
def obtener_poliza_por_numero(numero):
      poliza = repo_polizas.obtenerPolizaPorNumero(numero)
      if poliza:
            return jsonify(poliza.toDiccionario()), 200
      else:
            return jsonify({"error": "No se encontró la poliza con ese numero"}), 404