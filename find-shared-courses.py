"""
You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
"""

"""
student_course_pairs_1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]
"""


# 58 has any class that is same as 9$????
# YES! EC!


def shared_courses(courses):

    dictionary = {}
    # iterate through the list 
    # create a dic with the students ID as key and courses as values
    # dict = {58: LA, ME, EC, SD, 94: AH, OP, EC}

    for key, value in courses:
        if key not in dictionary:
            dictionary[key] = value
        dictionary[key] = value
    print(dictionary)



shared_courses([
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
])









def findSharedCourses(student_course_pairs):
    #dict to store student courses
    student_courses = {}

    #create a 
    for student, course in student_course_pairs:
        if int(student) not in student_courses:
            student_courses[int(student)] = set()
        student_courses[int(student)].add(course)
    ans = {}
    for s1, c1 in student_courses.items():
        for s2, c2 in student_courses.items():
            if s1 == s2 or tuple(sorted((s1, s2))) in ans:
                continue
            ans[tuple(sorted((s1, s2)))] = sorted(c1.intersection(c2))
    return ans

print(findSharedCourses([
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
]))
