# generated by datamodel-codegen
# datamodel-codegen --input ./openapi.json --input-file-type openapi --output-model-type pydantic_v2.BaseModel --enum-field-as-literal all --reuse-model --target-python-version 3.8 --output models.py

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import AnyUrl, BaseModel, Field, RootModel


class Pagination(BaseModel):
    count: int = Field(..., description="データ総数", examples=[100])
    next: AnyUrl = Field(..., description="次のページへのURL", examples=["https://api.example.com/?page=3&perpage=10"])
    previous: AnyUrl = Field(..., description="前のページへのURL", examples=["https://api.example.com/?perpage=10"])


class InvalidParameterDetailItem(BaseModel):
    code: Optional[str] = Field(None, description="エラー内容を示す簡潔な識別子", examples=["required"])
    message: Optional[str] = Field(None, examples=["この項目は必須です"])


class InvalidParameterDetail(RootModel[List[InvalidParameterDetailItem]]):
    root: List[InvalidParameterDetailItem]


class Errors(BaseModel):
    non_field_errors: Optional[InvalidParameterDetail] = None


class ProblemDetails400(BaseModel):
    code: Optional[Literal["invalid", "parse_error", "bad_request"]] = Field(
        None,
        description="エラー内容を示す簡潔な識別子\n* `invalid` - 不正なリクエスト値,リクエスト値が妥当でない\n* `parse_error` - 不正な形式,リクエスト値を読み取ることができない\n* `bad_request` - リクエストの内容に何らかの問題がある",
    )
    message: Optional[str] = Field(None, description="エラーの内容", examples=["Invalid input."])
    errors: Optional[Errors] = Field(
        None,
        description="入力値に対するエラーを構造化した情報\n(code`invalid`の場合のみ)\n* `non_field_errors` - リクエスト全体に起因した(単一項目でない)エラー内容\n* `*` - 対応した入力項目ごとのエラー内容",
        examples=[{"foo": [{"code": "required", "message": "この項目は必須です"}]}],
    )


class ProblemDetails404(BaseModel):
    code: Optional[Literal["not_found"]] = None
    message: Optional[str] = Field(None, description="エラーの内容", examples=["見つかりませんでした。"])


class ProblemDetails409(BaseModel):
    code: Optional[Literal["conflict"]] = None
    message: Optional[str] = Field(None, description="エラーの内容", examples=["状態の競合によりリクエストを処理できません。"])


class ProblemDetails429(BaseModel):
    code: Optional[Literal["throttled"]] = None
    message: Optional[str] = Field(
        None, description="エラーの内容", examples=["リクエストの処理は絞られました。 Expected available in xxxxxxx."]
    )


class ProblemDetails503(BaseModel):
    code: Optional[Literal["temporary_unavailable"]] = None
    message: Optional[str] = Field(None, description="エラーの内容", examples=["一時的にご利用になれません。"])


class StorageItem(BaseModel):
    port: int = Field(..., description="ポート番号", examples=[0])
    type: Literal["ssd", "hdd"] = Field(..., description="種別")
    size_gibibytes: int = Field(..., description="ストレージ容量(GiB)", examples=[100])


class Zone(BaseModel):
    code: Literal["tk1", "tk2", "tk3", "os1", "os2", "os3", "is1"] = Field(
        ..., description="ゾーンコード\n* tk1 東京第1\n* tk2 東京第2\n* tk3 東京第3\n* os1 大阪第1\n* os2 大阪第2\n* os3 大阪第3\n* is1 石狩第1"
    )
    name: str = Field(..., description="ゾーン名称", examples=["石狩第1"])


class Ipv4(BaseModel):
    address: str = Field(..., description="アドレス", examples=["198.51.100.2"])
    netmask: str = Field(..., description="サブネットマスク", examples=["255.255.254.0"])
    gateway: str = Field(..., description="ゲートウェイのアドレス", examples=["198.51.100.1"])
    nameservers: List[str] = Field(..., description="ネームサーバーのアドレスリスト")
    hostname: str = Field(..., description="標準ホスト名", examples=["example.jp"])
    ptr: str = Field(..., description="逆引きホスト名", examples=["example.jp"])


class Ipv6(BaseModel):
    address: str = Field(..., description="アドレス", examples=["2001:e42:102:1501:153:121:89:107"])
    prefixlen: int = Field(..., description="プレフィックス長", examples=[64])
    gateway: str = Field(..., description="ゲートウェイのアドレス", examples=["fe80::1"])
    nameservers: List[str] = Field(..., description="ネームサーバーのアドレスリスト")
    hostname: str = Field(..., description="標準ホスト名", examples=["example.jp"])
    ptr: str = Field(..., description="逆引きホスト名", examples=["example.jp"])


class Contract(BaseModel):
    plan_code: int = Field(..., description="プランコード", examples=[3439])
    plan_name: str = Field(..., description="プラン名", examples=["さくらのVPS(v5)  1G IK01"])
    service_code: str = Field(..., description="サービスコード", examples=["100000000000"])


