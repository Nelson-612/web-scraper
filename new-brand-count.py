import requests
from bs4 import BeautifulSoup

# Set Steam specials URL and fake a browser header
url = "https://store.steampowered.com/search/?specials=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find all game blocks
results = soup.find_all("a", class_="search_result_row")

print("🎮 Discounted Games on Steam:\n")
count = 0

for result in results:
    title = result.find("span", class_="title")
    discount_block = result.find("div", class_="discount_pct")
    price_block = result.find("div", class_="discount_final_price")

    # Skip entries without discount or price
    if not title or not discount_block or not price_block:
        continue

    discount_text = discount_block.text.strip()
    price_text = price_block.text.strip().replace("\r", "").replace("\n", " ").strip()

    # Only include games with an actual discount shown (e.g., "-50%")
    if discount_text:
        count += 1
        print(f"{count}. {title.text.strip()}")
        print(f"   🔻 Discount: {discount_text}")
        print(f"   💵 Price: {price_text}")
        print(f"   🔗 Link: {result['href']}\n")

if count == 0:
    print("No discounted games found. Steam may have updated their layout.")




