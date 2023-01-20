'''
10.4 name, symbol, number 인스턴스 속성 가진
 Element 클래스를 만들어보자.
 이 클래스에서 'Hydrogen', 'H', 1 값을 가진 객체를 생성한다.

'''

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

produce = Element('Hydrogen', 'H', 1)
print(produce.name, produce.symbol, produce.number)

'''
10.5 'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1과 같이
 키와 값으로 이루어진 el_dict 딕셔너리를 만들어보자.
 그리고 el_dict 딕셔너리로부터 Element 클래스의 hydrogen 객체를 생성한다.
'''

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name, hydrogen.symbol, hydrogen.number)
