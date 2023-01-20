'''
 10.6 Element 클래스에서 객체의 속성(name, symbol, number) 값을
 출력하는 dump() 메서드를 정의한다. 이 클래스의 hydrogen 객체를
 생성하고, dump() 메서드로 이 속성을 출력한다.
'''


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.dump()