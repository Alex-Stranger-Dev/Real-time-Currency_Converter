#Real-time Currency Converter
from colorama import Fore, Back, Style
from colorama import init
from forex_python.converter import CurrencyRates
c = CurrencyRates()
init()
print(Fore.BLACK)
print(Back.GREEN)
amount = int(input("Enter the amount:  "))
from_currency = input("From Currency:  ").upper()
to_currency = input("To Currency:  ").upper()
print(Fore.BLACK)
print(Back.CYAN)
print(from_currency, "  To  ", to_currency, amount) 
result = c.convert(from_currency, to_currency, amount)
print(round(result, 2))


