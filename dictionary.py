import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nDefinitions for '{word}':")
        for meaning in data[0]['meanings']:
            part_of_speech = meaning['partOfSpeech']
            for definition in meaning['definitions']:
                print(f"- ({part_of_speech}) {definition['definition']}")
    else:
        print(f"\nSorry, no definition found for '{word}'.")


# Main loop
while True:
    word = input("\nEnter a word (or type 'exit' to quit): ").strip()
    if word.lower() == 'exit':
        break
    get_definition(word)
