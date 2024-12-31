import os
import platform

# Default configurations
CONFIG = {
    "APK_PATH": os.getenv("APK_PATH", ""),
    "PLATFORM_VERSION": "30",
    "DEVICE_NAME": "test_avd",
    "AUTOMATION_NAME": "UiAutomator2",
    "APP_PACKAGE": "com.firebird.artist360.uat",
    "APP_ACTIVITY": "com.firebird.artist360.MainActivity"
}

def validate_config():
    """Validate required configurations"""
    if not CONFIG["APK_PATH"]:
        raise ValueError(
            "APK_PATH must be set in .env file. "
            "Please copy .env.example to .env and set your APK path."
        )
    
    if not os.path.exists(CONFIG["APK_PATH"]):
        os_type = platform.system()
        example_path = {
            "Darwin": "/Users/username/Downloads/app.apk",
            "Windows": "C:/Users/username/Downloads/app.apk",
            "Linux": "/home/username/downloads/app.apk"
        }.get(os_type, "/path/to/your/app.apk")
        
        raise FileNotFoundError(
            f"APK file not found at path: {CONFIG['APK_PATH']}\n"
            f"Please ensure the path exists and is accessible.\n"
            f"Example path for your OS: {example_path}"
        )

def get_config():
    """Get validated configuration"""
    validate_config()
    return CONFIG 