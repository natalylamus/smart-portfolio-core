# src/providers.py
from abc import ABC, abstractmethod
from functools import lru_cache
import pandas as pd


class MarketDataProvider(ABC):
    """Interfaz abstracta para cualquier proveedor de datos de mercado."""

    @abstractmethod
    def obtener_precio_actual(self, ticker: str) -> float:
        pass

    @abstractmethod
    def obtener_historia(self, ticker: str) -> pd.DataFrame:
        pass


class YahooFinanceClient(MarketDataProvider):
    """Proveedor real que consulta Yahoo Finance."""

    @lru_cache(maxsize=32)
    def obtener_precio_actual(self, ticker: str) -> float:
        try:
            import yfinance as yf
            t = yf.Ticker(ticker)
            precio = t.fast_info["last_price"]
            return float(precio)
        except Exception as e:
            raise ConnectionError(
                f"Error consultando Yahoo Finance para {ticker}: {e}"
            )

    def obtener_historia(self, ticker: str) -> pd.DataFrame:
        try:
            import yfinance as yf
            t = yf.Ticker(ticker)
            df = t.history(period="1y")
            if df.empty:
                raise ValueError(f"No se encontró historial para {ticker}")
            return df
        except Exception as e:
            raise ConnectionError(
                f"Error obteniendo historial de {ticker}: {e}"
            )


class MockDataProvider(MarketDataProvider):
    """Proveedor falso para tests. No requiere internet."""

    def obtener_precio_actual(self, ticker: str) -> float:
        precios = {"AAPL": 150.0, "TSLA": 200.0, "NVDA": 420.0}
        return precios.get(ticker, 100.0)

    def obtener_historia(self, ticker: str) -> pd.DataFrame:
        import numpy as np
        precios = 100 + np.arange(252) * 0.5
        index = pd.date_range(end=pd.Timestamp.today(), periods=252, freq="B")
        return pd.DataFrame({"Close": precios}, index=index)