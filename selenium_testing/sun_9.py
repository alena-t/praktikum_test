class Pats:
    head = 1

    def __init__(self, name, pat_type):
        self.name = name
        self.pat_type = pat_type
        self.tail = 1
        self.has_human = {}

    def set_human(self, human_name, age):
        self.has_human['human_name'] = human_name
        self.has_human['age'] = age

    def get_pat(self):
        return f'A {self.pat_type} {self.name} has ' \
               f'a human {self.has_human.get("human_name")} ' \
               f'with age={self.has_human.get("age")}'


if __name__ == '__main__':
    pat_1 = Pats('Barsik', 'cat')
    pat_1.set_human('Василий', 30)
    pat_2 = Pats('Rex', 'dog')
    pat_2.set_human('John', 24)
    print(pat_1.get_pat())
    print(pat_2.get_pat())
