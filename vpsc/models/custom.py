from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class UpdateServer(BaseModel):
    name: str = Field(..., description="""名前""")
    description: str = Field(..., description="""説明""")


class ShutdownServer(BaseModel):
    force: bool = Field(False, description="""強制停止を行うか""")


class UpdateNfsServer(BaseModel):
    name: str = Field(..., description="""名前""")
    description: str = Field(..., description="""説明""")


class UpdateHost(BaseModel):
    hostname: str = Field(..., description="""ホスト名""", examples=["example.jp"])


class CreateSwitch(BaseModel):
    name: str = Field(..., description="""名前""")
    description: str = Field(..., description="""説明""")
    zone_code: Literal["tk2", "tk3", "os3", "is1"] = Field(..., description="""ゾーンコード""")


class UpdateSwitch(BaseModel):
    name: str = Field(..., description="""名前""")
    description: str = Field(..., description="""説明""")


class UpdateNfsServerIpv4(BaseModel):
    address: str = Field(..., description="""アドレス""", examples=["198.51.100.2"])
    netmask: str = Field(..., description="""サブネットマスク""", examples=["255.255.254.0"])


class Ptr(BaseModel):
    ptr: str = Field(..., description="""逆引きホスト名""", examples=["example.jp"])


server_sort_query = Literal[
    "service_code",
    "-service_code",
    "name",
    "-name",
    "storage_size_gibibytes",
    "-storage_size_gibibytes",
    "memory_mebibytes",
    "-memory_mebibytes",
    "cpu_cores",
    "-cpu_cores",
    "hostname",
    "-hostname",
    "ipv6_hostname",
    "-ipv6_hostname",
    "ipv4_address",
    "-ipv4_address",
    "ipv6_address",
    "-ipv6_address",
    "zone_code",
    "-zone_code",
    "ipv4_ptr",
    "-ipv4_ptr",
    "ipv6_ptr",
    "-ipv6_ptr",
]
