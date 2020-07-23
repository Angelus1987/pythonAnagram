# Anagrams & Palindromes
__author__ = "Angelus1987"
# Github: https://github.com/Angelus1987
# |# ends the app|
# Import
import sys
import collections



"""Where import statements and any variables should be declared.And if necessary manipulated for global use."""


def find_anagrams(word_for_search, search_list_dictionary):
    f = open("smaller.txt", "r", encoding="utf8")
    content = f.read()
    print(content)
    f.close()
    """Find dictionary palingrams."""
    #pass


def find_palingrams():
    """Find dictionary palingrams."""
    pass


def print_generic_list(list_items_category_name, list_to_print):
    """Print a list of the items in any list passed to the function. Use the first parameter to describe the list."""
    pass


def find_palindromes():
    """Find palindromes in the anagrams list."""
    f = open("smaller.txt", "r", encoding="utf8")
    # Create a list called "find_palindromes" into which all the files lines are read in to....
    find_palindromes = f.read()
    # print the list (that now has the file details in it)
    print(find_palindromes)
    f.close()

    #pass


def print_pairs_of_twos(dictionary_of_pairs):
    """Print the keywords and values of an dictionary passed to the method."""
    pass


def print_explanation():
    print(
        '''
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once. It can however us on a few of the letters.    
        A palindrome is a word, number, phrase, or other sequence of characters which reads the same 
        backward as forward, such as "madam" or "racecar".
    
        A palingram – a letter palingram. A palingram can also be created using syllables
        or words, in addition to individual letters. An example of this using words is, “He was, was he?” 
        Notice that the words can be reversed and the sentence still reads the same. 
        A sentence that is a palingram and a palindrome is, “I did, did I”  
        
        This application allows three activities.
    
          Activity A: Finds the anagrams for any word you enter. Then identifies palindromes, if there are any, 
                      in the identified anagrams. 
    
          Activity B: Finds all the word pairs in the dictionary list which form palingrams. 
                      The palingrams ignore spaces and hyphens.   
                      
          Activity C: Find all the palindromes in the dictionary.
          ''')


def write_anagrams_palindromes_to_file(original_word, anagrams_list, palindromes_list):
    """Write the lists of anagrams and the palindromes to a file.
    Use the original word in the file names and descriptions ."""
    pass


def write_palingrams_to_file(palingram_list):
    """Write the lists of palingrams to a file."""
    pass
# Defining a menu to use on startup where user have to input Capitalized letters like A, B, C, or the # to quit
def menu():
    print("Welcome")
    # time.sleep(1)
    print()

    choice = input("""          MENU Options: Please use | A | B | C | #
                          1: Would you like to: Enter Activity A?
                          2: Would you like to: Enter Activity B?
                          3: Would you like to: See all palindromes in the dictionary ?
                          4: Exit ? Enter #
                          Please enter your choice: """)

    if choice == "A":
        activitya()
    elif choice == "a":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "B":
        activityb()
    elif choice == "b":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "C":
        activityc()
    elif choice == "c":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "#":
        sys.exit()
    elif choice == str:
        print("Please use # to exit")

    elif choice == int or float:
        print('''Invalid entry






            Only Strings / letters are allowed please try again




            ''')
        print("")
        print("Please use A | B | C | #")
        print("Please try again")

        menu()
    else:
        print("Please use A | B | C | #")
        print("Please try again")
        menu()

def activitya():
    print('''    
        Activity A: Finds the anagrams for any word you enter.
        Then identifies palindromes, if there are any, in the identified anagrams.
        ''')

    menu()

pass

def activityb():
    print('''
    Activity B: Finds all the word pairs in the dictionary list which form palingrams.
    The palingrams ignore spaces and hyphens.
    ''')
    menu()
pass

def activityc():
    print('''
    Activity C: Finding all the palindromes in the dictionary.
    

    Please wait.






    Loading


    ''')
    
    # ########print(print_generic_list)
    
    print("The palindromes Are:", collections.Counter(find_palindromes()))
    menu()

pass

def main():
    """The main method with primary functionality of the application."""
    running = True
    pass
# ______________________________________________________________________________

if __name__ == '__main__':
    menu()

