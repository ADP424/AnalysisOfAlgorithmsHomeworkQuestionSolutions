def max_registered_students(num_students, num_courses, student_courses, course_limits):
    # initialize list mapping each course to interested students
    course_interests = [set() for _ in range(num_courses)]
    for i in range(num_students):
        for course in student_courses[i]:
            course_interests[course - 1].add(i)

    # sort courses in descending order of enrollment limit
    sorted_courses = sorted(range(1, num_courses + 1), key=lambda x: course_limits[x - 1], reverse=True)

    # assign students to courses based on preferences and availability
    num_registered = 0

    # keep track of assigned courses
    assigned_courses = [set() for _ in range(num_students)]
    for course in sorted_courses:
        # remove spot from enrollment possibility
        num_spots = course_limits[course - 1]
        interested_students = sorted(list(course_interests[course - 1]), key=lambda x: len(student_courses[x]))
        for student in interested_students:
            if num_spots > 0 and len(assigned_courses[student]) < 3:
                num_spots -= 1
                assigned_courses[student].add(course)
                num_registered += 1

    return num_registered

def main():
    # read input and set number of students, courses, etc.
    students_and_courses = input().split()
    num_students = int(students_and_courses[0])
    num_courses = int(students_and_courses[1])

    student_courses = [set(map(int, input().split())) for _ in range(num_students)]
    course_limits = [int(input()) for _ in range(num_courses)]

    # call function and print output
    max_registered = max_registered_students(num_students, num_courses, student_courses, course_limits)
    print(max_registered)

main()