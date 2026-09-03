class SystemInformationLocators:

    SYSTEM_INFO_BUTTON_LOCATOR = '//android.view.View[@content-desc="System Info"]'

    SYSTEM_INFO_TITLE_LOCATOR = '//android.widget.TextView[@text="System Information"]'
   
    CONNECTION_STATUS_LABEL_LOCATOR = '//android.widget.TextView[@text="Connection Status"]'

    CONNECTION_STATUS_VALUE_LOCATOR = '//android.widget.TextView[@text="Connection Status"]/following-sibling::android.widget.TextView[1]'

    NETWORK_NAME_LABEL_LOCATOR = '//android.widget.TextView[@text="Network Name"]'

    NETWORK_NAME_VALUE_LOCATOR = '//android.widget.ScrollView/android.view.View[2]/android.widget.TextView[4]'

    DEVICE_MAC_LABEL_LOCATOR = '//android.widget.TextView[@text="Device Mac Address"]'

    DEVICE_MAC_VALUE_LOCATOR = '//android.widget.TextView[@text="Device Mac Address"]/following-sibling::android.widget.TextView[1]'

    SIGNAL_LABEL_LOCATOR = '//android.widget.TextView[@text="Signal (RSSI)"]'

    SIGNAL_VALUE_LOCATOR = '//android.widget.TextView[@text="Signal (RSSI)"]/following-sibling::android.widget.TextView[1]'

    DEVICE_IP_ADDRESS_LABEL_LOCATOR = '//android.widget.TextView[@text="Device iP Address"]'

    DEVICE_IP_ADDRESS_VALUE_LOCATOR = '//android.widget.TextView[@text="Device iP Address"]/following-sibling::android.widget.TextView[1]'

    DEVICE_SERIAL_LABEL_LOCATOR = '//android.widget.TextView[@text="Device Serial Number"]'

    DEVICE_SERIAL_VALUE_LOCATOR = '//android.widget.TextView[@text="Device Serial Number"]/following-sibling::android.widget.TextView[1]'

    ANDROID_VERSION_LABEL_LOCATOR = '//android.widget.TextView[@text="Android Version"]'

    ANDROID_VERSION_VALUE_LOCATOR = '//android.widget.TextView[@text="Android Version"]/following-sibling::android.widget.TextView[1]'

    LAUNCHER_VERSION_LABEL_LOCATOR = '//android.widget.TextView[@text="Launcher Version"]'

    LAUNCHER_VERSION_VALUE_LOCATOR = '//android.widget.TextView[contains(@text,"v.")]'

    REFRESH_LAUNCHER_LOCATOR = '//android.widget.TextView[@text="Refresh Launcher Apps"]'
    
    LOGOUT_Btn_LOCATOR = '//android.view.View[@content-desc="Logout"]'