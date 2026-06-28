from address import Address
from mailing import Mailing
address_from = Address("101000", "Москва", "Тверская", "7", "12")
address_to = Address("190000", "Санкт-Петербург", "Невский пр.", "25", "4")
parcel = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=450,
    track="RU123456789"
)
print(
    f"Отправление {parcel.track} из "
    f"{parcel.from_address.index}, {parcel.from_address.city}, {parcel.from_address.street}, "
    f"{parcel.from_address.house} - {parcel.from_address.apartment} в "
    f"{parcel.to_address.index}, {parcel.to_address.city}, {parcel.to_address.street}, "
    f"{parcel.to_address.house} - {parcel.to_address.apartment}. "
    f"Стоимость {parcel.cost} рублей."
)
