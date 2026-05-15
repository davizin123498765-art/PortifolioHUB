from playwright.sync_api import sync_playwright
import requests
import os


def normalize_url(url):
    if url.startswith("//"):
        return "https:" + url
    return url
def download_image(url, index):
    url = normalize_url(url)
    response = requests.get(url)
    response.raise_for_status()
    file_path = f"images/page_{index}.jpg"
    with open(file_path, "wb") as f:
        f.write(response.content)

        print(f"Saved: {file_path}")
        
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        os.makedirs("images", exist_ok=True)
        page.goto("https://gauchazh.clicrbs.com.br/login/flip/?redirectUri=https%3A%2F%2Fflipzh.clicrbs.com.br%2F%2Fjornal-digital%2Fpub%2Fgruporbs%2F%3Fflpzh%3Dprd")

        login_iframe = page.frame_locator(".box-login-nossa > iframe:nth-child(1)")

        email_input = login_iframe.locator("....")
        email_input.fill("....")

        email_submit_button = login_iframe.locator("#submit-button")
        email_submit_button.click()
        password_submit_button = login_iframe.locator("#senha")
        password_submit_button.fill("....")
        password_click = login_iframe.locator("#submit-button")
        password_click.click()

        ammount_of_pages = (int(33))
        current_page = 1       
        first_img = page.locator("img.pageimg").first
        first_img.wait_for()
        img = page.locator("img.pageimg").last
        src = img.get_attribute("src")
        src = normalize_url(src)
        print(first_img.get_attribute("src"))
        download_image(src, 1)
        for i in range(1,ammount_of_pages +1):
            
            page.locator(".multimidia_next").click()
            
            img = page.locator("img.pageimg").last
            src = img.get_attribute("src")
            src = normalize_url(src)

            download_image(src, i)
            print("done downloading")
            current_page += 1     
            
            pass

        page.screenshot(path="result.png", full_page=True)
        pass


    print("Hello from importer!")
    pass

if __name__ == "__main__":
    main()

