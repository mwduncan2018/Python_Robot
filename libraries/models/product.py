from dataclasses import dataclass

@dataclass
class Product:
    id: str = ""
    manufacturer: str = ""
    model: str = ""
    price: str = ""
    number_in_stock: str = ""

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("Id"),
            manufacturer=data.get("Manufacturer"),
            model=data.get("Model"),
            price=data.get("Price"),
            number_in_stock=data.get("NumberInStock")
        )