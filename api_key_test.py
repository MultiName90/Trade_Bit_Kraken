import ccxt

# Cargar credenciales desde el archivo kraken.key
def load_api_keys():
    with open("kraken.key", "r") as file:
        lines = file.readlines()
        return lines[0].strip(), lines[1].strip()

# Conectar con Kraken DEMO
api_key, api_secret = load_api_keys()
kraken = ccxt.kraken({
    'apiKey': api_key,
    'secret': api_secret
})


# Prueba de conexión con manejo de errores
def get_balance():
    try:
        balance = kraken.fetch_balance()

        # 🔍 Depuración: Imprimir respuesta cruda
        print("🔍 Respuesta cruda de Kraken:", balance)

        # Si la respuesta es un string, intentar convertirla en JSON
        if isinstance(balance, str):
            import json
            try:
                balance = json.loads(balance)  # Intentar convertirlo en un diccionario
            except json.JSONDecodeError:
                return {"error": "La respuesta no es un JSON válido."}

        # Si balance es un diccionario, buscar la clave 'total'
        if isinstance(balance, dict):
            return balance.get('total', "No se encontró el balance.")

        return {"error": "Formato de respuesta inesperado."}

    except Exception as e:
        return {"error": str(e)}

# Ejecutar consulta
balance = get_balance()
print("🔹 Balance final:", balance)
