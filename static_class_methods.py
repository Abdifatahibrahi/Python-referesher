class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"FixedFloat: {self.amount:.2f}"
    @classmethod
    def from_sum(cls, num1, num2):
        return cls(num1 + num2)
    
num1 = FixedFloat(78.985)
num2 = FixedFloat.from_sum(100, 80)
print(num2)

class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f"< Dollar: {self.symbol}{self.amount:.2f} >"
    
usd1 = Dollar(100)
usd2 = Dollar.from_sum(20,10)
print(usd1)
print(usd2)
        
        