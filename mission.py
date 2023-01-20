'''
 10.8 Element 클래스를 수정해서 name, symbol, number의 속성을
 private로 만든다. 각 속성값을 반환하기 위해 getter 프로퍼티를 정의한다.
'''

class Element():
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, name):
        print('inside the setter')
        self.hidden_name = name
    @property
    def symbol(self):
        print('inside the getter')
        return self.hidden_symbol
    @symbol.setter
    def symbol(self, symbol):
        print('inside the setter')
        self.hidden_symbol = symbol
    @property
    def number(self):
        print('inside the getter')
        return self.hidden_number
    @number.setter
    def symbol(self, number):
        print('inside the setter')
        self.hidden_number = number


produce = Element('Hydrogen', 'H', 1)
produce.name
produce.symbol
produce.number