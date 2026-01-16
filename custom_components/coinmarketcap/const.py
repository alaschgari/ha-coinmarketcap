"""Constants for the CoinMarketCap integration."""

DOMAIN = "coinmarketcap"

CONF_API_KEY = "api_key"
CONF_SYMBOLS = "symbols"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_DECIMALS = "decimals"
CONF_SHOW_SENSORS = "show_sensors"

DEFAULT_SCAN_INTERVAL = 300  # 5 minutes
DEFAULT_DECIMALS = 2
DEFAULT_SENSORS = ["price", "percent_change_24h"]

SENSOR_TYPES = {
    "price": {
        "name": "Price",
        "json_path": ["quote", "USD", "price"],
        "unit": "$",
        "icon": "mdi:cash"
    },
    "percent_change_1h": {
        "name": "1h Change",
        "json_path": ["quote", "USD", "percent_change_1h"],
        "unit": "%",
        "icon": "mdi:chart-line-variant"
    },
    "percent_change_24h": {
        "name": "24h Change",
        "json_path": ["quote", "USD", "percent_change_24h"],
        "unit": "%",
        "icon": "mdi:chart-line"
    },
    "percent_change_7d": {
        "name": "7d Change",
        "json_path": ["quote", "USD", "percent_change_7d"],
        "unit": "%",
        "icon": "mdi:calendar-week"
    },
    "percent_change_30d": {
        "name": "30d Change",
        "json_path": ["quote", "USD", "percent_change_30d"],
        "unit": "%",
        "icon": "mdi:calendar-month"
    },
    "volume_24h": {
        "name": "Volume 24h",
        "json_path": ["quote", "USD", "volume_24h"],
        "unit": "$",
        "icon": "mdi:chart-bar"
    },
    "volume_change_24h": {
        "name": "Volume Change 24h",
        "json_path": ["quote", "USD", "volume_change_24h"],
        "unit": "%",
        "icon": "mdi:chart-bell-curve"
    },
    "market_cap": {
        "name": "Market Cap",
        "json_path": ["quote", "USD", "market_cap"],
        "unit": "$",
        "icon": "mdi:chart-pie"
    },
    "market_cap_dominance": {
        "name": "Market Cap Dominance",
        "json_path": ["quote", "USD", "market_cap_dominance"],
        "unit": "%",
        "icon": "mdi:chart-donut"
    },
    "circulating_supply": {
        "name": "Circulating Supply",
        "json_path": ["circulating_supply"],
        "unit": None,
        "icon": "mdi:coins"
    },
    "total_supply": {
        "name": "Total Supply",
        "json_path": ["total_supply"],
        "unit": None,
        "icon": "mdi:safe"
    },
    "max_supply": {
        "name": "Max Supply",
        "json_path": ["max_supply"],
        "unit": None,
        "icon": "mdi:database"
    },
    "cmc_rank": {
        "name": "Rank",
        "json_path": ["cmc_rank"],
        "unit": None,
        "icon": "mdi:trophy"
    }
}

API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
