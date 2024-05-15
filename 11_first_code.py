class Cat:
    head = 1
    tail = 1

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def say_meow(self):
        print(f'{self.name} сказал МЯУ!')

    def change_colour(self, colour):
        self.colour = colour



if __name__ == '__main__':
    cat = Cat('Негодяй', 'полосатый')
    cat_1 = Cat('Пушок', 'белый')
    cat.say_meow()
    cat_1.say_meow()
    cat.change_colour('черный')
    print(cat.colour)
    print(cat_1.colour)

