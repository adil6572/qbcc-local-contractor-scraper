import argparse
import time
from playwright.sync_api import Playwright, sync_playwright
import csv
from bs4 import BeautifulSoup

categories = [
    'Builders',
    'Building Certifiers',
    'Building Inspectors',
    'Designers',
    'Client Side Project Managers',
    'Air Con & Refrigeration',
    'Bricklaying',
    'Carpenters',
    'Concretors',
    'Flooring',
    'Gasfitting',
    'Glass & Glazing',
    'Guttering',
    'Kitchens',
    'Landscaping (Structural)',
    'Painting',
    'Paving',
    'Pest Control (Termites)',
    'Plastering',
    'Plumbing and Drainage',
    'Roofs and Roof Restoration',
    'Screens & Grilles',
    'Shade Sails',
    'Sheds',
    'Soil Testing',
    'Swimming Pools',
    'Tiling',
    'Waterproofing',
    'Fire Services',
    'Shop fitting',
    'Structural Steel',
    'Stone Masonry'
]


def save_to_csv(filename, data):
    fields = data[0].keys() if data else []
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    print(f'{len(data)} records saved to {filename}')


def scrape_data(page):
    soup = BeautifulSoup(page.content(), 'html.parser')
    tbody = soup.find("tbody")
    rows_data = []

    for row in tbody.find_all("tr"):
        row_data = {}
        for cell in row.find_all("td"):
            label = cell.attrs.get("data-label")
            value = cell.get_text(strip=True)
            row_data[label] = value
        row_data.pop("Action")
        rows_data.append(row_data)
    return rows_data


def run(playwright: Playwright, category, filename) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    url = 'https://my.qbcc.qld.gov.au/myQBCC/s/findlocalcontractor'

    page.goto(url)

    category_select = page.locator('select[name="select-business-type"]')
    category_select.select_option(value=category)

    range_select = page.locator('select[name="select"]')
    range_select.select_option(label='Unlimited km')

    region = 'ADELAIDE PARK, QLD 4703'
    page.locator('input[name="find"]').fill(region)
    page.query_selector('div[title="ADELAIDE PARK, QLD 4703"]').click()

    page.locator('.slds-button_neutral').nth(2).click()
    page.wait_for_selector('#status-div')

    print("Page loaded Sucessfully")

    page.get_by_text("Grid").click()
    page.locator('.itemMenu').nth(0).select_option(value="50")

    data = []
    cnt = 1
    try:
        while True:
            print(f"scraping page...{cnt}")
            data = data + scrape_data(page)
            next_button = page.locator('button:has-text("Next")')
            if next_button.is_enabled():
                next_button.click()
                time.sleep(0.5)
                cnt += 1
            else:
                break

    except Exception as e:
        print(f"unable to scrape next page {cnt}")
        print(e.with_traceback())

    try:
        save_to_csv(filename, data)
    except Exception as e:
        print(f"unable to save the data for {filename}")

    context.close()
    browser.close()


def main():
    parser = argparse.ArgumentParser(
        description='Scrape QBCC website for local contractors.')
    parser.add_argument('-c', '--category', type=str, required=True, choices=categories,
                        help='Category to search in (e.g. "Flooring")')
    parser.add_argument('-f', '--filename', type=str, default='data.csv',
                        help='Name of the output CSV file (default: "data.csv")')

    args = parser.parse_args()

    if args.category not in categories:
        print(
            f"Category '{args.category}' not recognized. Choose from: {categories}")
        return

    with sync_playwright() as playwright:
        print("Scraping Initialized")
        run(playwright, args.category, args.filename)


if __name__ == '__main__':
    main()
