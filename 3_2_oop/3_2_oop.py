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
    
    def __lt__(self, other):
        return self.__avg_grade() < other.__avg_grade()
    
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
    
    def __lt__(self, other):
        return self.__avg_rate() < other.__avg_rate()
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за лекции: {self.__avg_rate():.1f}'

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
        
best_student = Student('Ruoy', 'Eman', 'male')
second_student = Student('John', 'Travolta', 'male')

bad_mentor = Lecturer('Alex', 'Terrible')
sad_mentor = Lecturer('Alex', 'Turner')

bad_reviewer = Reviewer('Juliy', 'Gusman')
sad_reviewer = Reviewer('Judge', 'Dredd')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
best_student.finished_courses += ['SQL']
second_student.finished_courses += ['SQL']

bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Java']
sad_reviewer.courses_attached += ['Python']
sad_reviewer.courses_attached += ['Java']
bad_mentor.courses_attached += ['Python']
bad_mentor.courses_attached += ['Java']
sad_mentor.courses_attached += ['Python']
sad_mentor.courses_attached += ['Java']
best_student.rate_lection(bad_mentor, 'Python', 2)
best_student.rate_lection(sad_mentor, 'Java', 10)

bad_reviewer.rate_hw(best_student, 'Python', 10)
sad_reviewer.rate_hw(second_student, 'Java', 2)

print(best_student)
print(best_student > second_student)
print(bad_mentor)
print(bad_mentor > sad_mentor)
print(bad_reviewer)
def avg_hw_course(student_list, course):
    sum_rate = 0
    num_rate = 0
    for student in student_list:
        sum_rate += sum(student.grades.get(course, {}))
        num_rate += len(student.grades.get(course, {}))
    return sum_rate / num_rate

student_list = [best_student, second_student]
print (avg_hw_course(student_list, 'Python'))

def avg_lecture_rate(lector_list, course):
    sum_rate = 0
    num_rate = 0
    for lecturer in lecturer_list:
        sum_rate += sum(lecturer.grades.get(course, {}))
        num_rate += len(lecturer.grades.get(course, {}))
    return sum_rate / num_rate

lecturer_list = [bad_mentor, sad_mentor]
print(avg_lecture_rate(lecturer_list, 'Python'))