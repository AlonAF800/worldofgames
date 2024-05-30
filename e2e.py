import sys
from selenium import webdriver


def test_scores_service(url):
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in PATH
    driver.get(url)

    try:
        score_element = driver.find_element_by_id('score')
        score = int(score_element.text)
        result = 1 <= score <= 1000
    except Exception as e:
        print(f"An error occurred: {e}")
        result = False
    finally:
        driver.quit()

    return result


def main():
    url = 'http://localhost:8777'  # URL of the application
    if test_scores_service(url):
        print("Test passed")
        sys.exit(0)
    else:
        print("Test failed")
        sys.exit(-1)


if __name__ == '__main__':
    main()
