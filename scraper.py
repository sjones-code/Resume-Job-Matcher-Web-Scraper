import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def get_job_description(url):
    driver = uc.Chrome()
    driver.get(url)
    
    try:
        wait = WebDriverWait(driver, 10)
        job_desc_elem = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.job_description.markdown_content"))
        )
        description = job_desc_elem.text
        return description
    except TimeoutException:
        print("Timed out waiting for 'div.job_description.markdown_content' element.")
        return None
    except Exception as e:
        print(f"Error scraping job description: {e}")
        return None
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.ziprecruiter.com/c/Hermeus/Job/Software-Engineer-Intern-(HMI)-Fall-2025/-in-Atlanta,GA?jid=c0a95d47b7e23c10"
    desc = get_job_description(url)
    if desc:
        print(desc[:500])
    else:
        print("Failed to get job description.")
