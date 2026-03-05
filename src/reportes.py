<<<<<<< HEAD
=======
# src/reportes.py
>>>>>>> 54a00fdd556556c5bcfc6a3138fd2c1e58623c83
from .portafolio import Portafolio


class ReportadorFinanciero:
    """
<<<<<<< HEAD
    Clase responsable únicamente de generar reportes.
    Aplica el principio SRP (Single Responsibility Principle).
    """

    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        print("📊 RESUMEN DEL PORTAFOLIO")
        print("-" * 40)

        if not portafolio.posiciones:
            print("El portafolio no tiene posiciones.")
            return

        for posicion in portafolio.posiciones:
            instrumento = posicion.instrumento
            print(
                f"Ticker: {instrumento.ticker} | "
                f"Tipo: {instrumento.tipo} | "
                f"Sector: {instrumento.sector} | "
                f"Cantidad: {posicion.cantidad} | "
                f"Precio Entrada: {posicion.precio_entrada}"
            )

        print("-" * 40)
=======
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



>>>>>>> 54a00fdd556556c5bcfc6a3138fd2c1e58623c83
