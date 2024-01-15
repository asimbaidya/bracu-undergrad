# --Task 01: solution-------------------------------
# q1: 16min done
def bux_encoder(word, index, rand_number):
    if index == len(word):
        return word

    e_ch = ord(word[index]) + rand_number
    # if e_ch > 122: # lower casee
    if e_ch > 90:  # upper case
        e_ch -= 26
    e_ch = chr(e_ch)
    word = word[:index] + e_ch + word[index + 1 :]
    return bux_encoder(word, index + 1, rand_number)


# --Task 02: On paper-------------------------------
# --Task 03: On paper-------------------------------

if __name__ == "__main__":
    # task 1 test
    random_number = 20301239 % 26

    word = input("Enter a word: ")
    random_number = int(input("test_random_number: "))

    encoded_word = bux_encoder(word, 0, random_number)
    print(encoded_word)
