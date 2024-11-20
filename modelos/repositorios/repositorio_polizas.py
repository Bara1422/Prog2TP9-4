from modelos.entidades.PolizaInmueble import PolizaInmueble
from modelos.entidades.PolizaInmuebleEscolar import PolizaInmuebleEscolar
import json

class RepositorioPoliza:
    __ruta_archivo = "datos/polizas.json"

    def __init__(self):
        self.__polizas = self.__cargarTodos()

    def __cargarTodos(self):
        lista_objetos = []
        lista_diccionarios = []
        try:
            with open(RepositorioPoliza.__ruta_archivo, 'r', encoding='utf-8') as archivo:
                lista_diccionarios = json.load(archivo)
        except Exception as e:
            print(f"Error al cargar las polizas de polizas.json: {e}")
        for poliza in lista_diccionarios:
            if 'cantPersonas' in poliza and 'montoEquipamiento' in poliza and 'montoMobiliario' in poliza and 'montoPersona' in poliza:
                lista_objetos.append(PolizaInmuebleEscolar.fromDiccionario(poliza))
            else:
                lista_objetos.append(PolizaInmueble.fromDiccionario(poliza))

        return lista_objetos

    def __guardarTodos(self):
        lista_dicc = []
        for poliza in self.__polizas:
            lista_dicc.append(poliza.toDiccionario())

        try:
            with open(RepositorioPoliza.__ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(lista_dicc, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar las polizas en polizas.json: {e}")

    def obtenerTodas(self) -> list[PolizaInmueble]:
        return self.__polizas
    
    def obtenerPolizaPorNumero(self, numero:int)->PolizaInmueble:
        for poliza in self.__polizas:
            if poliza.obtenerNumero() == numero:
                return poliza
        return None
    
    def existe(self, poliza:PolizaInmueble):
        if isinstance(poliza, PolizaInmueble):
            for poliza_a_buscar in self.__polizas:
                if poliza_a_buscar.obtenerNumero() == poliza.obtenerNumero():
                    return True
            return False
    
    def existePolizaPorNumero(self, numero:int)->bool:
        for poliza in self.__polizas:
            if poliza.obtenerNumero() == numero:
                return True
        return False
    
    def agregarPoliza(self, poliza:PolizaInmueble):
        if not self.existePolizaPorNumero(poliza.obtenerNumero()):
            self.__polizas.append(poliza)
            self.__guardarTodos()
        
    def eliminarPoliza(self, numero:int):
        if self.existePolizaPorNumero(numero):
            for poliza in self.__polizas:
                if poliza.obtenerNumero() == numero:
                    self.__polizas.remove(poliza)
                    self.__guardarTodos()
                    break
    
    def modificarPoliza(self, numero:int, incendio: float, explosion: float, robo: float, cantPersonas=None, montoEquipamiento=None, montoMobiliario=None, montoPersona=None):
        for poliza in self.__polizas:
            if isinstance(poliza, PolizaInmueble):
                if poliza.obtenerNumero() == numero:
                    poliza.establecerPorcentajeIncendio(incendio)
                    poliza.establecerPorcentajeExplosion(explosion)
                    poliza.establecerPorcentajeRobo(robo)
                    
                    if isinstance(poliza, PolizaInmuebleEscolar):
                        poliza.establecerCantPersonas(cantPersonas)
                        poliza.establecerMontoEquipamiento(montoEquipamiento)
                        poliza.establecerMontoMobiliario(montoMobiliario)
                        poliza.establecerMontoPersona(montoPersona)
                    self.__guardarTodos()

    