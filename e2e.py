import requests

def test_homepage():
    url = 'http://localhost:8777/'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == "Hello, World!"

if __name__ == "__main__":
    test_homepage()
    print("All tests passed!")
