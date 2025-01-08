class Computer:

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def drive(self):
        print("plmm" + self.p2)

    def degine(self):
        print("plllll" + self.p1)


c1: Computer = Computer("Suri", "Nari")
c1.drive()
c1.degine() 
x = 5
print(x.bit_length)
print(type(x))
print(type(c1))   