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
        
    def __avg_grade(self):
        sum_grades = 0
        num_graders = 0
        for grade in self.grades.values():
            sum_grades += sum(grade)
            num_graders += len(grade)
        return sum_grades / num_graders
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за домашние задания: {self.__avg_grade():.1f}\n'\
        f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"\
        f"Завершенные курсы: {', '.join(self.finished_courses)}"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __avg_rate(self):
        sum_rates = 0
        count_rates = 0
        for lecture in self.courses_attached:
            sum_rates += sum(self.grades.get(lecture, {}))
            count_rates += len(self.grades.get(lecture, {}))
        return sum_rates / count_rates
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за лекции: {self.__avg_rate():.1f}\n'
        
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
            and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
        
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

print(best_student.courses_in_progress)
bad_mentor = Lecturer('Alex', 'Terrible')
bad_mentor.courses_attached += ['Python']
bad_mentor.courses_attached += ['Java']
best_student.rate_lection(bad_mentor, 'Python', 2)
print(bad_mentor.courses_attached)
# bad_mentor.rate_hw (best_student, 'Python', 10)
# bad_mentor.rate_hw (best_student, 'Java', 4)
print(bad_mentor)



# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Java']

# bad_student = Student('R', 'Kelly', 'female')
# bad_student.courses_in_progress += ['SQL']
# bad_student.courses_in_progress += ['C++']


# cool_mentor = Lecturer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_lector = Lecturer('Hannibal', 'Lector')
# cool_lector.courses_attached += ['Java']
# cool_lector.courses_attached += ['SQL']


# bad_mentor = Reviewer('Alex', 'Terrible')
# bad_mentor.rate_hw (best_student, 'Python', 10)
# bad_mentor.rate_hw (best_student, 'Java', 4)
# best_student.rate_lection (cool_mentor, 'Python', 10)
# best_student.rate_lection (cool_lector, 'Java', 5)
# bad_student.rate_lection (cool_lector, 'SQL', 9)
# bad_student.rate_lection (cool_lector, 'C++', 8)
# bad_mentor.courses_attached += ['Python']
# bad_mentor.courses_attached += ['Java']
# # print(cool_mentor.grades)
# # print(best_student.name + 'a')
# print(bad_mentor.courses_attached)
 
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(cool_mentor.courses_attached)
# print(isinstance(cool_mentor, Lecturer))
# print(cool_mentor.courses_attached)
# print('Python' in best_student.courses_in_progress )
# print(1 in range(1,11,1))