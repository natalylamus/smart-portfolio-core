from .portafolio import Portafolio
 
#Codigo final de reportes
 
class ReportadorFinanciero:
    """
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
 
#Codigo final de reportes