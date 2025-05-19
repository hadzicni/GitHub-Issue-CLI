import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

def list_issues(repo):
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for issue in response.json():
            print(f"#{issue['number']}: {issue['title']}")
    else:
        print(f"Error {response.status_code}: {response.text}")
