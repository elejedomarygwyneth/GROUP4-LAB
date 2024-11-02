def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    words_list = []
    try:
        with open(filename, 'r') as file:
            words_list = [word.strip() for word in file.readlines()]
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return tuple(words_list)

def main():
    """Main function to initialize vocabulary and demonstrate usage."""
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    articles = getWords("articles.txt")
    prepositions = getWords("prepositions.txt")
    
    print(f"Nouns: {nouns}")
    print(f"Verbs: {verbs}")
    print(f"Articles: {articles}")
    print(f"Prepositions: {prepositions}")

if __name__ == "__main__":
    main()

