import subprocess
import requests
import pyfiglet
import rich
from rich.rule import Rule
import os
import sys
from bs4 import BeautifulSoup

os.system("cls" if os.name == "nt" else "clear")

print(pyfiglet.figlet_format(str("WEBEXE")))

line = Rule("", style="white")

rich.print(line)

print("\nChecking dependencies...\n")

if sys.executable.endswith(f"\\anaconda3\\python.exe"):
    os.system(f"{sys.executable[:-len('python.exe')]}\\Scripts\\activate")
    os.system("conda.bat activate base")
    os.system(f"{sys.executable[:-len('python.exe')]}\\Scripts\\pip.exe install -r requirements.txt")
else:
    os.system(f"{sys.executable[:-len('python.exe')]}\\Scripts\\pip.exe install -r requirements.txt")

os.system("cls" if os.name == "nt" else "clear")

print(pyfiglet.figlet_format(str("WEBEXE")))

line = Rule("", style="white")

rich.print(line)

while True:
    try:
        url = input("\nEnter a URL to create an application for: ")
        url.strip()
        try:
            try:
                if url.startswith("http") or url.startswith("ws") or url.startswith("wss"):
                    response = requests.get(url)
                else:
                    response = requests.get(f"http://{url}")
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
            rich.print("Process interrupted!")
    
    except KeyboardInterrupt:
        rich.print("\n")
        rich.print("Interrupted! Have a nice day :)")
        os._exit(0)
