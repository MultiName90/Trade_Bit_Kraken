import krakenex

# Configurar API Key de Kraken
kraken = krakenex.API()
kraken.load_key('kraken.key')
print(kraken.query_private('Balance'))