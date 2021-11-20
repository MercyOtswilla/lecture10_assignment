# table x- 1 to 10, x^2, 1/x

def main():
    for x in range(1,11):
        print("{0}\t{1}\t{2:0.3f}".format(x, 2**x, 1/x))


main()
