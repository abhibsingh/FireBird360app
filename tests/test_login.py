import time
import os
import pytest
import logging
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_random_email():
    """Generate a random email address for testing."""
    random_number = random.randint(1000, 9999)
    return f"test+{random_number}@gmail.com"

def test_account_creation(driver):
    """
    Test case 1: Automate the account creation flow.
    """
    try:
        # Wait for the app to load
        time.sleep(5)

        # Step 1: Click on "Create Account" button
        logger.info("Locating 'Create Account' button...")
        create_account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Create Account"]'))
        )
        create_account_button.click()
        logger.info("Navigated to 'Create Account'.")

        # Step 2: Enter first name
        logger.info("Locating first name input field...")
        first_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]"))
        )
        first_name_field.click()
        first_name_field.send_keys("John")
        logger.info("First name entered.")

        # Continue with all the other steps from your original test...
        # [Previous test steps remain the same]

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_navigate_to_manager(driver):
    """
    Test case 2: Navigate to the Manager section.
    """
    try: 
        # Step 8: Click on "Manager" icon
        logger.info("Clicking on the 'Manager' icon...")
        manager_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[2]"))
        )
        manager_icon.click()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_continue_manager_flow(driver):
    """
    Test case 3: Continue through the initial Manager flow.
    """
    try:
        # Step 9: Click "Continue" button
        logger.info("Clicking on 'Continue' button...")
        continue_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Continue']"))
        )
        continue_button.click()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_search_artist(driver):
    """
    Test case 4: Search for an artist in the Manager section.
    """
    try:
        # Step 10: Search for "Taylor"
        logger.info("Searching for artist 'Taylor'...")
        search_artist_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Search for artist name']"))
        )
        search_artist_button.click()

        # [Rest of the search artist test steps remain the same]

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_verify_app_content(driver):
    """
    Test case 5: Verify app content after navigating from Manager.
    """
    try:
        time.sleep(10)

        #Step 9: Scroll up and down
        logger.info("Scrolling up and down to verify Spotify element...")
        touch_action = TouchAction(driver)
        touch_action.press(x=500, y=1000).move_to(x=500, y=200).release().perform()  # Scroll down
        time.sleep(1)
        touch_action.press(x=500, y=200).move_to(x=500, y=1000).release().perform()  # Scroll up

        # Step 10: Check for Spotify element
        logger.info("Verifying presence of Spotify element...")
        element = driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='7 days']")
        assert element.is_displayed(), "Element containing 'Followers' not found!"
        if element:
            logger.info("Spotify element found!")
        else:
            logger.error("Spotify element NOT found!")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

def test_add_artist_and_validate_highlights(driver):
    try:
        # Step 0: Relaunch the app
        logger.info("Relaunching the app for this test case.")
        driver.close_app()  # Close the app
        driver.launch_app()  # Relaunch the app
        time.sleep(20)  # Wait for 20 seconds before starting execution

        # [Rest of the add artist test steps remain the same]

    except Exception as e:
        logger.error(f"An error occurred during the test: {e}")
        raise

def test_switch_artist(driver):
    """
    Test case: Switch from one artist to another in the dropdown menu.
    """
    try:
        # Step 1: Click on the dropdown menu for the artist "Shreya Ghoshal"
        logger.info("Clicking on 'Shreya Ghoshal' artist dropdown menu...")
        shreya_ghoshal_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[starts-with(@content-desc, 'Shreya Ghoshal')]/android.widget.ImageView[1]"))
        )
        shreya_ghoshal_dropdown.click()
        logger.info("Clicked on 'Shreya Ghoshal' dropdown menu.")

    except Exception as e:
        logger.error(f"An error occurred during the artist switch test: {str(e)}")
        raise 