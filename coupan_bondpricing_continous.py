from math import exp


class coupan_bond:

    def __init__(self, rate, principal, maturity, interest_rate):
        self.rate = rate/100
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate/100


    def present_value(self, x, n):
        return   x / exp(self.interest_rate * n)


    def calculate_price(self):
        price = 0
        for t in( 1, self.maturity+1):
            price = price + self.present_value(self.principal*self.rate, t)

        price = price + self.present_value(self.principal, self.maturity)

        return price

if __name__ == '__main__':

    bond = coupan_bond(10, 1000, 3, 4)
    print(bond.calculate_price())

