from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def test_scores_service(url):
    try:
        driver = webdriver.Chrome()

        driver.get(url)

        score_element = driver.find_element(By.ID, 'score')

        score = int(score_element.text)

        if 1 <= score <= 1000:
            result = True
        else:
            result = False

    except Exception as e:
        print(f"An error occurred: {e}")
        result = False

    finally:
        # Close the browser
        driver.quit()

    return result


def main_function(url):
    test_result = test_scores_service(url)

    if test_result:
        return 0
    else:
        return -1


if __name__ == "__main__":
    url = "http://localhost:8777"
    exit_code = main_function(url)
    os._exit(exit_code)
