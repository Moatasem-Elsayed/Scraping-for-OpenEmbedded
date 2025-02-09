from playwright.sync_api import sync_playwright
from tabulate import tabulate
import sys

if len(sys.argv)!=2:
    print("Usage: python test.py <search_term>")
    sys.exit(1)

searched_term = sys.argv[1]
pw = sync_playwright().start()
browser = pw.chromium.launch(
    
)

page = browser.new_page()
page.goto("https://layers.openembedded.org/layerindex/branch/master/recipes/")
page.get_by_placeholder("Search recipes").fill(f"{searched_term}")
page.locator("xpath=/html/body/div[1]/div/div/div[1]/form/div/div/div/div/button").click()
page.wait_for_load_state("load")
rows = page.locator("xpath=/html/body/div[1]/div/div/table/tbody/tr")

display = []
for row in rows.element_handles():
    try:
        row.wait_for_selector("td")
        columns = row.query_selector_all("td")
        recipe_name = columns[0].inner_text()
        version = columns[1].inner_text()
        description = columns[2].inner_text()
        layer = columns[3].inner_text()
        display.append([recipe_name, version, description, layer])
    except Exception as e:
        # print(e)
        recipefile=page.locator("xpath=/html/body/div[1]/div/div/table[1]/tbody/tr[8]/td")
        recipefile=recipefile.inner_text()
        if recipefile:
            version=page.locator("xpath=/html/body/div[1]/div/div/table[1]/tbody/tr[2]/td").inner_text()
            description=page.locator("xpath=/html/body/div[1]/div/div/table[1]/tbody/tr[4]/td").inner_text()
            layer=page.locator("xpath=/html/body/div[1]/div/div/table[1]/tbody/tr[9]/td/a").inner_text()
            display.append([recipefile, version, description, layer])
            break
        continue
browser.close()

if not display:
    print("No results found")
    sys.exit(1)
headers = ["Name", "Version", "Description", "Layer"]
print(tabulate(display, headers=headers, tablefmt="grid"))