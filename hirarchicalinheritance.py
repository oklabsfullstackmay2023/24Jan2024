#1 class defination is one time process
class Person():
    #1. property/variable/state
    #2. constrcutor/esp.function
    #3. function/behaviour/method
    def eat(self):
        print('I am eating')
        pass
    def sleep(self):
        print('I am sleeping')
        pass
    def learn(self):
        print('I am learning')
        pass
    def walk(self):
        print('I am learning')
        pass
    pass
class Doctor(Person):
    #1. property/state/variable
    #2. constructor/esp.function
    #3. function/method/behaviour
    def checkUp(self):
        print(f"I am checking patient")
        
        pass
    pass
class Teacher(Person):
    #1. property/state/variable
    #2. constructor/esp.function
    #3. function/method/behaviour
    def teach(self):
        print(f'I am teaching students')
        pass
    pass
class Army(Person):
    #1. property/variable/state
    #2. constructor/esp.method
    #3. function/method/behaviour
    def toProtectBorderAndCountry(self):
        print(f'I am protecting border')
        pass   
    pass

#2. create class external object is many time process
drjoshi=Doctor()
print(f"The doctor {drjoshi.eat() }")
print(f"The doctor {drjoshi.walk() }")
print(f"The doctor {drjoshi.sleep() }")
print(f"The doctor {drjoshi.learn() }")

anilsir=Teacher()
print(f'The teacher {anilsir.eat() }')
print(f'The teacher {anilsir.walk() }')
print(f'The teacher {anilsir.sleep() }')
print(f'The teacher {anilsir.learn() }')

premchandmasaji=Army()
print(f'The army {premchandmasaji.eat() }')
print(f'The army {premchandmasaji.walk() }')
print(f'The army {premchandmasaji.sleep() }')
print(f'The army {premchandmasaji.learn() }')
