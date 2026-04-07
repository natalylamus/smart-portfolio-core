# src/portafolio.py
from __future__ import annotations
from typing import List
from .modelos import Posicion


class PosicionNoExisteError(Exception):
    """Se lanza cuando se intenta remover una posición que no existe en el portafolio."""
    pass


class Portafolio:
    def __init__(self) -> None:
        self._posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        if not isinstance(posicion, Posicion):
            raise TypeError("posicion debe ser una instancia de Posicion.")
        self._posiciones.append(posicion)

    def remover_posicion(self, ticker: str) -> None:
        """Remueve la posición con el ticker dado. Lanza PosicionNoExisteError si no existe."""
        for posicion in self._posiciones:
            if posicion.instrumento.ticker == ticker:
                self._posiciones.remove(posicion)
                return
        raise PosicionNoExisteError(
            f"No existe ninguna posición con el ticker '{ticker}' en el portafolio."
        )

    @property
    def posiciones(self) -> List[Posicion]:
        return self._posiciones