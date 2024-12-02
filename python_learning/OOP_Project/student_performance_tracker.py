from typing import List, Dict

class Student:
    def __init__(self, name: str, scores: List[int]):
        self.name = name
        self.scores = scores

    def calculate_average(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def is_passing(self) -> bool:
        return all(score >= 40 for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, name: str, scores: List[int]):
        if name in self.students:
            print(f"{name} is already in the system.")
        else:
            self.students[name] = Student(name, scores)

    def calculate_class_average(self) -> float:
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students) if self.students else 0

    def display_student_performance(self):
        if not self.students:
            print("No student data available.")
            return
        print("Student Performance Summary:")
        for student in self.students.values():
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name}, Subjects: {self.scores_to_str(student.scores)}, "
                  f"Average Score: {avg:.2f}, Status: {status}")

    def scores_to_str(self, scores: List[int]) -> str:
        subjects = ['Math', 'Science', 'English', 'History', 'Geography', 'Computer']
        return ", ".join([f"{subjects[i]}: {scores[i]}" for i in range(len(scores))])

    def get_student_names(self) -> List[str]:
        """Returns a list of student names."""
        return list(self.students.keys())

    def get_student_data(self, name: str) -> str:
        """Returns the performance summary of a specific student."""
        if name in self.students:
            student = self.students[name]
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            return f"Student: {student.name}, Subjects: {self.scores_to_str(student.scores)}, " \
                   f"Average Score: {avg:.2f}, Status: {status}"
        else:
            return f"Student {name} not found in the system."
