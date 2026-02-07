

from modelos import Instrumento, Posicion

print("=== CREANDO INSTRUMENTO ===")
instrumento = Instrumento(
    ticker="AAPL",
    tipo="Acción",
    sector="Tecnología"
)
print(instrumento)

print("\n=== CREANDO POSICIÓN ===")
posicion = Posicion(
    instrumento=instrumento,
    cantidad=10,
    precio_entrada=150
)
print("Cantidad inicial:", posicion.cantidad)
print("Precio de entrada:", posicion.precio_entrada)

print("\n=== CALCULAR VALOR ACTUAL ===")
precio_mercado = 180
valor_actual = posicion.calcular_valor_actual(precio_mercado)
print("Precio de mercado:", precio_mercado)
print("Valor actual:", valor_actual)

print("\n=== MODIFICAR CANTIDAD (CORRECTO) ===")
posicion.cantidad = 5
print("Nueva cantidad:", posicion.cantidad)

print("\n=== INTENTAR CANTIDAD NEGATIVA (DEBE FALLAR) ===")
try:
    posicion.cantidad = -3
except ValueError as error:
    print("Error capturado correctamente:", error)

print("\n=== PRUEBA FINALIZADA ===")
