# tests/test_models.py
import pytest
from src.modelos import Instrumento, Posicion
from src.portafolio import Portafolio, PosicionNoExisteError


# ─────────────────────────────────────────────
# Tests de Instrumento
# ─────────────────────────────────────────────

def test_instrumento_se_crea_correctamente(instrumento_test):
    assert instrumento_test.ticker == "TSLA"
    assert instrumento_test.tipo == "Accion"
    assert instrumento_test.sector == "Tecnologia"


def test_instrumento_es_inmutable(instrumento_test):
    with pytest.raises(Exception):
        instrumento_test.ticker = "AAPL"


# ─────────────────────────────────────────────
# Tests de Posicion
# ─────────────────────────────────────────────

def test_posicion_se_crea_correctamente(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=10, precio_entrada=150)
    assert posicion.cantidad == 10
    assert posicion.precio_entrada == 150


def test_posicion_cantidad_negativa_lanza_error(instrumento_test):
    with pytest.raises(ValueError):
        Posicion(instrumento=instrumento_test, cantidad=-5, precio_entrada=100)


def test_posicion_cambiar_cantidad_negativa_lanza_error(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=10, precio_entrada=100)
    with pytest.raises(ValueError):
        posicion.cantidad = -3


def test_posicion_instrumento_invalido_lanza_error():
    with pytest.raises(TypeError):
        Posicion(instrumento="no_es_instrumento", cantidad=5, precio_entrada=100)


def test_calcular_valor_actual(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=10, precio_entrada=150)
    assert posicion.calcular_valor_actual(200) == pytest.approx(2000)


# ─────────────────────────────────────────────
# Tests parametrizados — PnL (Ganancia/Pérdida)
# ─────────────────────────────────────────────

@pytest.mark.parametrize(
    "precio_entrada, precio_actual, cantidad, esperado",
    [
        (100, 150, 10, 500),   # ganancia
        (200, 180, 5, -100),   # pérdida
        (50,  50,  7,  0),     # sin cambio
    ],
)
def test_calculo_pnl(precio_entrada, precio_actual, cantidad, esperado, instrumento_test):
    posicion = Posicion(
        instrumento=instrumento_test,
        cantidad=cantidad,
        precio_entrada=precio_entrada,
    )
    pnl = posicion.calcular_ganancia_no_realizada(precio_actual=precio_actual)
    assert pnl == pytest.approx(esperado)


# ─────────────────────────────────────────────
# Tests de Portafolio
# ─────────────────────────────────────────────

def test_portafolio_vacio_no_tiene_posiciones(portafolio_vacio):
    assert len(portafolio_vacio.posiciones) == 0


def test_agregar_posicion(portafolio_vacio, instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=100)
    portafolio_vacio.agregar_posicion(posicion)
    assert len(portafolio_vacio.posiciones) == 1


def test_agregar_posicion_invalida_lanza_error(portafolio_vacio):
    with pytest.raises(TypeError):
        portafolio_vacio.agregar_posicion("no_es_posicion")


def test_remover_activo_inexistente_lanza_error(portafolio_vacio):
    with pytest.raises(PosicionNoExisteError):
        portafolio_vacio.remover_posicion(ticker="NFLX")


def test_remover_posicion_existente(portafolio_vacio, instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=100)
    portafolio_vacio.agregar_posicion(posicion)
    portafolio_vacio.remover_posicion(ticker="TSLA")
    assert len(portafolio_vacio.posiciones) == 0

     # ─────────────────────────────────────────────
# Tests de ReportadorFinanciero
# ─────────────────────────────────────────────
from src.reportes import ReportadorFinanciero

def test_imprimir_resumen_portafolio_vacio(portafolio_vacio, capsys):
    reportador = ReportadorFinanciero()
    reportador.imprimir_resumen(portafolio_vacio)
    captured = capsys.readouterr()
    assert "El portafolio no tiene posiciones" in captured.out

def test_imprimir_resumen_con_posiciones(portafolio_vacio, instrumento_test, capsys):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=100)
    portafolio_vacio.agregar_posicion(posicion)
    reportador = ReportadorFinanciero()
    reportador.imprimir_resumen(portafolio_vacio)
    captured = capsys.readouterr()
    assert "TSLA" in captured.out
    assert "RESUMEN DEL PORTAFOLIO" in captured.out