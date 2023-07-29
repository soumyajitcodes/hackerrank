if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_list.append([name, score])

    min_grade = float("inf")
    grade_list = []

    for entry in student_list:
        grade_list.append(entry[1])

    for grade in grade_list:
        if grade != min(grade_list) and grade < min_grade:
            min_grade = grade

    student_list.sort()

    for student in student_list:
        if student[1] == min_grade:
            print(student[0])
