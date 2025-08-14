# 🎮 Steam Specials Web Scraper

A Python script that scrapes **Steam's Specials** page to list discounted games, including their discount percentage, final price, and store link.

## 📌 Features
- Scrapes Steam's *Specials* section for current game discounts.
- Extracts:
  - Game title
  - Discount percentage
  - Final price
  - Direct store link
- Skips entries without a valid discount or price.
- Uses a fake User-Agent header to reduce the chance of being blocked.

## 🛠 Tech Stack
- **Python 3**
- [Requests](https://pypi.org/project/requests/) — Send HTTP requests.
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) — Parse HTML content.
