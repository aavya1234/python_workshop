class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        return  "woof!"
class cat(animal):
    def speak(self):
        return  "meow!"
dog=dog("buddy")
cat=cat("whiskers")
print(dog.name,dog.speak())
print(cat.name,cat.speak())