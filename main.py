class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
                 self.name = name
                 self.age = age
                 self.track = track
                 self.score = score
                 print("my name is", name, "and I am age", age, "my track is", track, "my current score is", score) 
        def speak(self):
        pass
    d = student("Tunde", 24, "Python", 12.5)
    #methods
    class student(*args):
    def change_name(self, args):
        
        self.args = Bob.change_name()
        self.args = Bob.change_age()
        self.args = Bob.change_track()
        self.args = Bob.get_score()
    def get_input(self args):
        self_args = self.args("change name", "change age", "add track" "get score")
         print(self.args)
         get_input()


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
