import requests
import re
from bs4 import BeautifulSoup


def req_url(url: str):
    """
    Sends a GET request to THE URL and handles status codes.

    Args:
        url (str): The URL for the request.

    Returns:
        requests.Response or None:
            - The response object if request succeeded.
            - None if the request fails or an error occurs.

    Raises:
        Prints an error message for any exceptions.
    """
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error for {url}: {response}")
            return None

        return response
    except Exception as e:
        print(f"An error occured when requesting the page: {e}")

def scrape_states(response):
    """
    Extracts state names and associated links from a table in the HTML.
    The state names are cleaned of special characters and the links are
    relative paths (/wiki/{state}) of the states.

    Args:
        response (requests.Response): The response object with the HTML to be parsed.
    Returns:
    tuple: A tuple containing two lists:
        - states (list): A list of state names as strings.
        - state_links (list): A list of Wikipedia links for each state respectively.
    """
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
    """
    Scrapes state details: area, population, neighbors, languages, political system,
    capital, and density from the provided HTML response.
    Specifically, extracts data from a table with class 'infocaseta', parses fields
    based on their headers

    Args:
        response (requests.Response): The response object containing the HTML to be parsed.

    Returns:
        list: A list of parsed state details
    """
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", attrs={"class": "infocaseta"})

    rows = table.findAll("tr")

    state_data = {
        'totală': None, # area
        'vecini': None,
        'fus orar': None,
        'densitate': None,
        'estimare': None, # population
        'limbi oficiale': None,
        'sistem politic': None,
        'capitala': None
    }

    for row in rows:

        header = row.find("th")
        value = row.find("td")
        if header and value:
            header_text = header.get_text(strip=True).lower()
            header_text = ''.join(char for char in header_text if char.isalpha() or char.isspace())
            header_text = header_text.strip()
            value_text = value.get_text(strip=True)

            if header_text == 'fus orar':
                state_data['fus orar'] = value_text
            elif header_text == 'totală':
                state_data['totală'] = format_area(value_text)
            elif header_text == 'estimare' or header_text == 'recensământ': # Norvegia uses recensamant
                state_data['estimare'] = format_population(value_text)
            elif header_text == 'vecini':
                state_data['vecini'] = format_neighbors(value)
            elif header_text == 'limbi oficiale':
                state_data['limbi oficiale'] = format_languages(value)
            elif header_text == 'sistem politic':
                state_data['sistem politic'] = format_political_system(value)
            elif header_text == 'capitala':
                state_data['capitala'] = format_capital(value)
            elif header_text == 'densitate':
                state_data['densitate'] = format_density(value_text)

    return state_data

def format_area(value_text):
    """
    Format the area value by removing unwanted characters and extracting the relevant number.

    Args:
        value_text (str): The text containing the area data.

    Returns:
        str: The cleaned area value as a string.
    """
    new_value_text = re.sub(r'[ ,.\xa0]', '', value_text)
    match = re.match(r'^\d+', new_value_text)
    return match.group() if match else value_text


def format_population(value_text):
    """
    Format the population estimate by extracting only the relevant number.

    Args:
        value_text (str): The text containing the population data.

    Returns:
        str: The formatted population estimate.
    """
    new_value_text = value_text.split()[0]
    new_value_text = ''.join([char for char in new_value_text if char.isdigit() or char == '.'])
    return new_value_text.replace('.', '')


def format_neighbors(value):
    """
    Format the neighbors' names then join them with commas.

    Args:
        value (BeautifulSoup element): The 'td' element containing the neighbors' data.

    Returns:
        str: A string containing the names of the neighbors separated by commas.
    """

    # fix for Belarus , [5]
    value_text = [border.get_text(strip=True) for border in value.findAll('a')]
    value_text.pop()  # Removing the last needless row on the page
    value_text = [text for text in value_text if text.replace(' ', '').isalpha()] # On some states would include refs: <neighbor>[<digit>]
    value_text = ', '.join(value_text)

    return value_text


def format_languages(value):
    """
    Extract the first official language

    Args:
        value (BeautifulSoup element): The 'td' element containing the languages' data.

    Returns:
        str: The name of the first official language.
    """
    first_anchor = value.find('a')
    if first_anchor:
        return first_anchor.get_text(strip=True)
    return value.get_text(strip=True)

def format_political_system(value):
    """
    Extract and format the political system.

    Args:
        value (BeautifulSoup element): The 'td' element containing the political system data.

    Returns:
        str: The formatted political system as a string.
    """
    new_value_text = ''
    for anchor in value.findAll('a'):
        text = anchor.get_text(strip=True)
        if text.replace(' ', '').replace('-', '').isalpha():
            new_value_text += text + ' '

    if new_value_text == '':
        new_value_text += value.get_text(strip=True)

    return new_value_text.strip().rstrip(',')


def format_capital(value):
    """
    Extract and format the capital city.

    Args:
        value (BeautifulSoup element): The 'td' element containing the capital data.

    Returns:
        str: The formatted capital city as a string.
    """
    new_value_text = ''
    # must fix for antigua saint john's
    for anchor in value.findAll('a'):
        text = anchor.get_text(strip=True)
        new_value_text += ''.join([char for char in text if char.isalpha() or char.isspace() or char == '\'']) + ', '
    return new_value_text.strip().rstrip(', ').lstrip(', ')


def format_density(value_text):
    """
    Format the density value by removing unwanted characters.

    Args:
        value_text (str): The text containing the density data.

    Returns:
        str: The formatted density value.
    """

    if value_text.startswith('('): # Republica Moldova references the year at the start, not the end
        match = re.search(r'(\d+,\d+)', value_text)
        if match:
            value_text = match.group(1)

        return value_text.replace(',', '.') # Romania uses ,
    return value_text.replace('[', ' ').replace('/', ' ').replace('.', '').replace(',', '.').split()[0]

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

        state_data = scrape_state_data(state_page)

        print(f"State: {states[i]}")
        print(state_data)

if __name__ == "__main__":
    main()