import time
import json
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

# Configure logging
logging.basicConfig(filename='nytimes_scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class NYTimesScraper:
    def __init__(self):
        # Run in headless mode
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Chrome(options=chrome_options)
        self.data_ls = []

    def open_website(self, url):
        try:
            self.browser.get(url)
            time.sleep(5)
            logging.info(f"Opened website: {url}")
        except Exception as e:
            logging.error(f"Error opening website: {e}")

    def search_keyword(self, keyword):
        try:
            self.browser.find_element(By.XPATH, '//div[1]/div/button[@class="css-tkwi90 e1iflr850"]').click()
            input_keywords = self.browser.find_element(By.XPATH, '//*[@id="search-input"]/form/div/input[@class="css-1u4s13l"]')
            input_keywords.send_keys(keyword)
            self.browser.find_element(By.XPATH, '//*[@id="search-input"]/form/button[@class="css-1gudca6 e1iflr852"]').click()
            time.sleep(5)
            logging.info(f"Searched for keyword: {keyword}")
        except Exception as e:
            logging.error(f"Error during search: {e}")

    def apply_filters(self):
        try:
            self.browser.find_element(By.XPATH, './/div[@aria-label="Date Range"]/button[@data-testid="search-date-dropdown-a"]').click()
            self.browser.find_element(By.XPATH, '//div/ul/li[@class="css-guqk22"]/button[@value="All Since 1851"]').click()
            logging.info("Applied date filter: All Since 1851")
        except Exception as e:
            logging.error(f"Error applying date filter: {e}")

        try:
            self.browser.find_element(By.XPATH, '//*[@id="site-content"]//div[@data-testid="section"]/button[@class="css-4d08fs"]').click()
            self.browser.find_element(By.XPATH, '//*[@id="site-content"]//ul[@class="css-64f9ga"]/li[4]/label/span[@class="css-16eo56s"]').click()
            self.browser.find_element(By.XPATH, '//*[@id="site-content"]//ul[@class="css-64f9ga"]//li[5]/label/span[@class="css-16eo56s"]').click()
            logging.info("Applied section filters: Business and Health")
        except Exception as e:
            logging.error(f"Error applying section filter: {e}")

        try:
            self.browser.find_element(By.XPATH, '//div[@data-testid="type"]/button[@class="css-4d08fs"]').click()
            self.browser.find_element(By.XPATH, '//div/ul[@class="css-64f9ga"]/li[2]/label/span[@class="css-16eo56s"]').click()
            logging.info("Applied type filter")
        except Exception as e:
            logging.error(f"Error applying type filter: {e}")

    def load_all_results(self):
        while True:
            try:
                self.browser.find_element(By.XPATH, '//div[@class="css-vsuiox"]/button[@data-testid="search-show-more-button"]').click()
                time.sleep(2)
                logging.info("Loaded more results")
            except Exception as e:
                logging.info("No more results to load")
                break

    def scrape_data(self):
        try:
            all_data = self.browser.find_elements(By.XPATH, '//div/ol[@aria-live="polite"]/li[@class="css-1l4w6pd"]')
            for data in all_data:
                dictionary = {}
                dictionary['date_obj'] = data.find_element(By.XPATH, './/div/span[@class="css-17ubb9w"]').text
                dictionary['title'] = data.find_element(By.XPATH, './/div/a/h4[@class="css-nsjm9t"]').text
                dictionary['image_url'] = data.find_element(By.XPATH, './/div//img[@class="css-rq4mmj"]').get_attribute('src')
                self.data_ls.append(dictionary)
                logging.info(f"Scraped data - DATE: {dictionary['date_obj']} TITLE: {dictionary['title']} IMAGE URL: {dictionary['image_url']}")
        except Exception as e:
            logging.error(f"Error scraping data: {e}")

    def save_to_json(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.data_ls, f, indent=4)
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving data to JSON: {e}")

    def close_browser(self):
        self.browser.quit()
        logging.info("Browser closed")

    def run(self, url, keyword):
        self.open_website(url)
        self.search_keyword(keyword)
        self.apply_filters()
        self.load_all_results()
        self.scrape_data()
        time.sleep(10)
        self.save_to_json('nytimes_data.json')
        self.close_browser()
        logging.info(f"Scraping completed with {len(self.data_ls)} items")
        print(self.data_ls)
        print(len(self.data_ls))


if __name__ == "__main__":
    scraper = NYTimesScraper()
    scraper.run('https://www.nytimes.com/', 'Covid Pakistan')
