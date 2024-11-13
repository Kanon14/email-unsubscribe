# email-unsubscribe

## Overview
This Python script automates the process of searching for "unsubscribe" links in your Gmail inbox, clicking on those links, and saving them to a file. It is useful for quickly handling email unsubscriptions without manually clicking each link. The script utilizes the `imaplib` library to access your Gmail inbox, `email` to parse email content, and `BeautifulSoup` to find and filter unsubscribe links within HTML email content.

## Project Setup
### Prerequisites
- Python 3.8+
- Compatible cuda toolkit and cudnn installed on your machine.
- Anaconda or Miniconda installed on your machine.
- Environment Variables: The script requires a `.env` file to securely load your Gmail email credentials. Create a `.env` file with the following:
    ```bash
    EMAIL = your_email@gmail.com
    PASSWORD = your_password
    ```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Kanon14/email-unsubscribe.git
cd email-unsubscribe
```

2. Create and activate a Conda environment:
```bash
conda create -n email-unsubscribe python=3.10 -y
conda activate email-unsubscribe
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Functinality
1. **Email Login and Connection:** Connects to Gmail using `IMAP` to access the inbox.
2. **Email Search:** Searches for emails containing the term "unsubscribe" in their body.
3. **Link Extraction:** Parses each email to find "unsubscribe" links using BeautifulSoup.
4. **Click Links:** Attempts to open each unsubscribe link, logging success or failure.
5. **Save Links:** Saves all clicked links to a text file (`links.txt`) for record-keeping.


## How to Run
1. **Run the Script:** Execute the script to find, click, and save unsubscribe links:
    ```bash
    python main.py
    ```
2. **Output:** The script will print the status of each unsubscribe link (clicked or failed) and create a `links.txt` file containing all found links. 
