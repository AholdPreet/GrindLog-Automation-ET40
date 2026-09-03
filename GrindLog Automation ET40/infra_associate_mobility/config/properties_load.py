import configparser
from pathlib import Path


def load_properties(filename="config.properties"):

    config = configparser.ConfigParser()
    config_path = Path(__file__).parent / filename
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    config.read(config_path)
    return config


# Load configuration on import
_config = load_properties()


# Expose credentials as module-level variables for easy import
APPIUM_HUB_URL = _config.get('appium', 'hub.url')
CLIENT_ID      = _config.get('oauth', 'client.id')
CLIENT_SECRET  = _config.get('oauth', 'client.secret')
TENANT_ID      = _config.get('oauth', 'tenant.id')
DEVICE_UDID    = _config.get('device', 'udid')
DEVICE_NAME    = _config.get('device', 'name')

# Appium settings
APPIUM_PLATFORM = _config.get('appium', 'platform')
APPIUM_AUTOMATION_NAME = _config.get('appium', 'automation.name')
APPIUM_NO_RESET = _config.getboolean('appium', 'no.reset')
APPIUM_NEW_COMMAND_TIMEOUT = _config.getint('appium', 'new.command.timeout')

# App configuration (optional)
APP_PACKAGE = _config.get('app', 'package', fallback=None)
APP_ACTIVITY = _config.get('app', 'activity', fallback=None)
