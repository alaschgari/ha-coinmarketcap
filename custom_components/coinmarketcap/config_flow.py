"""Config flow for CoinMarketCap integration."""
import logging
import voluptuous as vol
import aiohttp

from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_API_KEY, CONF_SYMBOLS, API_URL

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_API_KEY): str,
    vol.Required(CONF_SYMBOLS, default="BTC,ETH"): str,
})

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CoinMarketCap."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validate the API key
            valid = await self._test_api_key(user_input[CONF_API_KEY])
            if valid:
                return self.async_create_entry(title="CoinMarketCap", data=user_input)
            else:
                errors["base"] = "invalid_auth"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

    async def _test_api_key(self, api_key):
        """Test if the API key is valid."""
        headers = {
            'X-CMC_PRO_API_KEY': api_key,
            'Accepts': 'application/json',
        }
        params = {
            'symbol': 'BTC',
            'convert': 'USD'
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(API_URL, headers=headers, params=params) as response:
                    return response.status == 200
            except Exception:
                return False
