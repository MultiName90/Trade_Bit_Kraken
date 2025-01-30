import ccxt

# Cargar API Key desde archivo
def load_api_keys():
    with open("kraken.key", "r") as file:
        lines = file.readlines()
        return lines[0].strip(), lines[1].strip()

api_key, api_secret = load_api_keys()

# Conectar a Kraken Futures DEMO
kraken_demo = ccxt.kraken({
    'apiKey': api_key,
    'secret': api_secret,
    'urls': {
        'api': 'https://demo-futures.kraken.com/derivatives/api/'
    }
})

# Consultar balance
def get_balance():
    try:
        balance = kraken_demo.fetch_balance()
        return balance
    except Exception as e:
        return {"error"}

# Ejecutar consulta
balance = get_balance()
print(balance)