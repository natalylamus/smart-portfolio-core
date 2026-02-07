
from dataclasses import dataclass


@dataclass(frozen=True)
class Instrumento:
    ticker: str
    tipo: str
    sector: str


class Posicion:
    def __init__(self, instrumento: Instrumento, cantidad: float, precio_entrada: float) -> None:
        if not isinstance(instrumento, Instrumento):
            raise TypeError("instrumento debe ser una instancia de Instrumento.")

        self.instrumento = instrumento
        self._cantidad: float = 0.0  
        self.cantidad = float(cantidad)  
        self.precio_entrada = float(precio_entrada)

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("La cantidad NO puede ser negativa.")
        self._cantidad = value

    def calcular_valor_actual(self, precio_mercado: float) -> float:
        return self.cantidad * float(precio_mercado)



