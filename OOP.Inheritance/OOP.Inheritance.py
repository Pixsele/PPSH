def buying_securities(func):
    def inside_func(obj):
        if obj.echelon == 3:
            print('Это высокорискованная сделка \n')
            return None
        return func(obj)

    return inside_func


class Investments:
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print(f'Тикер : {self.ticker}\nЦена билета : {self.price}{self.currency}\nСектор : {self.industry}')


class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    def display(self):
        dividend_status = 'Да'
        if self.dividend == False:
            dividend_status = 'Нет'
        super().display()
        print(f'Диведенды : {dividend_status}\nЭшелон : {self.echelon}\nГодовая доходность : {self.profit}%\n')

    @buying_securities
    def buying(self):
        if self.profit > 5:
            count = int(input('Количество : '))
            print(f'Успешно приобретено {count} бумаг на сумму {(self.price * count):,.2f} {self.currency}')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    def display(self):
        super().display()
        print(f'Купон : {self.coupon}\nЭшелон : {self.echelon}\nНоминальная стоимость : {self.nominal}\n')

    @buying_securities
    def buying(self):
        if self.price <= self.nominal:
            count = int(input('Количество : '))
            print(f'Успешно приобретено {count} акций на сумму {(self.price * count):,.2f} {self.currency}')


shares = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
bonds = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 3, 3, 1000)

shares.display()
shares.buying()
bonds.display()
bonds.buying()
