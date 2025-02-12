from playwright.sync_api import sync_playwright
import os




def main():

    with sync_playwright() as p:
        login = "Jarmil"
        password = "Admin123"
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://js-trebesin.github.io/playwright-exam/")
        page.fill("input[id='login']", login)
        page.fill("input[id='pass']", password)
        

        page.click("button[class='login-btn']")
        jarmil = page.locator("class['psst']")


      
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!
        
        input("n")
        print(jarmil)
        browser.close()
        

if __name__ == "__main__":
    main()
