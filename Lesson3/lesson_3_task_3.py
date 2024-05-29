from address import Address
from mailing import Mailing

adress_to = Address(170100, "Tver", "Smolenskaya", 9, 25)
adress_from = Address(141200, "Moscow", "Tverskaya", 25, 895)
mailing_1 = Mailing(adress_to, adress_from, 258.6, "RF2025841254")

# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
print(f"Отправление {mailing_1.track} из {adress_from.index}, {adress_from.city}, {adress_from.street}, {adress_from.building} - {adress_from.apartment}."
      f"Стоимость {mailing_1.cost} рублей")
