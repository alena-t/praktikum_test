class TestCat:

    def __init__(self, color, ears, tail):
        self.tail = tail
        self.head = 1
        self.color = color
        self.ears = ears
        self.paws = 4



class TestDog(TestCat):

    def change_color(self, new_colore):
        self.color = new_colore


cat_1 = TestCat("yellow", 2, 1)
dog_1 = TestDog("brown", 2, 2)
cat_1.set_color("orange")
dog_1.set_color("black")
dog_1.change_color("red")
