from smartphone import Smartphone
catalog = [ ]
phone1 = Smartphone("Samsung", "4567", "+79530958921")
phone2 = Smartphone("Tecno", "900", "+79530958920")
phone3 = Smartphone("Motorola", "789", "+79530958919")
phone4 = Smartphone("Apple", "456", "+79530958001")
phone5 = Smartphone("Fly", "567", "+79530958821")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")