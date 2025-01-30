import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY= os.getenv('OPENAI_API_KEY')

model = 'gpt-4o-mini'
openai = OpenAI()

class Website:
    '''
    We can represent a website with this class 
    '''
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else 'no_title_provided'
        if soup.body:
            for irrelevant in soup.body(['script','style','img','input']):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]
    def get_contents(self):
        return f'Webpage title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n'

git_max = Website("https://github.com/MaxGandini")
print(git_max.links)

# as you can see, the output is complicated to parse by hand, here we take an llm to sort this all out:

link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
link_system_prompt += "You should respond in JSON as in this example:"
link_system_prompt += """
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page": "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

def get_links(url):
    website = Website(url)
    response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": link_system_prompt},
                {"role": "user", "content": get_links_user_prompt(website)}
                ],
            response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

print(get_links("https://anthropic.com"))


