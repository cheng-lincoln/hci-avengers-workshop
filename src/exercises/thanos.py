from src.load import load_rainbow_table
RAINBOW_TABLE = load_rainbow_table()

def crack(previous_guess, number_of_tries):
    guess = [c for c in previous_guess]
    force_stop = False

    #=== Start writing your code from here onwards! ===
    # Same as exercise 1 (hulk.py), except that now (number_of_tries)
    # tells you the number of tries you have made so far

    # RAINBOW_TABLE[0] gives you the 1st entry in the rainbow table (e.g. 'able')
    # RAINBOW_TABLE[5] gives you the 4th entry in the rainbow table (e.g. 'also')

    #=== Stop writing your code here! ===

    return (guess, force_stop)
