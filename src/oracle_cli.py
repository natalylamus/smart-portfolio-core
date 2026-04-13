# src/oracle_cli.py
import json
import os
from .modelos import Instrumento, Posicion
from .portafolio import Portafolio
from .providers import YahooFinanceClient
from .predictor import InstrumentoPredictivo

ARCHIVO_PORTAFOLIO = "portafolio.json"


def cargar_portafolio_json() -> list:
    if os.path.exists(ARCHIVO_PORTAFOLIO):
        with open(ARCHIVO_PORTAFOLIO, "r") as f:
            return json.load(f)
    return []


def guardar_portafolio_json(datos: list) -> None:
    with open(ARCHIVO_PORTAFOLIO, "w") as f:
        json.dump(datos, f, indent=2)
    print(f"💾 Portafolio guardado en {ARCHIVO_PORTAFOLIO}")


def ejecutar_oraculo() -> None:
    print("\n" + "=" * 40)
    print("   🔮 SMART PORTFOLIO ORACLE")
    print("=" * 40)

    ticker = input("\nIngrese el Ticker (ej: AAPL, NVDA, TSLA): ").upper().strip()

    provider = YahooFinanceClient()
    instrumento = Instrumento(ticker=ticker, tipo="Acción", sector="Mercado")
    oraculo = InstrumentoPredictivo(instrumento=instrumento, provider=provider)

    try:
        precio_actual = oraculo.precio_actual()
        oraculo.entrenar_modelo()
        prediccion_7d = oraculo.predecir_precio(dias_futuros=7)
        prediccion_30d = oraculo.predecir_precio(dias_futuros=30)

        tendencia = "📈" if prediccion_7d > precio_actual else "📉"

        print(f"\n📊 {ticker}")
        print(f"   Precio actual:        ${precio_actual:.2f}")
        print(f"   Predicción  7 días:   ${prediccion_7d:.2f} {tendencia}")
        print(f"   Predicción 30 días:   ${prediccion_30d:.2f}")

        comprar = input("\n¿Deseas registrar una compra? (s/n): ").lower().strip()

        if comprar == "s":
            cantidad = float(input("Cantidad de acciones: "))
            posicion = Posicion(
                instrumento=instrumento,
                cantidad=cantidad,
                precio_entrada=precio_actual,
            )

            datos = cargar_portafolio_json()
            datos.append({
                "ticker": ticker,
                "tipo": instrumento.tipo,
                "sector": instrumento.sector,
                "cantidad": cantidad,
                "precio_entrada": precio_actual,
                "prediccion_7d": prediccion_7d,
                "prediccion_30d": prediccion_30d,
                "alerta_riesgo": posicion.alerta_riesgo,
            })
            guardar_portafolio_json(datos)

    except ConnectionError as e:
        print(f"\n❌ Error de conexión: {e}")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


if __name__ == "__main__":
    ejecutar_oraculo()