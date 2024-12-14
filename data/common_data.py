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
