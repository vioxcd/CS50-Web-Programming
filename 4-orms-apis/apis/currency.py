import requests


def main():
    response = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
    if response.status_code != 200:
        raise Exception("ERROR: API request unsuccessful")
    data = response.json()
    rate = data["rates"]["EUR"]
    print(f"1 USD is equal to {rate} EUR")


if __name__ == "__main__":
    main()