class Server(BaseModel):
    id: int = Field(..., description="id")
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")
    service_type: Literal["linux", "windows"] = Field(..., description="サービスタイプ")
    service_status: Literal["on_trial", "link_down_on_trial", "in_use", "link_down"] = Field(
        ..., description="サービス状況\n* on_trial お試し中\n* link_down_on_trial お試し中（一時停止）\n* in_use 利用中\n* link_down 一時停止中"
    )
    cpu_cores: int = Field(..., description="CPUコア数", examples=[2])
    memory_mebibytes: int = Field(..., description="メモリ容量(MiB)", examples=[1024])
    storage: List[StorageItem] = Field(..., description="ストレージ情報")
    zone: Zone = Field(..., description="ゾーン情報")
    options: List[str] = Field(..., description="オプション（追加ソフトウェア）")
    version: str = Field(..., description="プランの世代", examples=["v5"])
    ipv4: Ipv4
    ipv6: Ipv6
    contract: Contract = Field(..., description="契約情報")
    power_status: Literal[
        "power_on", "in_shutdown", "power_off", "installing", "in_scaleup", "migration", "unknown"
    ] = Field(
        ...,
        description="電源ステータス\n* power_on 電源ON\n* in_shutdown シャットダウン中\n* power_off 電源OFF\n* installing OSインストール中\n* in_scaleup スケールアップ中\n* migration サーバー移行作業中\n* unknown 不明（電源状態を取得できない）\nこのエンドポイントが返す電源ステータスはキャッシュされた情報のため、最新の正確な電源ステータスが必要な場合は\n**サーバーの電源状態を取得する**`/servers/{server_id}/power-status`をご利用ください",
    )


class ServerPowerStatus(BaseModel):
    status: Literal[
        "power_on", "in_shutdown", "power_off", "installing", "in_scaleup", "migration", "unknown"
    ] = Field(
        ...,
        description="電源ステータス\n* power_on 電源ON\n* in_shutdown シャットダウン中\n* power_off 電源OFF\n* installing OSインストール中\n* in_scaleup スケールアップ中\n* migration サーバー移行作業中\n* unknown 不明（電源状態を取得できない）",
    )


class StorageItem1(BaseModel):
    type: Literal["ssd", "hdd"] = Field(..., description="種別")
    size_gibibytes: int = Field(..., description="ストレージ容量(GiB)", examples=[100])


class Ipv41(BaseModel):
    address: str = Field(..., description="アドレス", examples=["198.51.100.2"])
    netmask: str = Field(..., description="サブネットマスク", examples=["255.255.254.0"])


class Contract1(BaseModel):
    plan_code: int = Field(..., description="プランコード", examples=[3439])
    plan_name: str = Field(..., description="プラン名", examples=["さくらのVPS(v5)  NFS 200GB OS03"])
    service_code: str = Field(..., description="サービスコード", examples=["100000000000"])


class NfsServer(BaseModel):
    id: int = Field(..., description="id")
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")
    service_status: Literal["in_preparation", "on_trial", "link_down_on_trial", "in_use", "link_down"] = Field(
        ...,
        description="サービス状況\n* in_preparation 準備中\n* on_trial お試し中\n* link_down_on_trial お試し中（一時停止）\n* in_use 利用中\n* link_down 一時停止中",
    )
    setting_status: Literal["done", "in_update", "failed"] = Field(
        ..., description="設定状況\n* done 設定完了\n* in_update 設定更新中\n* failed 設定更新失敗"
    )
    storage: List[StorageItem1] = Field(..., description="ストレージ情報")
    zone: Zone = Field(..., description="ゾーン情報")
    ipv4: Ipv41
    contract: Contract1 = Field(..., description="契約情報")
    power_status: Literal["power_on", "in_shutdown", "power_off", "unknown"] = Field(
        ...,
        description="電源ステータス\n* power_on 電源ON\n* in_shutdown シャットダウン中\n* power_off 電源OFF\n* unknown 不明（電源状態を取得できない）\nこのエンドポイントが返す電源ステータスはキャッシュされた情報のため、最新の正確な電源ステータスではない場合があります",
    )


class NfsServerPowerStatus(BaseModel):
    status: Literal["power_on", "in_shutdown", "power_off", "unknown"] = Field(
        ...,
        description="電源ステータス\n* power_on 電源ON\n* in_shutdown シャットダウン中\n* power_off 電源OFF\n* unknown 不明（電源状態を取得できない）",
    )


class Service(BaseModel):
    service_category: str = Field(..., description="サービスカテゴリー", examples=["cloud"])
    service_name: str = Field(..., description="サービス名", examples=["クラウド東京第1ゾーン"])
    switch_code: str = Field(..., description="スイッチコード", examples=["111111111111"])


class ExternalConnection(BaseModel):
    service_code: str = Field(..., description="サービスコード", examples=["100000000000"])
    type: Literal["cloud", "sales", "localrouter", "awsdxcon"] = Field(..., description="外部接続方式")
    services: List[Service]


class Switch(BaseModel):
    id: int = Field(..., description="id")
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")
    switch_code: str = Field(..., description="スイッチコード")
    zone: Zone = Field(..., description="ゾーン情報")
    server_interfaces: List[int] = Field(..., description="接続されているサーバーのインターフェースid")
    nfs_server_interfaces: List[int] = Field(..., description="接続されている追加ストレージ（NFS）のインターフェースid")
    external_connection: ExternalConnection = Field(..., description="接続されている外部接続の情報")


class UpdateServer(BaseModel):
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")


class ShutdownServer(BaseModel):
    force: bool = Field(False, description="強制停止を行うか")


class UpdateNfsServer(BaseModel):
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")


class UpdateHost(BaseModel):
    hostname: str = Field(..., description="ホスト名", examples=["example.jp"])


class CreateSwitch(BaseModel):
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")
    zone_code: Literal["tk2", "tk3", "os3", "is1"] = Field(..., description="ゾーンコード")


class UpdateSwitch(BaseModel):
    name: str = Field(..., description="名前")
    description: str = Field(..., description="説明")


class UpdateNfsServerIpv4(BaseModel):
    address: str = Field(..., description="アドレス", examples=["198.51.100.2"])
    netmask: str = Field(..., description="サブネットマスク", examples=["255.255.254.0"])


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
