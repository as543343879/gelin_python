from enum import auto, Enum

import typing


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        """ 自动用name的小写配置成value, 否则auto()会用整数1~xxx配置成value """
        return name.lower()


class ProviderType(AutoName):
    """ 云供应商类型 """
    LZ = auto()
    ALIYUN = auto()
    AWS = auto()
    HUAWEI = auto()
    TENCENT = auto()
    UCLOUD = auto()

    @staticmethod
    def from_str(_type: typing.Union[str, "ProviderType"]) -> "ProviderType":
        if isinstance(_type, str):
            return ProviderType[_type.upper()]
        return 0

t = ProviderType.from_str('LZ')
print(t.name,t.value)

