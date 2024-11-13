from dotenv import load_dotenv
import imaplib
import email
import os
import requests
from bs4 import BeautifulSoup
load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD") # App password for authentication

def connect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail
    
def extract_link_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links

def click_link(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"Clicked link: {link}")
        else:
            print(f"Failed to click link: {link}, Error code: {response.status_code}")
    except Exception as e:
        print(f"Failed to click link: {link}, Error: {str(e)}")    
    
def search_for_email():
    mail = connect_to_mail()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()
    
    links = []
    
    for num in data:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode()
                    links.extend(extract_link_from_html(html_content))
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode()
            
            if content_type == "text/html":
                links.extend(extract_link_from_html(content))
    
    mail.logout()
    return links

def save_link(links):
    with open("links.txt", "w") as f:
        f.write("\n".join(links))

# Search for unsubscribe links in emails and click them. Save the clicked links to a file. 
links = search_for_email()
for link in links:
    click_link(link)
    
save_link(links)