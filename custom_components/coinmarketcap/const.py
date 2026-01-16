"""Constants for the CoinMarketCap integration."""

DOMAIN = "coinmarketcap"

CONF_API_KEY = "api_key"
CONF_SYMBOLS = "symbols"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_DECIMALS = "decimals"

DEFAULT_SCAN_INTERVAL = 300  # 5 minutes
DEFAULT_DECIMALS = 2

API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
