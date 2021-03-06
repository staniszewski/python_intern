import re

# Function that calculates hack power based on base_power dictionary.
# If the hack contains other characters than base letters allowed, hack is useless and its power is equal to zero.
def hack_calculator(hack):

    hack_phrase = re.compile(r'(ba{1,2})')
    hack_power = 0
    base_power = {'a': 1, 'b': 2, 'c': 3, 'ba': 10, 'baa': 20}
    char_repeated = {}

    # Checking every character in hack.
    # If the character is other than allowed, function will raise error and stop program.
    for character in hack:
        char_repeated.setdefault(character, 0)
        char_repeated[character] += 1
        if character not in base_power.keys():
            print('Error! Invalid character detected!')
            return 0
        else:
            hack_power += (base_power.get(character) * char_repeated.get(character))

    # This part looks for special phrases in hack
    hack_phrases_found = hack_phrase.findall(hack)

    if hack_phrases_found != 0:
        for phrase in hack_phrases_found:
            hack_power += base_power.get(phrase)

    print('Your hack "' + hack + '" has %d power. \n' % hack_power)


if __name__ == "__main__":
    while 1:
        hack_calculator(input('Enter hack: '))