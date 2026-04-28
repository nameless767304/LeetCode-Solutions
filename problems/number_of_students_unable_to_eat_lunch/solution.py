class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while students and (len(set(students)) == 2 or sandwiches[0] == students[0]):
            student = students.pop(0)
            if sandwiches[0] == student:
                sandwiches.pop(0)
            else:
                students.append(student)

        return len(sandwiches)
        