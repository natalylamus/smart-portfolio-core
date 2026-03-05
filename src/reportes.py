from .portafolio import Portafolio


class ReportadorFinanciero:
    """
    Responsable únicamente de generar reportes financieros.
    Aplica el principio SRP (Single Responsibility Principle).
    """

    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        if not isinstance(portafolio, Portafolio):
            raise TypeError("Se esperaba un objeto Portafolio.")

        print("📊 RESUMEN DEL PORTAFOLIO")
        print("-" * 40)

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
                f"Valor: {valor}"
            )

        print("-" * 40)
        print(f"Valor total del portafolio: {total}")