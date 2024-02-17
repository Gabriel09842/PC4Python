import requests

def obtener_precio_bitcoin():
  try:
    respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respuesta.raise_for_status()
    datos = respuesta.json()
    precio_bitcoin = datos["bpi"]["USD"]["rate_float"]
    return precio_bitcoin
  except requests.RequestException as e:
    raise ValueError(f"Error al consultar la API: {e}")

def main():
  try:
    n = float(input("Ingrese la cantidad de Bitcoins: "))
    precio_bitcoin = obtener_precio_bitcoin()
    costo_total = n * precio_bitcoin
    print(f"El costo actual de {n:,.4f} Bitcoins es: ${costo_total:,.4f}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
