def main():
    outfile = open("mydata.txt", "w")

    for x in range(1,101):
       print("{0}{1:5}{2:10.3f}".format(x, x**2, x**0.5), file=outfile)


main()
