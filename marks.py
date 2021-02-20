def tuple_of_marks(n):
    tup = ()
    for i in range(n):
        subject = ["maths", "physics", "computer", "english", "hindi"]
        sum = 0
        tup_student = ()
        for j in range(5):
            marks = input("Enter the marks in: {0}".format(subject[j]))
            tup_student = tup_student + (marks,)
            sum += int(marks)
        tup_student = tup_student + (sum,)
        tup = tup + (tup_student,)
    return tup

# print(tuple_of_marks(2))
dic = {'name': 'akash', 'age': 34, 'height': 5.9}

ls_stu1 = [12, 20, 30, 10, 100, 30, 23, 20]

# for mark in ls_stu1:
#     if mark == 100:
#         print("You scored a perfect 100!!")
#         break
#     else:
#         print("not for this subject")


# def perfect_hundred(ls):
#     for m in ls:
#         if m == 100:
#             print("You scored a perfect 100!!")
#             return
#     print("Sorry, you didn't make a perfect hundred!")
#
# perfect_hundred([12, 20, 30, 10, 10, 30, 23, 20])




