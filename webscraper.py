import requests
from bs4 import BeautifulSoup

def get_study_spaces():
    url = 'https://www.library.dartmouth.edu/spaces'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    spaces = [] 

    row_divs = soup.find_all('div', class_='row')
    for row_div in row_divs:
        grid_divs = row_div.find_all('div', class_='fx dcl-spaces-entry col-md-4 col-sm-4 col-xs-12')

        for grid_div in grid_divs:
            space = {}

            space_location = grid_div.find('div', class_='space-location').text.strip()
            space_title = grid_div.find('h2', class_='space-title').text.strip()
            space['location'] = space_location
            space['title'] = space_title

            if grid_div.find('div', class_='space-meta'):
                space_meta = grid_div.find('div', class_='space-meta')

                capacity_element = space_meta.find('div', class_='space-capacity')
                capacity = capacity_element.text.strip() if capacity_element else "Not specified"
                space['capacity'] = capacity

                amenities = space_meta.find('div', class_='space-activity').text.strip()
                space['amenities'] = amenities

                reserve_link = grid_div.find('a', class_='dcl-spaces-reserve')
                reserve_url = reserve_link['href'] if reserve_link else None
                space['reserve_url'] = reserve_url

            else:
                noise_level = grid_div.find('span', class_='noise-level').text.strip()
                space_summary = grid_div.find('div', class_='space-summary').text.strip()
                space['noise_level'] = noise_level
                space['summary'] = space_summary

            spaces.append(space)

    return spaces
