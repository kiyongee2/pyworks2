# Person 클래스 생성 -> Employee 클래스 (상속관계)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 상속 - 클래스이름(부모클래스)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)       # 부모의 멤버 생성(상속) - super() 사용
        self.employee_id = employee_id    # 자신의 멤버 생성

    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 사번 : {self.employee_id}')


p = Person("김강", 62)
print(p.name)

# Employee 인스턴스(emp) 생성
emp = Employee("김산", 31, 100)
emp.info()

