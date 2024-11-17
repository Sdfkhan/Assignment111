from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def find_total_articles():
    # Set up the WebDriver
    service_obj = Service(r"C:\Drivers\chromedriver-win32\chromedriver.exe")
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service_obj, options=options)

    # Navigate to the Wikipedia page
    url = "https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table"
    driver.get(url)

    # Locate all language elements (links)
    language_elements = driver.find_elements(By.XPATH, "//a[contains(@title, 'w:')]")
    languages = [element.text for element in language_elements]  # Extract language names

    # Locate all <b> tag elements for article counts
    value_elements = driver.find_elements(By.TAG_NAME, "b")
    values = [v.text.replace(",", "").strip() for v in value_elements]  # Extract and clean article counts

    # Combine languages with their corresponding article counts
    language_values = {}
    for i in range(min(len(languages), len(values))):
        language_values[languages[i]] = int(values[i])

    # Calculate the total for English and German
    selected_languages = ["English", "German"]
    total_articles = sum(language_values[lang] for lang in selected_languages if lang in language_values)

    # Close the browser
    driver.quit()

    return total_articles


# Example usage
total = find_total_articles()
print(f"Total articles for English and German: {total}")
