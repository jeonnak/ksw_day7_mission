'''
 10.7 print(hydrogen)을 호출한다. Element 클래스의 정의에서 dump 메서드를
 __str__() 메서드로 바꿔서 새로운 hydrogen 객체를 생성하고,
 그리고 print(hydrogen)을 다시 호출한다.
'''

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])

print(hydrogen)