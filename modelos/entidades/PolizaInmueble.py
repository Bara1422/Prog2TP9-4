class PolizaInmueble:
    def __init__(self, numero:int, incendio: float, explosion: float, robo: float):
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo

    @classmethod
    def fromDiccionario(cls, dic:dict) -> 'PolizaInmueble':
        return cls(
            dic["numero"],
            dic["incendio"],
            dic["explosion"],
            dic["robo"]
        )
    
    def toDiccionario(self):
        return {
            "numero": self._numero,
            "incendio": self._incendio,
            "explosion": self._explosion,
            "robo": self._robo
        }
    
    def toString(self):
        return f"Número de póliza: {self._numero}, Porcentaje de incendio: {self._incendio}, Porcentaje de explosión: {self._explosion}, Porcentaje de robo: {self._robo}"
    
    def obtenerNumero(self):
        return self._numero
    
    def obtenerPorcentajeIncendio(self):
        return self._incendio
    
    def obtenerPorcentajeExplosion(self):
        return self._explosion
    
    def obtenerPorcentajeRobo(self):
        return self._robo
    
    def establecerPorcentajeIncendio(self, incendio:float):
        self._incendio = incendio

    def establecerPorcentajeExplosion(self, explosion:float):
        self._explosion = explosion

    def establecerPorcentajeRobo(self, robo:float):
        self._robo = robo
    
    def valorMensualPoliza(self) -> float:
        return (self._incendio * 0.02) + (self._explosion * 0.01) + (self._robo * 0.03)
    