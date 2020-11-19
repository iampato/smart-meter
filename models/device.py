
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class MeterDevice:
    id: str
    model_no: str
    manufacturer: str

    def __init__(self, id: str, model_no: str, manufacturer: str) -> None:
        self.id = id
        self.model_no = model_no
        self.manufacturer = manufacturer

    @staticmethod
    def from_dict(obj: Any) -> 'MeterDevice':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        model_no = from_str(obj.get("model_no"))
        manufacturer = from_str(obj.get("manufacturer"))
        return MeterDevice(id, model_no, manufacturer)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["model_no"] = from_str(self.model_no)
        result["manufacturer"] = from_str(self.manufacturer)
        return result


def meter_device_from_dict(s: Any) -> MeterDevice:
    return MeterDevice.from_dict(s)


def meter_device_to_dict(x: MeterDevice) -> Any:
    return to_class(MeterDevice, x)