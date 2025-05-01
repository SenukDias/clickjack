import requests
import sys
from colorama import Fore, Style, init
import webbrowser
import os

# Initialize colorama
init(autoreset=True)

def check_clickjacking(url):
    try:
        print(f"{Style.BRIGHT}🔍 Checking Clickjacking protection for: {Fore.CYAN}{url}\n")

        response = requests.get(url)
        headers = response.headers

        x_frame_options = headers.get('X-Frame-Options')
        content_security_policy = headers.get('Content-Security-Policy')

        if x_frame_options:
            print(f"{Fore.GREEN}✔ X-Frame-Options is set: {Fore.YELLOW}{x_frame_options}")
        else:
            print(f"{Fore.RED}✖ X-Frame-Options header is NOT set!")

        if content_security_policy:
            if 'frame-ancestors' in content_security_policy:
                print(f"{Fore.GREEN}✔ Content-Security-Policy with frame-ancestors is set:")
                print(f"{Fore.YELLOW}  {content_security_policy}")
            else:
                print(f"{Fore.LIGHTRED_EX}⚠ Content-Security-Policy is present but missing 'frame-ancestors':")
                print(f"{Fore.YELLOW}  {content_security_policy}")
        else:
            print(f"{Fore.RED}✖ Content-Security-Policy header is NOT set!")

        if not x_frame_options and not content_security_policy:
            print(f"\n{Fore.RED}{Style.BRIGHT}❌ Your site may be vulnerable to Clickjacking!")
        else:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Your site appears to be protected against Clickjacking.")

        # Write the HTML test file
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Clickjacking Test</title>
        </head>
        <body>
            <h2>🔒 Clickjacking Test for: {url}</h2>
            <p>If the website loads below, it may be vulnerable to clickjacking:</p>
            <iframe src="{url}" width="800" height="600" style="border:2px solid black;"></iframe>
        </body>
        </html>
        """

        with open("clickjacking_test.html", "w") as f:
            f.write(html_content)

        print(f"\n{Fore.CYAN}🌐 Opening visual test in your browser...")
        webbrowser.open("file://" + os.path.abspath("clickjacking_test.html"))

    except Exception as e:
        print(f"{Fore.RED}⚠ Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Usage: python clickjacking_check.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "http://" + url
    check_clickjacking(url)

