
class Student:
    def __init__(self, name, score):
        self.name = name;
        self.score = score;

    def ex_score(self):
        print(self.name,'的分数是：',self.score)


s1 = Student('张三', '80')
s1.ex_score()