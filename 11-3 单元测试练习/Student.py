class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise  ValueError
        elif self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 80:
            return 'A'
        else:
            return 'C'
s1 = Student('yyzhu',59)
print(s1.get_grade())