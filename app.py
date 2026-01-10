favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["Grand Canyon", "Yosemite", "Niagara Falls"],
    "Charlie": ["Maldives", "Bali", "Santorini"]
}
for person, places in favorite_places.items():
    print(f"{person} likes the following places:")
    for place in places:
        print(f"- {place}")
    print()

