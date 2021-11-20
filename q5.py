def grading():
    n = int(input("Enter grade: "))
    description = ("Fail", "Poor","Fair","Good","Excellent")
    grade = description[n-1]
    print(grade)


grading()


def grading2():
    score = int(input("Enter score: "))

    if score <=100 and score>=90:
        print("A")

    elif score <=89 and score>=80:
        print("B")

    elif score <= 79 and score>=70:
        print("C")

    elif score<=69 and score>=60:
        print("D")

    elif score<=59 and score>=1:
        print("F")

    else:
        print("Invalid score.")



grading2()
