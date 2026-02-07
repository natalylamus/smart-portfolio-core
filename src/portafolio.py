# src/portafolio.py
from __future__ import annotations

from typing import List

from .modelos import Posicion


class Portafolio:
    """
    Gestor (colección) de posiciones.
    Contiene una lista de Posicion y permite agregar nuevas posiciones.
    """

    def __init__(self) -> None:
        # Reto de tipado: lista tipada de Posicion
        self._posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        """
        Recibe un objeto Posicion y lo guarda en el portafolio.
        """
        if not isinstance(posicion, Posicion):
            raise TypeError("posicion debe ser una instancia de Posicion.")
        self._posiciones.append(posicion)

    @property
    def posiciones(self) -> List[Posicion]:
        """
        Devuelve la lista de posiciones (para consultar).
        """
        return self._posiciones


