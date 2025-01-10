import requests

BASE_URL = "http://127.0.0.1:5000"

def fetch_top_by_population(count = 10):
    """
    Fetch and print the top <count> states by population. Default is 10

    Args:
        count (int): The number of states to fetch for.
    """
    response = requests.get(f"{BASE_URL}/top-tari-populatie?limit={count}")
    if response.status_code == 200:
        states = response.json()

        print(f"Top {count} states by population:")
        for country in states:
            print(f"- {country[0]}: {country[1]} people")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_top_by_density(count = 10):
    """
    Fetch and print the top <count> states by density.

    Args:
        count (int): The number of states to fetch for.
    """
    response = requests.get(f"{BASE_URL}/top-tari-densitate?limit={count}")
    if response.status_code == 200:
        states = response.json()
        print(f"Top {count} states by density:")
        for country in states:
            print(f"- {country[0]}: {country[1]}")
    else:
        print(f"Failed to fetch data: {response.status_code}")


def fetch_utc_2():
    """
    Fetch and print the states with utc+2 Timezone.
    """
    response = requests.get(f"{BASE_URL}/tari-UTC+2")
    if response.status_code == 200:
        states = response.json()
        print("States With utc+2 Timezone:")
        for country in states:
            print(f"- {country[0]}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_states_english():
    """
    Fetch and print the states with english as official language.
    """
    response = requests.get(f"{BASE_URL}/tari-limba-engleza")
    if response.status_code == 200:
        states = response.json()
        print("States that speak english as official language:")
        for country in states:
            print(f"- {country[0]}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_states_political_system(system):
    """
    Fetch and print the states with a given political system.

    Args:
        system (str): The political system/regime to fetch for.
    """
    response = requests.get(f"{BASE_URL}/tari-regim-politic?regim={system}")
    if response.status_code == 200:
        states = response.json()
        print(f"States under the political system of {system}: ")
        for country in states:
            print(f"- {country[0]}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def main():
    fetch_top_by_population()
    fetch_top_by_density(3)
    fetch_utc_2()
    fetch_states_english()
    fetch_states_political_system("republică")

if __name__ == "__main__":
    main()

