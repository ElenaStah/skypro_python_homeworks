
from mailing import Mailing
from address import Address


to_address = Address(350042, "Краснодар", "Механическая", 21, 2)
from_address = Address(350000, "Краснодар", "Механическая", 20, 2)

mailing = Mailing(to_address, from_address, 500, 6588900)

print(f"Отправление { mailing.track} из {mailing.from_address.индекс}, {mailing.from_address.город}, " 
    f"{mailing.from_address.улица},  {mailing.from_address.дом} - {mailing.from_address.квартира}"
    f" в {mailing.to_address.индекс}, {mailing.to_address.город}, {mailing.to_address.улица},"
    f"  {mailing.to_address.дом} - {mailing.to_address.квартира}. Стоимость {mailing.cost} рублей.")
    