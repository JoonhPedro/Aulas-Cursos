class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b 


    def subtracao(self):
        return self.valor_a - self.valor_b 


    def multiplacacao(self):
        return self.valor_a * self.valor_b 


    def divisao(self):
        return self.valor_a / self.valor_b 

if __name__ == '__main__':
    calculadora = Calculadora(10, 5)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplacacao())
    
    #class Calculadora:

    #def soma(self, valor_a, valor_b):
    #   return valor_a + valor_b

    #def subtracao(self, valor_a, valor_b):
    #    return valor_a - valor_b

    #def multiplacacao(self, valor_a, valor_b):
    #    return valor_a * valor_b

    #def divisao(self, valor_a, valor_b):
    #    return valor_a / valor_b


    #calculadora = Calculadora()
    #print(calculadora.soma(10, 2))
    #print(calculadora.subtracao(5, 3))
    #print(calculadora.divisao(100, 2))
    #print(calculadora.multiplacacao(10, 5))