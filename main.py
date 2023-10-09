import subprocess
import requests
import pyfiglet
import rich
from rich.rule import Rule
import os
import sys
from bs4 import BeautifulSoup

print(pyfiglet.figlet_format(str("WEBEXE")))

line = Rule("", style="white")

print("Checking dependencies...")

os.system("pip.exe install -r requirements.txt")

os.system("cls" if os.name == "nt" else "clear")

print(pyfiglet.figlet_format(str("WEBEXE")))

line = Rule("", style="white")

print(line)

while True:
    url = input("\nEnter a URL to create an application for.")
    try:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip()
            website_title = title
        except Exception as e:
            rich.print(f"An error occurred while fetching the website title: {str(e)}")
            website_title = None

        if website_title:
            if sys.platform.startswith("win"):
                chrome_proxy_path = f"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe"
            else:
                chrome_proxy_path = f"{os.environ['HOME']}/.config/google-chrome/Default/chrome_proxy.exe"
            subprocess.run([chrome_proxy_path, "--app=" + url, "--name=" + website_title], check=True)
            rich.print(f"Successfully built Chrome app for {url} with the name '{website_title}'.")
        else:
            rich.print("Unable to fetch the website title. Please check the URL.")
            
    except Exception as e:
        rich.print(f"An error has occurred: {str(e)}")
    
    except KeyboardInterrupt:
        rich.print("Interrupted! Have a nice day :)")
