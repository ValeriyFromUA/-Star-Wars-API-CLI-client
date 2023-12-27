import json
import requests
from typing import NoReturn


def get_response(category: str, item_id: str = None) -> json:
    data = requests.get(f'https://swapi.dev/api/{category}{"/" + item_id if item_id else ""}')
    return data.json() if data else {'error': 'Service not available'}


def get_input_data() -> tuple[str, str]:
    valid_categories = ['people', 'planets', 'starships']
    print("Available categories: people, planets, starships")
    category = input("Enter a category: ").lower()
    while category not in valid_categories:
        print("Invalid category. Please choose from people, planets, or starships.")
        category = input("Enter a valid category: ").lower()
    item_id = input("Enter an ID (press Enter to skip): ")
    while item_id and int(item_id) < 1:
        print("Invalid ID. Enter an valid ID (press Enter to skip):")
        item_id = input("Enter an valid ID (press Enter to skip): ")

    return category, item_id


def create_report() -> NoReturn:
    category, item_id = get_input_data()
    print(get_response(category, item_id))


if __name__ == '__main__':
    create_report()
