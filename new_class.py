class TestCat:
    lapki = 4

    def __init__(self, colore, ears, tail):
        self.tail = tail
        self.head = 1
        self.mustage = 10
        self.colore = colore
        self.ears = ears

    def set_mustages(self, mustage_count):
        self.mustage = mustage_count


class TestDog(TestCat):

    def change_colore(self, new_colore):
        self.colore = new_colore


cat_1 = TestCat("yellow", 2, 1)
dog_1 = TestDog("brown", 2, 2)
cat_1.set_mustages(7)
dog_1.set_mustages(8)
dog_1.change_colore("red")
