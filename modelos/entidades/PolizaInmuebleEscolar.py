from modelos.entidades.PolizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float, cantPersonas: int, montoEquipamiento: float, montoMobiliario: float, montoPersona: float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona

    @classmethod
    def fromDiccionario(cls, dic: dict) -> 'PolizaInmuebleEscolar':
        return cls(
            dic['numero'],
            dic['incendio'],
            dic['explosion'],
            dic['robo'],
            dic['cantPersonas'],
            dic['montoEquipamiento'],
            dic['montoMobiliario'],
            dic['montoPersona']
        )
    
    def obtenerCantPersonas(self):
        return self.__cantPersonas
    
    def obtenerMontoEquipamiento(self):
        return self.__montoEquipamiento
    
    def obtenerMontoMobiliario(self):
        return self.__montoMobiliario
    
    def obtenerMontoPersona(self):
        return self.__montoPersona
    
    def establecerCantPersonas(self, cantPersonas):
        self.__cantPersonas = cantPersonas

    def establecerMontoEquipamiento(self, montoEquipamiento):
        self.__montoEquipamiento = montoEquipamiento

    def establecerMontoMobiliario(self, montoMobiliario):
        self.__montoMobiliario = montoMobiliario

    def establecerMontoPersona(self, montoPersona):
        self.__montoPersona = montoPersona

    
    def valorMensualPoliza(self) -> float:
        return (self.obtenerPorcentajeIncendio() * 0.01) + (self.obtenerPorcentajeExplosion() * 0.01) + (self.obtenerPorcentajeRobo() * 0.02) + (self.__montoEquipamiento * 0.01) + (self.__montoMobiliario * 0.01) + (self.__montoPersona * self.__cantPersonas * 0.01)
    
    def toString(self):
        return super().toString() + f"Cantidad de personas: {self.__cantPersonas}, MontoEquipamiento: {self.__montoEquipamiento}, MontoMobiliario: {self.__montoMobiliario}, MontoPersona: {self.__montoPersona}"

    def toDiccionario(self):
        return {
            'numero': self.obtenerNumero(),
            'incendio': self.obtenerPorcentajeIncendio(),
            'explosion': self.obtenerPorcentajeExplosion(),
            'robo': self.obtenerPorcentajeRobo(),
            'cantPersonas': self.__cantPersonas,
            'montoEquipamiento': self.__montoEquipamiento,
            'montoMobiliario': self.__montoMobiliario,
            'montoPersona': self.__montoPersona
        }