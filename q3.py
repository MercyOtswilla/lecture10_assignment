def main():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    product =  first_num * second_num
    
    for digit in str(product):
        print(digit)


main()
