from .portafolio import Portafolio


class ReportadorFinanciero:
    """
    Clase responsable únicamente de generar reportes.
    Aplica el principio SRP (Single Responsibility Principle):
    no guarda estado ni modifica datos del dominio.
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
        

