import requests

def precio_btc():
  try:
    resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    resp.raise_for_status()
    datos = resp.json()
    btc = datos["bpi"]["USD"]["rate_float"]
    return btc
  except requests.RequestException as e:
    raise ValueError(f"Error al consultar la API: {e}")

def main():
  try:
    n = float(input("Ingrese la cantidad de Bitcoins: "))
    btc = precio_btc()
    total = n * btc
    print(f"El costo actual de {n:,.4f} Bitcoins es: ${total:,.4f}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
