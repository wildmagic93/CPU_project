class CPU():
    def __init__(self):
        self.registry = ['', '', '', '']
        self.addresses = []

    def load_data(self, num1, num2 = ''):
        data = [num1, num2]
        count = 0
        for i in range(len(self.registry)):
            if (self.registry[i] == '' and count < 2):
                self.registry[i] = data[count]
                self.addresses.append(i)
                count += 1
        if count != 2:
            self.registry[0] = num1
            self.addresses.append(0)
            self.registry[1] = num2
            self.addresses.append(1)
    
    def read(self, position):
        return self.registry[position]

    def flush_addresses(self):
        self.registry[self.addresses[0]] = ''
        self.registry[self.addresses[1]] = ''
        self.addresses = []

    def add(self, num1, num2):
        self.load_data(num1, num2)
        x = self.registry[self.addresses[0]]
        y = self.registry[self.addresses[1]]
        self.flush_addresses()
        z = x + y
        self.load_data(z)
        return z

    def subtract(self, num1, num2):
        self.load_data(num1, num2)
        x = self.registry[self.addresses[0]]
        y = self.registry[self.addresses[1]]
        self.flush_addresses()
        z = x - y
        self.load_data(z)
        return z

    def multiply(self, num1, num2):
        self.load_data(num1, num2)
        x = self.registry[self.addresses[0]]
        y = self.registry[self.addresses[1]]
        self.flush_addresses()
        z = x * y
        self.load_data(z)
        return z

    def divide(self, num1, num2):
        self.load_data(num1, num2)
        x = self.registry[self.addresses[0]]
        y = self.registry[self.addresses[1]]
        self.flush_addresses()
        z = x / y
        r = x % y
        self.load_data(z, r)
        return (z, r)

prova = CPU()
print(prova.add(3,4))
