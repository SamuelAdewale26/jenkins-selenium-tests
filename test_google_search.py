import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleSearch:
    
    @pytest.fixture
    def driver(self):
        """Setup Chrome driver for testing"""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in background
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()
    
    def test_google_homepage_loads(self, driver):
        """Test that Google homepage loads successfully"""
        driver.get("https://www.google.com")
        assert "Google" in driver.title
        assert driver.find_element(By.NAME, "q").is_displayed()
    
    def test_google_search(self, driver):
        """Test that Google search works"""
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium testing")
        search_box.submit()
        
        # Wait for results
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "g"))
        )
        
        assert len(results) > 0
    
    def test_page_title_changes(self, driver):
        """Test that page title reflects search"""
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Jenkins automation")
        search_box.submit()
        
        WebDriverWait(driver, 10).until(
            EC.title_contains("Jenkins automation")
        )
        
        assert "Jenkins automation" in driver.title
