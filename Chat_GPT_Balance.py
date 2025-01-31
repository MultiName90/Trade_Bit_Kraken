import ccxt

# Cargar API Key desde archivo
def load_api_keys():
    with open("kraken.key", "r") as file:
        lines = file.readlines()
        return lines[0].strip(), lines[1].strip()

api_key, api_secret = load_api_keys()

# Conectar a Kraken DEMO (Si estás usando una cuenta real, quita 'urls')
kraken = ccxt.kraken({
    'apiKey': api_key,
    'secret': api_secret
})

# Consultar balance
def get_balance():
    try:
        balance = kraken.fetch_balance()
        print("Respuesta Completa de Kraken:", balance)  # Agregar para depurar

        # Verificar si la respuesta contiene el campo 'total'
        if isinstance(balance, dict) and 'total' in balance:
            return balance['total']
        else:
            return {"error": "No se encontró el balance en la respuesta."}

    except Exception as e:
        return {"error": str(e)}

# Ejecutar consulta
balance = get_balance()
print("Balance:", balance)
