from Mailing import Mailing
from Address import Address

to_address = Address("111111", "г.Москва", "ул.Московская", "д.111", "кв.11")
from_address = Address("222222", "г.Санкт-Петербург", "ул.Питерская", "д.222",
                       "кв.22")
mailing = Mailing(to_address, from_address, 1122, "станция Ховрино")

print(f"Отправление {mailing.track} из {
    mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {
          mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {
          mailing.to_address.street}, "
      f"{mailing.to_address.house} - {
          mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")
