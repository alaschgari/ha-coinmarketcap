"""Sensor platform for CoinMarketCap integration."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SENSOR_TYPES, CONF_SHOW_SENSORS, DEFAULT_SENSORS

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the CoinMarketCap sensors."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    symbols = coordinator.symbols.split(',')
    # Get enabled sensors from options or fallback to default
    enabled_sensors = entry.options.get(CONF_SHOW_SENSORS, entry.data.get(CONF_SHOW_SENSORS, DEFAULT_SENSORS))
    
    entities = []
    for symbol in symbols:
        for sensor_type in enabled_sensors:
            if sensor_type in SENSOR_TYPES:
                entities.append(CoinMarketCapSensor(coordinator, symbol, sensor_type))
        
    async_add_entities(entities)

class CoinMarketCapSensor(CoordinatorEntity, SensorEntity):
    """Representation of a CoinMarketCap sensor."""

    def __init__(self, coordinator, symbol, sensor_type):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._symbol = symbol.upper()
        self._sensor_type = sensor_type
        self._sensor_info = SENSOR_TYPES[sensor_type]
        
        self._attr_name = f"{self._symbol} {self._sensor_info['name']}"
        self._attr_unique_id = f"{DOMAIN}_{self._symbol}_{sensor_type}"
        self._entry_id = coordinator.config_entry.entry_id
        
        # Set icon if defined
        if "icon" in self._sensor_info:
            self._attr_icon = self._sensor_info["icon"]

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information about this entity."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry_id)},
            name="CoinMarketCap",
            manufacturer="CoinMarketCap",
            entry_type="service",
        )

    @property
    def state(self):
        """Return the state of the sensor."""
        data = self.coordinator.data.get(self._symbol)
        if data:
            # Navigate schema: data['symbol'] -> [path]
            # e.g. ['quote', 'USD', 'price']
            value = data
            for key in self._sensor_info["json_path"]:
                value = value.get(key)
                if value is None:
                    return None
            
            # Formatting
            if isinstance(value, (int, float)):
                # Apply rounding to prices, percentages, and market cap/volume if it's a currency
                # We simply apply to everything that is a number for consistency with the 'decimals' setting
                # or strictly generally for price/% as requested.
                # Let's apply it generally to floats to keep it clean.
                return round(value, self.coordinator.decimals)
            return value
            
        return None

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._sensor_info.get("unit")

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        # Attributes are now individual sensors, so we reduce this to standard attributes
        # or we could keep providing all raw data? 
        # Better: Provide only last_updated if available
        data = self.coordinator.data.get(self._symbol)
        if data:
            quote = data.get('quote', {}).get('USD', {})
            return {
                "last_updated": quote.get('last_updated'),
                "api_id": data.get('id')
            }
        return None
