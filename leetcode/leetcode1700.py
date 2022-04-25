# ****************************************************************分割线****************************************************************
# todo 1700（Number of Students Unable to Eat Lunch）
# 无法吃午餐的学生数量

from collections import deque

class Solution:
    def countStudents(self, students: list, sandwiches: list) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while len(students) > 0 and not ((students.count(0) == 0 or students.count(1) == 0) and students[0] != sandwiches[0]):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                temp = students.popleft()
                students.append(temp)
        # print("s:{s} f:{f}".format(s=students,f=sandwiches))
        return len(students)

print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
