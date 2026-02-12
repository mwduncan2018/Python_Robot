from dataclasses import dataclass

@dataclass
class WatchListEntry:
    id: str = ""
    manufacturer: str = ""
    model: str = ""

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("Id"),
            manufacturer=data.get("Manufacturer"),
            model=data.get("Model")
        )