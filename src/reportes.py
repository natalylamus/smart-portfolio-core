# src/reportes.py
from .portafolio import Portafolio


class ReportadorFinanciero:
    """
    Responsable únicamente de generar reportes.
    No guarda estado ni datos (SRP).
    """

    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        if not isinstance(portafolio, Portafolio):
            raise TypeError("Se esperaba un objeto Portafolio.")

        print("📊 RESUMEN DEL PORTAFOLIO")
        print("-" * 40)

        total = 0.0
        for posicion in portafolio.posiciones:
            valor = posicion.calcular_valor_actual(posicion.precio_entrada)
            total += valor
            print(
                f"{posicion.instrumento.ticker} | "
                f"{posicion.instrumento.tipo} | "
                f"Cantidad: {posicion.cantidad} | "
                f"Valor: {valor}"
            )

        print("-" * 40)
        print(f"Valor total del portafolio: {total}")



