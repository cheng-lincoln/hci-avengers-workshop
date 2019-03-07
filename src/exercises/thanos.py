from src.load import load_rainbow_table
RAINBOW_TABLE = load_rainbow_table()

def crack(previous_guess, number_of_tries):
    """
    If your previous guess was 'abcd', then:
    previous_guess[0] == 'a'
    previous_guess[1] == 'b'
    previous_guess[2] == 'c'
    previous_guess[3] == 'd'

    number_of_tries is the number of tries..

    RAINBOW_TABLE[0] gives you the 1st entry in the rainbow table (e.g. 'able')
    RAINBOW_TABLE[5] gives you the 4th entry in the rainbow table (e.g. 'also')
    """
    guess = [c for c in previous_guess]
    force_stop = False

    #=== Start writing your code from here onwards! ===
    
    #=== Stop writing your code here! ===

    return (guess, force_stop)
