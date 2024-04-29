from is_numberr import is_number

def equal(x: str)-> bool :
    '''This function receives a word and returns True or false
    depending on whether the word is a palindrome or not'''

    for i in range(len(x)//2): # Compare the first and the last character, the second and the penultimate  
        if x[i] != x[-i-1]: # and continue comparing like this until reaching the characters that are in the middle of the word
            return False # When it does the comparison, if there are two different characters, it returns false
    return True # If all is equal, it returns True
    
if __name__ == "__main__": # Function main, the starting point of the code
    try:
        print("This program is a palindorme verificator")

        x: str = input("Enter the word that you think that is a palindrome: ")

        if is_number(x):
            raise TypeError("You enter a str of numbers not a word (str of letters)")  
        print("The word",x, "is", str(equal(x))+"ly a palindrome")
        
    except TypeError as error:
        print(f"Error: {error}")