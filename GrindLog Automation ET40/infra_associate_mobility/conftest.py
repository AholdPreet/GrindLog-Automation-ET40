"""
conftest.py
-----------
Single place to update credentials, device info, and connection setup.
Pytest auto-loads this file — the `driver` fixture and `tap` helper are
available to every test file in this folder without any import needed for
the fixture (just add `driver` as a parameter to your test/fixture).
Import `tap` explicitly:  from conftest import tap
"""

import urllib3
import requests
import pytest

from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from config.properties_load import (
    APPIUM_HUB_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    TENANT_ID,
    DEVICE_UDID,
    DEVICE_NAME,
    APPIUM_PLATFORM,
    APPIUM_AUTOMATION_NAME,
    APPIUM_NO_RESET,
    APPIUM_NEW_COMMAND_TIMEOUT,
    APP_PACKAGE,
    APP_ACTIVITY,
)

DESIRED_CAPS = {
    "platformName":      APPIUM_PLATFORM,
    "automationName":    APPIUM_AUTOMATION_NAME,
    "udid":              DEVICE_UDID,
    "appPackage":        APP_PACKAGE,
    "appActivity":       APP_ACTIVITY,
    "noReset":           APPIUM_NO_RESET,
    "newCommandTimeout": APPIUM_NEW_COMMAND_TIMEOUT,
    # UFT Digital Lab auth — exact names from the portal "For Appium capability" dialog
    "oauthClientId":     CLIENT_ID,
    "oauthClientSecret": CLIENT_SECRET,
    "tenantId":          TENANT_ID,
}


class SslBypassConnection(RemoteConnection):

    def _get_connection_manager(self):
        return urllib3.PoolManager(
            timeout=self.get_timeout(),
            cert_reqs="CERT_NONE",
            assert_hostname=False,
        )


class UftDriver(webdriver.Remote):
   
    def start_session(self, capabilities: dict) -> None:
        print("\n[session] Connecting -> " + APPIUM_HUB_URL)
        resp = requests.post(
            APPIUM_HUB_URL + "/session",
            json={"desiredCapabilities": DESIRED_CAPS},
            verify=False,
            timeout=120,
        )
        if not resp.ok:
            raise RuntimeError(
                "Session creation failed " + str(resp.status_code)
                + ": " + resp.text[:400]
            )
        data = resp.json()
        self.session_id = (
            data.get("sessionId") or data.get("value", {}).get("sessionId")
        )
        self.w3c = False
        self.caps = data.get("value", {}).get("capabilities", {"platformName": "Android"})
        print("[session] Connected  session ID: " + str(self.session_id))


@pytest.fixture(scope="module")
def driver():
    """Creates a UFT Digital Lab Appium session and yields the driver.
    The session is closed automatically when the test module finishes."""
    executor = SslBypassConnection(APPIUM_HUB_URL)
    d = UftDriver(command_executor=executor, options=AppiumOptions())
    d.implicitly_wait(10)
    yield d
    d.quit()
    print("\n[session] Session closed.")


