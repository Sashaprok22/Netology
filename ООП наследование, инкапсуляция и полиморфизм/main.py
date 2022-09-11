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

    def get_averge_rate(self):
        rates_count = 0
        rates_sum = 0

        for grades in self.grades.values():
            rates_count += len(grades)
            rates_sum += sum(grades)

        return rates_sum / rates_count if rates_count > 0 else "N/A"

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

    def get_averge_rate(self):
        rates_count = 0
        rates_sum = 0

        for grades in self.courses_grades.values():
            rates_count += len(grades)
            rates_sum += sum(grades)

        return rates_sum / rates_count if rates_count > 0 else "N/A"


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

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

lecturer = Lecturer("Name", "Surname")
lecturer.courses_attached += ['Python']

best_student.rate_lecture(lecturer, "Python", 7)

student = Student('1', '2', 'your_gender')
student.courses_in_progress += ['Python']
 
cool_mentor.rate_hw(student, 'Python', 7)
cool_mentor.rate_hw(student, 'Python', 6)
cool_mentor.rate_hw(student, 'Python', 10)
 
print(lecturer == lecturer)