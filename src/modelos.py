# src/modelos.py
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

    def calcular_ganancia_no_realizada(self, precio_actual: float) -> float:
        """Retorna la ganancia (o pérdida) no realizada de la posición."""
        return (float(precio_actual) - self.precio_entrada) * self.cantidad
    
    ## con Ajuste modelos punto 2 

    ## Se realiza ajuste 

    @property
    def alerta_riesgo(self) -> bool:
        """Retorna True si la pérdida supera el 10% del valor de entrada."""
        valor_entrada = self.precio_entrada * self.cantidad
        if valor_entrada == 0:
            return False
        perdida = self.calcular_ganancia_no_realizada(self.precio_entrada)
        return perdida < -(valor_entrada * 0.10)

