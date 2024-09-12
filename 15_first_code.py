class TestCat:

    def __init__(self, name):
        self.head = 1
        self.paws = {}
        self.tail = []
        self.name = name

    def play_with_cat(self):
        return f'{self.name} meow'

    def say_meow(self):
        return f'{self.name} Meow-Meow'


if __name__ == '__main__':
    cat = TestCat('Барсик')
    cat_2 = TestCat('Пушок')
    cat.tail = 0

    print(cat.name)
    print(cat.tail)
    print(cat_2.name)
    print(cat_2.tail)
    print(cat.play_with_cat())
    print(cat_2.say_meow())
