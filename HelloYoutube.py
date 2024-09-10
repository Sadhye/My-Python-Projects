class FractionSimplifier:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def hcf(self, x, y):
        hcf = 1
        if x < y:
            smaller = x
        elif x > y:
            smaller = y
        else:
            return x
        for i in range(1, smaller + 1):
            if x % i == 0 and y % i == 0:
                hcf = i
        return hcf

    def simplify_fraction(self):
        hcf_value = self.hcf(self.numerator, self.denominator)
        simplified_numerator = self.numerator / hcf_value
        simplified_denominator = self.denominator / hcf_value
        return simplified_numerator, simplified_denominator

    def __str__(self):
        simplified_numerator, simplified_denominator = self.simplify_fraction()
        return f"{self.numerator}/{self.denominator} simplified is {int(simplified_numerator)}/{int(simplified_denominator)}"

fraction = FractionSimplifier(5, 10)
print(fraction)