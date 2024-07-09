from smartphone import Smartphone

phone1 = Smartphone("Apple", "15", "+79111111111")
phone2 = Smartphone("Nokia", "Mini", "+79222222222")
phone3 = Smartphone("Honor", "P80", "+79333333333")
phone4 = Smartphone("Samsung", "A+", "+79444444444")
phone5 = Smartphone("HUAWEI", "Nova", "+79555555555")

catalog = [phone1, phone2, phone3, phone4, phone5]

for all in catalog:
    print(f"{all.marka} - {all.model}. {all.number}")
