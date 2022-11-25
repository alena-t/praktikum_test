
class CatForTest:
    date = None

    def __init__(self, name=None, tail=None, age=None):
        self._name = name
        self.__tail = tail
        self.color = {}
        self.mustage = []
        self.age = age

    def date_change(self, date):
        self.date = date
        self.age = date

    def change_name(self, new_name):
        self.name = new_name

    def add_mustage(self, mustage_color):
        self.mustage.append(mustage_color)

    def add_cat_color(self, color, where):
        self.color[where] = color

    def get_cat_colors(self):
        cat_colors = 'Cat have:'
        for key, value in self.color.items():
            cat_colors = cat_colors + value + ' on his' + key
        return cat_colors

    def tail_param(self, param):
        self.__tail = param


class StreetCat(CatForTest):

    def get_mustage(self):
        return self.mustage


cat_1 = CatForTest(name="Tom")
cat_1._name = "Jery"
cat_2 = CatForTest()
cat_2._name = "Barsik"
cat_2.change_name("Pushok")
cat_1.add_cat_color("orange", "left_side")
cat_1.add_cat_color("white", "right_side")
# cat_colors = cat_1.get_cat_colors()
print(cat_1.get_cat_colors())

cat_3 = StreetCat()
cat_3.name = "Persik"
