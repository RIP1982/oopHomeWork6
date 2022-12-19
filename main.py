class Function:
    sing = ""

    def __init__(self):
        self.x = 0
        self.y = 0

    def set_values(self):
        self.x = float(input("Input X: "))
        self.y = float(input("Input Y: "))

    def get_values(self):
        return self.x, self.y

    def set_sing(self):
        self.sing = input("Input sing('+' '-' '*' '/'): ")

    def get_sing(self):
        return self.sing


    def calc(self):
        s = self.get_sing()
        if s in ('+', '-', '*', '/'):
            x = self.get_values()[0]
            y = self.get_values()[1]
            if s == '+':
                return "%.2f" % (x + y)
            elif s == '-':
                return "%.2f" % (x - y)
            elif s == '*':
                return "%.2f" % (x * y)
            elif s == '/':
                if y != 0:
                    return "%.2f" % (x / y)
                else:
                    return "Divide by zero!"
        else:
            return "Wrong sing!"


simplCalculator = Function()

print("Input zero for exit!")
while True:
    simplCalculator.set_sing()
    s = simplCalculator.get_sing()
    if s == '0':
        break
    simplCalculator.set_values()
    print(simplCalculator.calc())