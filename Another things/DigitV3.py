'''dadad'''
def text_to_number(text: str) -> int:
    '''dadaadadad'''
    num_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    tokens = text.split()
    total_sum = 0
    current_thousand = 0
    current_section = 0

    i = 0
    while i < len(tokens):
        word = tokens[i]
        if word == "thousand":
            current_thousand = (
                current_section if current_section else 1
            ) * 1000
            total_sum += current_thousand
            current_section = 0
        elif word == "hundred":
            current_section *= 100
        else:
            current_section += num_words[word]
        i += 1

    total_sum += current_section
    return total_sum


input_text = input()
print(text_to_number(input_text))
