import requests
import re
from bs4 import BeautifulSoup
from requests import RequestException


def req_url(url: str):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error for {url}: {response}")
            return None

        return response
    except Exception as e:
        print(f"An error occured when requesting the page: {e}")

def scrape_states(response):
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    states = []
    state_links = []

    if table:
        rows = table.findAll("tr")
        for row in rows[1:]:
            cells = row.findAll("td")
            if not cells:
                continue

            first_cell = cells[0]
            bold_tag = first_cell.find("b")

            if bold_tag:
                state_name = bold_tag.get_text(strip=True).split(" - ")[0]
                state_name = ''.join(char for char in state_name if char.isalnum() or char.isspace() or char == '-')
                states.append(state_name)

                state_link = [anchor.get('href') for anchor in bold_tag.findAll('a') if anchor.get('href').startswith('/wiki')
                              and not anchor.get('href').endswith('.svg')][0]

                state_links.append(state_link)

    return states, state_links

def scrape_state_data(response):
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", attrs={"class": "infocaseta"})

    rows = table.findAll("tr")
    details = ('totală', 'vecini', 'fus orar', 'densitate', 'estimare', 'limbi oficiale', 'sistem politic', 'capitala')

    for row in rows:
        header = row.find("th")
        value = row.find("td")
        if header and value:
            header_text = header.get_text(strip=True).lower()
            header_text = ''.join(char for char in header_text if char.isalpha() or char.isspace())
            header_text = header_text.strip()
            value_text = value.get_text(strip=True)

            if header_text == 'totală':
                value_text = re.search(r'\b\d+(?:[., ]\d+)*\b', value_text)
                value_text = value_text.group(0).replace(',', '').replace('.', '').replace(' ', '')

            if header_text == 'vecini':
                value_text = [border.get_text(strip=True) for border in value.findAll('a')]
                value_text.pop()

            if header_text == 'limbi oficiale':
                first_anchor = value.find('a')
                if first_anchor:
                    value_text = first_anchor.get_text(strip=True)

            if header_text in details:
                print(f"Header: {header_text}, Value: {value_text}")



def main():
    response = req_url("https://ro.wikipedia.org/wiki/Lista_statelor_lumii")

    if not response:
        return

    states, state_links = scrape_states(response)
    base_url = "https://ro.wikipedia.org"

    for i in range(len(states)):
        state_url = base_url + state_links[i]
        state_page = req_url(state_url)
        if not state_page:
            return

        print(f"State: {states[i]}")
        scrape_state_data(state_page)

        print()

if __name__ == "__main__":
    main()