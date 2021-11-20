# A program for a simple type of a secret code.

def main():
    sentence = input("Write the sentence you want coded: ")
    for char in sentence:
        code = ord(char)
        coded_char = code + 5
        new_chr = chr(coded_char)
    print(new_chr,end='')


main()
