class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lection(self, mentor, course, grade):
        if  isinstance(mentor, Lecturer) \
            and course in mentor.courses_attached \
            and course in self.courses_in_progress \
            and grade in range(1,11,1):
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def avg_grade(self):
        sum_grades = 0
        num_graders = 0
        for grade in self.grades.values():
            sum_grades += sum(grade)
            num_graders += len(grade)
        return sum_grades / num_graders
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за домашние задания: {self.avg_grade():.1f}\n'\
        f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"\
        f"Завершенные курсы: {', '.join(self.finished_courses)}"
    
best_student = Student ('Sasha', 'Ryzhik', 'male')
print (best_student)