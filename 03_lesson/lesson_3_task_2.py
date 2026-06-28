from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79219876543"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79315554433"),
    Smartphone("Google", "Pixel 8", "+79412223344"),
    Smartphone("Asus", "Zenfone 10", "+79510001122")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
