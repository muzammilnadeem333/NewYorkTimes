# NYTimesScraper

NYTimesScraper is a Python-based web scraper that uses Selenium to extract data from the New York Times website. The scraper searches for a given keyword, applies various filters, and retrieves relevant articles along with their publication dates and image URLs. The data is logged, displayed in the console, and saved to a JSON file. The scraper can run in headless mode functionality is added for headless mode.

## Features

- Search for articles based on a keyword.
- Apply date, section, and type filters to refine search results.
- Load all available search results by clicking the "Show More" button.
- Extract article titles, publication dates, and image URLs.
- Log all actions and errors for debugging and monitoring.
- Save the scraped data to a JSON file.
- Run Selenium in headless mode for a non-GUI environment.

## Requirements

- Python 3.7+
- Selenium
- ChromeDriver

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/NYTimesScraper.git
    cd NYTimesScraper
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download ChromeDriver:**

    - Download the version of ChromeDriver that matches your installed version of Chrome from [here](https://sites.google.com/chromium.org/driver/).
    - Place the ChromeDriver executable in a directory included in your system's PATH, or specify the path directly in the code.

## Usage

1. **Run the scraper:**

    ```bash
    python nytime_scraper.py
    ```

2. **Configure the scraper:**

    Modify the `run` method call in the `if __name__ == "__main__":` block to use your desired URL and keyword:

    ```python
    scraper.run('https://www.nytimes.com/', 'Covid Pakistan')
    ```

3. **JSON Output:**

    The scraped data will be saved to `nytimes_data.json` in the root directory.

## Logging

All actions and errors are logged to `nytimes_scraper.log` file in the root directory. This log file provides a detailed trace of the scraper's execution for debugging and monitoring purposes.

## Example

Here's an example of how to run the scraper:

```python
if __name__ == "__main__":
    scraper = NYTimesScraper()
    scraper.run('https://www.nytimes.com/', 'Covid Pakistan')
