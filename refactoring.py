# Import necessary libraries
import random
import wikipedia

# Function to process external files
def process_external_file(file_name):
    with open(file_name, "r") as input_file:
        file_content = input_file.read()
        items_list = list(map(str.strip, file_content.split(",")))
        random_item = random.choice(items_list)
        return items_list, random_item

# Function to create hints
def create_hints(random_item):
    content_summary = wikipedia.summary(random_item, auto_suggest=False)
    remove_specifics = content_summary
    for specific_word in random_item.split():
        remove_specifics = remove_specifics.replace(specific_word, "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.lower(), "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.upper(), "XXXXXXX")
        remove_specifics = remove_specifics.replace(specific_word.capitalize(), "XXXXXXX")
    hint = remove_specifics.split(".")
    return hint

# Function to calculate points
def calculate_points(hint_counter):
    points_dicctionary = {0: 10, 1: 5, 2: 3, 3: 2, 4: 1}
    for key, value in points_dicctionary.items():
        if hint_counter == key:
            return value

# Function to start the game
def start_game(category_number, category_name, random_item):
    print(" \n\U0001F47E\U0001F579  ARKADIA TEAM \U0001F579 \U0001F47E \n    -- Presents -- ")
    print("\n   \U0001F914 GUESSINATOR \U00002753\n ")
    input("Press to continue...\n")
    hint_counter = 0

    # Prompt the user to choose a category
    get_category = input(
        "\n\U0001F449 Choose a category:\n \n\U0001F468 1. Characters \n\U0001F3F0 2. Places \n\U000023F0 3. Objects\n \n ")

    # Check if the chosen category matches the expected category number
    if get_category == category_number:
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
    else:
        print("\n\U0001F4A5 Invalid Category \U0001F4A5")

# Main function
# Main function
def main():
    # Process external files
    objects_list, random_object = process_external_file("objects.txt")
    places_list, random_place = process_external_file("places.txt")
    characters_list, random_character = process_external_file("characters.txt")

    # Define categories and their corresponding random items
    categories = [
        {"number": "1", "name": "character", "random_item": random_character},
        {"number": "2", "name": "place", "random_item": random_place},
        {"number": "3", "name": "object", "random_item": random_object}
    ]

    # Loop over categories and start the game for each
    for category in categories:
        start_game(category["number"], category["name"], category["random_item"])

if __name__ == "__main__":
    main()
