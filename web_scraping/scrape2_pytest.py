import json
import pyautogui
from playwright.sync_api import sync_playwright
from colorama import Fore, Style, init
from scrapy.utils.display import pprint

# Get the screen size using pyautogui
screen_size = pyautogui.size()
width, height = screen_size.width, screen_size.height

# Initialize colorama
init()


# Assuming href_dict is defined like this:
# href_dict = {"Exhibitor1": "link1", "Exhibitor2": "link2", ...}

def process_exhibitors(page, href_dict):
    exhibitors = []

    # Process each unique link in the dictionary
    for i, (key, href) in enumerate(href_dict.items()):
        print(f"Processing link {i + 1}/{len(href_dict)}: {href} (Exhibitor: {key})")
        exhibitor_data = extractor(page, href)
        # Optionally, you can store the data with the exhibitor name as a key
        exhibitors.append({key: exhibitor_data})

    return exhibitors


def extractor(page, href):
    # Navigate to the link
    page.goto(href)

    # Wait for the page to load fully
    page.wait_for_selector('body')

    # Extract relevant information, for example:

    # Extract the exhibitor's name
    name_selector = "h1.exhibitor-name"  # Update this selector based on the actual HTML structure
    exhibitor_name = (page.inner_text(name_selector)).strip().rstrip(',\n').rstrip('"') if page.query_selector(
        name_selector) else "Name unknown"

    # Extract other information such as description, web address, phone_number,
    web_address_selector = "#js-vue-contactinfo>div>div>ul>li>a"  # Update this selector based on the actual HTML
    phone_number_selector = "article#js-vue-contactinfo>div>div>ul>li:nth-of-type(2)"
    description_selector = "#section-description > div > p"
    products_selector = "article#js-vue-productsgrouped"

    # structure
    exhibitor_web_address = (
        (page.inner_text(web_address_selector)).replace('\n', ' ').replace('\t', '').strip().rstrip('"')
        if page.query_selector(web_address_selector) and "." in page.inner_text(web_address_selector)
        else "No Web Info"
    )

    # First, extract the phone number text as before
    exhibitor_phone = (page.inner_text(phone_number_selector)).replace('\n', '').replace('\t', '').strip().rstrip(
        '"') if page.query_selector(phone_number_selector) else "No Phone Info"

    # Then, extract only the digits from the phone number
    exhibitor_phone = ''.join(char for char in exhibitor_phone if char.isdigit()).rstrip('"')

    # If you want to ensure it's not empty after filtering
    exhibitor_phone = exhibitor_phone if exhibitor_phone else "No Phone Info"

    exhibitor_description = (page.inner_text(description_selector)).replace('\n', ' ').replace('\t', '') \
        .replace('\xa0', ' ').strip().rstrip('"') if page.query_selector(
        description_selector) else "No Description Info"

    exhibitor_products = (page.inner_text(products_selector)).replace('\n', ' ') \
        .replace('\t', '').strip().rstrip('"') if page.query_selector(products_selector) else "No Products Info"

    # Return the extracted information as a dictionary
    exhibitor_info = {
        "ex_href": href,
        "name": exhibitor_name,
        "web": exhibitor_web_address,
        "phone": exhibitor_phone,
        "description": exhibitor_description,
        "products": exhibitor_products
    }

    # Print the dictionary in the specified order
    pprint(json.dumps(exhibitor_info, indent=5, sort_keys=False))
    return exhibitor_info


def get_element_text(page, element, default="NA"):
    """Helper function to get text content of an element if visible."""
    return page.inner_text(element).replace('\n', ' ').replace('\t', '').strip() if element.is_visible() else default


def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": width, "height": height})
        page = context.new_page()

        # Navigate to the webpage
        url = "https://directory.imts.com/8_0/explore/exhibitor-gallery.cfm?featured=false"
        page.goto(url)
        print("Navigating to the webpage...")

        # Wait for the page title to ensure the page is loaded
        page.wait_for_load_state('domcontentloaded')
        title = page.title()
        print(f"Page Title:  {Fore.GREEN + title + Style.RESET_ALL}")

        cards_str = 'li.js-Card.card.br3.dib.float.pa3'
        #
        # # Count the initial number of cards
        cards_init = page.query_selector_all(cards_str)
        print(f"Number of cards before clicking 'See All Results' button: {len(cards_init)}")

        print('===================  ================')
        # Click on "See All Results" to load all exhibitors
        print("Clicking on 'See All Results'...")
        see_all_button = page.locator("text=See All Results")
        see_all_button.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        see_all_button.click()
        page.wait_for_timeout(5000)  # crucially important - run without this line once!

        # Count the number of cards after clicking the button
        cards_str_all = 'li.js-Card.card.br3.dib.float.pa3'
        cards_all = page.query_selector_all(cards_str_all)
        print(f"Number of cards after clicking 'See All Results' button: {len(cards_all)}")
        page.evaluate("document.documentElement.style.zoom='80%'")

        # creating a dictionary by href_id as key and href as value - to avoid duplicate entries
        href_dict: dict[str, str] = {}

        # Process each card and get href_on_card/exhibitor site and add it to href_dict:
        for i, card in enumerate(cards_all):
            if i % 15 == 0:
                card.scroll_into_view_if_needed(timeout=20000)
            # the above one line was needed in playwright Java, but not mandatory for playwright pytest;
            # with the line, execution is slower
            print(f"===================Processing an exhibitor............")
            print(f"Extracting exhibitor data for card...{i}")

            try:
                # Wait for the website lead element to be available
                website_lead = card.wait_for_selector('a', timeout=15000)  # Adjust the selector and timeout as needed

                if website_lead is not None:
                    website_trans_url = 'https://directory.imts.com' + website_lead.get_attribute('href')
                    print(f"Website Transition URL: {website_trans_url}")
                    # Split the URL by '/'
                    parts = website_trans_url.split('/')
                    # The digits are located at the fifth index (index starts at 0)
                    digits = parts[5]
                    href_id = digits
                    href_dict[href_id] = website_trans_url

                    # Continue processing with the website_trans_url...
                else:
                    print(f"Website link not found for card {i}, skipping...")
                    continue
            except Exception as e:
                print(f"Error processing card {i}: {e}")
                continue

        # Add the rest of your processing logic here...
        print('================================= href list ==========================================')
        non_duplicate_entries = len(href_dict)
        print('Number of non duplicate entries:', non_duplicate_entries)
        print('================================= pretty print href_dict ==========================================')
        pprint(href_dict)

        exhibitors_data = process_exhibitors(page, href_dict)
        print('================================= pretty print exhibitors_data ========================================')
        pprint(exhibitors_data)


# Run the scrape function
scrape()
