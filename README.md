# CoinMarketCap Home Assistant Integration

This custom integration for Home Assistant allows you to track cryptocurrency prices and market data using the CoinMarketCap API.

## Features
- Real-time price tracking in USD.
- 24h percent change sensors.
- Additional attributes like Market Cap and 24h Volume.
- Easy configuration via Home Assistant UI.

## Installation via HACS
1. Open HACS in your Home Assistant instance.
2. Click on "Integrations".
3. Click the three dots in the upper right corner and select "Custom repositories".
4. Add the URL of this repository and select "Integration" as the category.
5. Click "Add" and then install the "CoinMarketCap" integration.
6. Restart Home Assistant.

## Configuration
1. Go to **Settings** > **Devices & Services**.
2. Click **Add Integration**.
3. Search for **CoinMarketCap**.
4. Enter your **API Key** and the **Symbols** (comma-separated, e.g., `BTC,ETH,SOL`) you want to track.
