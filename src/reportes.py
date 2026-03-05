<<<<<<< HEAD
# src/reportes.py
=======
>>>>>>> 4226ac764d6c8aa9676dce9c105513f09f355adb
from .portafolio import Portafolio


class ReportadorFinanciero:
    """
<<<<<<< HEAD
    Responsable únicamente de generar reportes.
    No guarda estado ni datos (SRP).
=======
    Responsable únicamente de generar reportes financieros.
    Aplica el principio SRP (Single Responsibility Principle).
>>>>>>> 4226ac764d6c8aa9676dce9c105513f09f355adb
    """

    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        if not isinstance(portafolio, Portafolio):
            raise TypeError("Se esperaba un objeto Portafolio.")

        print("📊 RESUMEN DEL PORTAFOLIO")
        print("-" * 40)

<<<<<<< HEAD
        total = 0.0
        for posicion in portafolio.posiciones:
            valor = posicion.calcular_valor_actual(posicion.precio_entrada)
            total += valor
            print(
                f"{posicion.instrumento.ticker} | "
                f"{posicion.instrumento.tipo} | "
                f"Cantidad: {posicion.cantidad} | "
=======
        if not portafolio.posiciones:
            print("El portafolio no tiene posiciones.")
            return

        total = 0.0

        for posicion in portafolio.posiciones:
            instrumento = posicion.instrumento
            valor = posicion.calcular_valor_actual(posicion.precio_entrada)

            total += valor

            print(
                f"Ticker: {instrumento.ticker} | "
                f"Tipo: {instrumento.tipo} | "
                f"Sector: {instrumento.sector} | "
                f"Cantidad: {posicion.cantidad} | "
                f"Precio Entrada: {posicion.precio_entrada} | "
>>>>>>> 4226ac764d6c8aa9676dce9c105513f09f355adb
                f"Valor: {valor}"
            )

        print("-" * 40)
<<<<<<< HEAD
        print(f"Valor total del portafolio: {total}")



=======
        print(f"Valor total del portafolio: {total}")
>>>>>>> 4226ac764d6c8aa9676dce9c105513f09f355adb
