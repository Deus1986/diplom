import dataclasses
from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def services_names(cls):
        services_names = [member.value for service, member in cls.__members__.items()]
        return services_names


class Services(BaseEnum):
    service_name_1 = "МегаКино"
    service_name_2 = "Онлайн‑кинотеатр START"
    service_name_3 = "Ева"
    service_name_4 = "МегаФон Музыка"
    service_name_5 = "Приложение"
    service_name_6 = "МегаФон Технологии"


@dataclasses.dataclass
class Product:
    brand: str
    name: str
    amount: int
    amount_2: int
    good_id: int
    price: int


tablet_samsung = Product('Samsung', 'Samsung Galaxy Tab S6 Lite 64GB LTE 2024 Серый', 5, 3, 185238, 32499)


@dataclasses.dataclass
class Store:
    branch_id: int
    city_id: int
    contact_phone: str
    region_id: int
    region_name: str
    eshop_id: int


st_petersburg_store = Store(14, 1834, '+7 (812) 949 1010', 260, 'Санкт-Петербург', 27)
