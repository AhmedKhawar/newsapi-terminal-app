import requests

while True:
    query = input("Enter the topic of the news you want to see: ")
    key="7639992b06704b1a912f7286e340fe38"
    api = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-04&sortBy=publishedAt&apiKey={key}"

    content = requests.get(api)

    reply = content.json()
    newsCount = 1

    for news in reply["articles"]:
        print(f"{newsCount}. Title:", news["title"])
        print("\n")
        print(f"{newsCount}. URL:", news["url"])
        print("\n")
        print("********************************************\n\n")
        newsCount += 1
    
    choice = input("Do you want to look up for any other topic ('q' to exit - 'y' to continue): \n")
    if choice != 'q':
        newsCount = 0
    else:
        break
