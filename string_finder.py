def capture_letters():
    """
    Counts how many times a specific letter appears in a user-provided text.

    Steps:
    1. Asks the user for a text.
    2. Asks the user which letter to count.
    3. Iterates through the text and counts matches.
    4. Prints the total count.

    Returns:
        None
    """
    
    how_many_letters = 0

    text = s_input("Please gives us your text : ")

    wanted_text = s_input("Which letter do you want to capture? =")

    for x in text:
        if x == wanted_text:
            how_many_letters +=1

    print(f"There are about {how_many_letters} {wanted_text} in total.\n")

def capture_words():
    """
     Counts how many times a specific word appears in a given text.

    This function:
    - Prompts the user for a text input.
    - Splits the text into words.
    - Prompts the user for a target word.
    - Iterates through the word list.
    - Counts every match of the chosen word.
    - Prints the total number of occurrences.

    Returns:
        None
    """
    
    how_many_words = 0

    text = s_input("Please gives us your text : ")

    text = text.split()

    wanted_text = s_input("Which word do you want to capture? =")

    for x in text:
        if x == wanted_text:
            how_many_words +=1  ## I know that the count() does the same thing but why not ? :)

    print(f"There are about {how_many_words} {wanted_text} in total.\n")

def play_again():
    """
    Asks the user if they want to run the program again.

    The function:
    - Returns True if the user types 'y'.
    - Returns False if the user types 'n'.
    - Repeats the question until a valid answer is given.

    Returns:
        bool: True for 'y', False for 'n'
    """

    play_again = True

    while play_again:

        playAgain = s_input("Wanna play again ? (y)(n) = ")

        if playAgain not in ["y","n"]:

            print("Please just type 'y' or 'n'.")
            continue

        elif playAgain == "n":

            print("Thank you for using our program!...")
            return False
        else:
            return True
        

def s_input(prompt : str, to_lower = True):
    """
     A safer input function that strips leading/trailing spaces
    and optionally converts the text to lowercase.

    Args:
        prompt (str): Message shown to the user.
        to_lower (bool, optional): Convert output to lowercase. Defaults to True.

    Returns:
        str: Cleaned user input.
    """
    
    user_input = input(prompt).strip()    

    return user_input.lower() if to_lower else user_input  ## if to_lower is true user_input = user_input.lower()  else  user_input = just user_input.strip()


if __name__ == "__main__":
    
    print("Welcome to string finder !\n")

    def main():

        play = True
        
        while play:

            words_or_letters = s_input("Would you like to capture words or letters ? (w)(l):")
        
            match words_or_letters:
                case "w":
                    capture_words()
                case "l":
                    capture_letters()

            play = play_again()
            
    main()
