# src/predictor.py
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from .modelos import Instrumento
from .providers import MarketDataProvider


class InstrumentoPredictivo:
    """
    Envuelve un Instrumento del dominio y le agrega capacidades de ML.
    Aplica inyección de dependencias: el proveedor se pasa desde afuera.
    """

    def __init__(self, instrumento: Instrumento, provider: MarketDataProvider):
        if not isinstance(instrumento, Instrumento):
            raise TypeError("instrumento debe ser una instancia de Instrumento")
        self.instrumento = instrumento
        self.provider = provider
        self._historial: pd.DataFrame = pd.DataFrame()
        self._modelo = LinearRegression()
        self._entrenado = False

    def cargar_datos(self) -> None:
        """Descarga el historial de precios desde el proveedor."""
        print(f"📡 Obteniendo datos para {self.instrumento.ticker}...")
        self._historial = self.provider.obtener_historia(
            self.instrumento.ticker
        )
        print("✅ Datos cargados correctamente.")

    def entrenar_modelo(self) -> None:
        """Entrena una regresión lineal sobre el historial de precios."""
        if self._historial.empty:
            self.cargar_datos()

        df = self._historial.reset_index()
        X = df.index.values.reshape(-1, 1)
        y = df["Close"].values

        self._modelo.fit(X, y)
        self._entrenado = True
        print(f"🤖 Modelo entrenado para {self.instrumento.ticker}.")

    def predecir_precio(self, dias_futuros: int = 7) -> float:
        """Predice el precio para N días en el futuro."""
        if not self._entrenado:
            self.entrenar_modelo()

        ultimo_indice = len(self._historial)
        prediccion = self._modelo.predict([[ultimo_indice + dias_futuros]])
        return float(prediccion[0])

    def precio_actual(self) -> float:
        """Consulta el precio actual desde el proveedor."""
        return self.provider.obtener_precio_actual(self.instrumento.ticker)