import re
import sys

if __name__ == "__main__":
    sys.path.append('.')  # Add the current directory to sys.path
    from menuitem import MenuItem  # Assuming MenuItem is in menuitem.py
else:
    from menuitem import MenuItem


def clean_price(price_str: str) -> float:
    """
    Cleans a price string and converts it to a float.  Handles various formats.

    Args:
        price_str: The price string to clean (e.g., "$12.99", "10", "15,000.00").

    Returns:
        The cleaned price as a float. Returns 0.0 if the price is invalid.
    """
    if not isinstance(price_str, str):
        return 0.0  # Handle non-string input

    price_str = price_str.strip().replace("$", "").replace(",", "")
    try:
        return float(price_str)
    except ValueError:
        return 0.0



def clean_scraped_text(scraped_text: str) -> list[str]:
    """
    Cleans scraped text by removing unwanted elements and splitting it.

    Args:
        scraped_text: The scraped text to clean.

    Returns:
        A list of cleaned strings.
    """
    if not scraped_text:
        return []

    lines = scraped_text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if line in ["GS", "V", "S", "P"]:
            continue  # Skip specific codes
        if line.startswith("NEW!"):
            continue  # Skip "NEW!" indicator
        cleaned_lines.append(line)
    return cleaned_lines



def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    """
    Extracts menu item details from cleaned scraped text.

    Args:
        title: The title or category of the menu item.
        scraped_text: The scraped text containing item details.

    Returns:
        A MenuItem object.  Returns None on invalid input.
    """
    if not title or not scraped_text:
        return None

    cleaned_lines = clean_scraped_text(scraped_text)
    if not cleaned_lines:
        return None  # Handle empty cleaned text

    item_name = cleaned_lines[0]
    item_price = clean_price(cleaned_lines[1])
    item_description = cleaned_lines[2] if len(cleaned_lines) > 2 else "No description available."

    return MenuItem(category=title, name=item_name, price=item_price, description=item_description)



if __name__ == '__main__':
    # Example usage and testing
    test_items = [
        '''
NEW!

Tully Tots

$11.79

Made from scratch with shredded potatoes, cheddar-jack cheese and Romano cheese all rolled up and deep-fried. Served with a spicy cheese sauce.
        ''',
        '''Super Nachos

$15.49
GS

Tortilla chips topped with a mix of spicy beef and refried beans, nacho cheese sauce, olives, pico de gallo, jalapeños, scallions and shredded lettuce. Sour cream and salsa on the side. Add guacamole $2.39

        ''',
        '''Veggie Quesadilla

$11.99
V

A flour tortilla packed with cheese, tomatoes, jalapeños, black olives and scallions. Served with sour cream and pico de gallo.
Add chicken $2.99 | Add guacamole $2.39
''',
        '''Kid's Burger & Fries

$6.99
'''
    ]
    title = "TEST"
    for scraped_text in test_items:
        item = extract_menu_item(title, scraped_text)
        print(item)



if __name__=='__main__':
    pass
