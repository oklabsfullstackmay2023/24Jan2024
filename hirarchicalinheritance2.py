#1. class defination is one time process
class Person():
    #1. property/variable/state
    #2. constrcutor/esp.method
    #3. method/behaviour/function
    def eat(self):
        print(f'I am eating')
        pass
    def sleep(self):
        print(f'I am sleeping')
        pass
    def walk(self):
        print(f'I am walking')
        pass
    def learn(self):
        print(f'I am learning')
        pass
    pass
class Dancer(Person):
    #1. property/variable/state
    #2. constructor/esp.function
    #3. function/method/behaviour
    def dancing(self):
        print(f'I am dancing')
        pass
    pass
class Programmer(Person):
    #1. property/variable/state
    #2. constructor/esp.function
    #3. function/method/behaviour
    def coding(self):
        print(f'I am coding')
        pass
    pass
class Singer(Person):
    #1. property/variable/state
    #2. constructor/esp.function
    #3. method/function/behaviour
    def singing(self):
        print(f'I am singing')
        pass
    pass

#2 create class external object is many time process
madhuridixit=Dancer()
print(f' {madhuridixit.eat() }')
print(f' {madhuridixit.walk() }')
print(f' {madhuridixit.sleep() }')
print(f' {madhuridixit.learn() }')
print(f' {madhuridixit.dancing() }')

rohit=Programmer()
print(f'{rohit.eat() }')
print(f'{rohit.learn() }')
print(f'{rohit.walk() }')
print(f'{rohit.sleep() }')
print(f'{rohit.coding() }')

arjitsingh=Singer()
print(f'{arjitsingh.eat() }')
print(f'{arjitsingh.walk() }')
print(f'{arjitsingh.learn() }')
print(f'{arjitsingh.sleep() }')
print(f'{arjitsingh.singing() }')