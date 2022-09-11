class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        rows = [
            f"Имя: {self.name}",
            f"Фамилия: {self.surname}",
            f"Средняя оценка за домашние задания: {self.get_averge_rate()}",
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}",
            f"Завершенные курсы: {', '.join(self.finished_courses)}",

        ]
        return "\n".join(rows)

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.get_averge_rate() < student.get_averge_rate()

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.get_averge_rate() == student.get_averge_rate()

    def get_averge_rate(self, course=None):
        rates_count = 0
        rates_sum = 0

        for c_course, grades in self.grades.items():
            if course is not None:
                if course == c_course:
                    rates_count += len(grades)
                    rates_sum += sum(grades)
            else:
                rates_count += len(grades)
                rates_sum += sum(grades)

        return rates_sum / rates_count if rates_count > 0 else 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_averge_rate()}"
    
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_averge_rate() < lecturer.get_averge_rate()

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.get_averge_rate() == lecturer.get_averge_rate()

    def get_averge_rate(self, course=None):
        rates_count = 0
        rates_sum = 0

        for c_course, grades in self.courses_grades.items():
            if course is not None:
                if course == c_course:
                    rates_count += len(grades)
                    rates_sum += sum(grades)
            else:
                rates_count += len(grades)
                rates_sum += sum(grades)

        return rates_sum / rates_count if rates_count > 0 else 0


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

 
lecturer1 = Lecturer("Lecturer", "1")
lecturer1.courses_attached += ["Python"]

lecturer2 = Lecturer("Lecturer", "2")
lecturer2.courses_attached += ["Python"]

reviewer = Reviewer("Reviewer", "1")
reviewer.courses_attached += ["Python"]

student1 = Student("Student", "1", "gender")
student1.courses_in_progress += ["Python"]

student2 = Student("Student", "2", "gender")
student2.courses_in_progress += ["Python"]

reviewer.rate_hw(student1, "Python", 3)
reviewer.rate_hw(student1, "Python", 6)

reviewer.rate_hw(student2, "Python", 7)
reviewer.rate_hw(student2, "Python", 2)

student1.rate_lecture(lecturer1, "Python", 5)
student1.rate_lecture(lecturer2, "Python", 10)

student2.rate_lecture(lecturer2, "Python", 1)
student2.rate_lecture(lecturer1, "Python", 5)

print(lecturer1)
print(reviewer)
print(student1)

print(lecturer1 > lecturer2)
print(student1 < student2)

def get_students_averge_rate(students, course):
    rates_sum = 0
    rates_count = 0

    for student in students:
        rates_count += 1
        rates_sum += student.get_averge_rate(course)

    return rates_sum / rates_count if rates_count > 0 else 0

def get_lecturers_averge_rate(lecturers, course): # Абсолютно идентичная функция с предыдущей)
    rates_sum = 0
    rates_count = 0

    for lecturer in lecturers:
        rates_count += 1
        rates_sum += lecturer.get_averge_rate(course)

    return rates_sum / rates_count if rates_count > 0 else 0

print(get_students_averge_rate([student1, student2], "Python"))
print(get_lecturers_averge_rate([lecturer1, lecturer2], "Python"))