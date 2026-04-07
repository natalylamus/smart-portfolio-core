# tests/conftest.py
import pytest
from src.modelos import Instrumento, Posicion
from src.portafolio import Portafolio


@pytest.fixture
def instrumento_test():
    return Instrumento(ticker="TSLA", tipo="Accion", sector="Tecnologia")


@pytest.fixture
def portafolio_vacio():
    return Portafolio()