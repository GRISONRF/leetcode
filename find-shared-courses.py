"""
You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
"""

""" Sample Input:
student_course_pairs_1 = [
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
]
 
Sample Output (pseudocode, in any order):
 
find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
} """



# return as list of ID and course pairs
# return list of all courses they share with friends

# dict: studentID key and courses value
#{ 58: SWE, LA, ME, EC; 94: AH, OS}

#ans = {}
#check every id with the others (nested loop)
#check if the pair is already in dict (need to sort them before adding to the dict so it makes it easier to know if they are already added) and use intersection to find the courses they share. To use intersection the courses need to be in a set, so it's better to already add them as a set in the first fictionary when I'm creating it.




def shared_courses(courses):

    students_courses = {}
    for id, course in courses:
        if id not in students_courses:
            students_courses[students_courses]

print(shared_courses([
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
]))



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
