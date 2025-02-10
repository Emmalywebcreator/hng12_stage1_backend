import requests

def get_fun_fact(n):
    """Fetch a fun fact about a number from numbersapi.com"""
    NUMBERS_API_URL = "http://numbersapi.com/"
    try:
        response = requests.get(f"{NUMBERS_API_URL}{n}")
        if response.status_code == 200:
            fact = response.text
        else:
            fact = "Could not retrieve a fact at this time"
    except requests.RequestException:
        fact = "Could not retrieve number api"
    return fact