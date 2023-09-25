##Сортируется сначала по редкости(т.к. такой вид сортировки я чаще использовал в играх), потом по цене, потом по цвету(никогда такого не видел ¯\_(ツ)_/¯)
## и в конце по id(т.к обычно игроки не видят id предметов, и важны разработчику, нежели игроку)

class Item:
    def __init__(self, ID, price, rarity, color, name):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color
        self.name = name

    def __eq__(self, other):
        if self.rarity == other.rarity and self.price == other.price and self.color == other.color and self.ID == other.ID:
            return True
        else:
            return False
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.rarity > other.rarity:
            return True
        if self.rarity < other.rarity:
            return False
        if self.price > other.price:
            return True
        if self.price < other.price:
            return False
        if self.color < other.color:
            return True
        if self.color > other.color:
            return False
        if self.ID < other.ID:
            return True
        if self.ID > other.ID:
            return False
    def __gt__(self, other):
        return not self < other

    def __le__(self, other):
        return self == other or self < other
    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        return f'{self.name}'


book = Item(1,150,0,'#8B4513','Book')
sword = Item(2,1000,3,'	#C0C0C0','Sword')
helmet = Item(3,500,2,'#000000','Helmet')

test_massive = [book,sword,helmet]
test_massive.sort()
print(*test_massive)