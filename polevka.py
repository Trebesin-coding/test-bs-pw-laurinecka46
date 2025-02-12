from bs4 import BeautifulSoup
import requests


def main():
    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list = []

    ingredience = 



   

    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá


if __name__ == "__main__":
    main()