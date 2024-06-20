import random
import wikipedia


def guessinator_introduction():
    print(
        "\n\U0001F47E\U0001F579  ARKADIA TEAM \U0001F579 \U0001F47E \n    -- Presents --    \n\n\U0001F914 GUESSINATOR \U0001F914 \nThe Ultimate Guessing Game!\U00002753\n\n")
    input("Press Enter to continue...\n")
    print(
        "\n\U0001F579  In Guessinator, a player takes turns guessing random items from various categories.\n\U0001F579  The player receives hints from the Wikipedia library related to the random item.\n\U0001F579  The goal is to correctly guess the item with the fewest attempts possible.\n\U0001F579  The correct guess wins the game! Let the guessing begin!\U0001F4AA\n")
    input("\nPress Enter to continue...\n")


def process_external_file(file_name):
    """
    function processes external file and returns list of items and the random item.
    """
    with open(file_name, "r") as input_file:
        file_content = input_file.read()
        items_list = list(map(str.strip, file_content.split(",")))
        random_item = random.choice(items_list)
        return (items_list, random_item)


objects_list, random_object = process_external_file("objects.txt")
places_list, random_place = process_external_file("places.txt")
characters_list, random_character = process_external_file("characters.txt")
animals_list, random_animal = process_external_file("animals.txt")
books_list, random_book = process_external_file("books.txt")


def create_hints(random_item):
    """
    Retrieve the list of hints from wikipedia library
    """
    content_summary = wikipedia.summary(random_item, auto_suggest=False)
    remove_specifics = content_summary
    for specific_word in random_item.split():
        remove_specifics = remove_specifics.replace(specific_word, "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.lower(), "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.upper(), "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.capitalize(), "XXXXXXX")

    hints = remove_specifics.split(".")
    long_hints = []
    for hint in hints:
        if len(hint) >= 50:
            long_hints.append(hint)
    random.shuffle(long_hints)
    return long_hints


def calculate_points(hint_counter):
    """
    Calculate the points based on the hints given
    """
    points_dicctionary = {0: 10, 1: 5, 2: 3, 3: 2, 4: 1}
    for key, value in points_dicctionary.items():
        if hint_counter == key:
            return value


def get_category_input():
    """
    Get category input from the user and validate it.
    """
    while True:
        get_category = input(
            "\n\U0001F449 Choose a category by entering the category number: \n \n\U0001F468 1. Characters \n\U0001F3F0 2. Places \n\U000023F0 3. Objects \n\U0001F438 4. Animals \n\U0001F4D6 5. Books\n \n ")
        if get_category in ["1", "2", "3", "4", "5"]:
            return get_category
        else:
            print("Invalid Category. Please choose a valid category number (1-5).")


def start_game(category_number, category_name, random_item):
    """
    function compares the category to user input
    """
    hint_counter = 0
    hints = create_hints(random_item)
    for hint in hints[0:5]:
        print("\n\U00002B50 Your hint: \U00002B50", hint)
        user_guess = input(f"\n\U0001F449 Guess the {category_name}: ")
        if random_item.lower() == user_guess.lower():
            print("\nYou Win! \U0001F3C6")
            total_points = calculate_points(hint_counter)
            print(f"Total Points: {total_points}")
            break
        else:
            print("\nTry Again! \U0001F3B2\n")
            hint_counter += 1
    else:
        print("\nYou Lose! \U0001F622")
        print(f"The correct answer was: {random_item}")


def main():
    guessinator_introduction()

    category_dictionary_random = {"1": random_character, "2": random_place, "3": random_object, "4": random_animal,
                                  "5": random_book}
    category_dictionary = {"1": "Character", "2": "Place", "3": "Object", "4": "Animal", "5": "Book"}

    category = get_category_input()
    category_random = category_dictionary_random[category]
    category_name = category_dictionary[category]

    start_game(category, category_name, category_random)


if __name__ == "__main__":
    main()


