"""
VPSC のコマンド一覧です
"""

from time import sleep
from xmlrpc.client import Fault

import click
from pydantic import BaseModel

from .models.custom import UpdateServer, UpdateHost, UpdateNfsServer, UpdateNfsServerIpv4, UpdateApiKey, CreateApiKey
from .exceptions import exception_handler, APIException
from .client import APIConfig, Client


def _print(data: BaseModel):
    click.echo(data.model_dump_json(exclude_unset=True, indent=2))


@click.group()
def vpsc():
    """
    VPSC コマンドです。

    操作するリソースを指定して実行してください
    """
    global client
    client = Client(config=APIConfig())


@vpsc.group()
def server():
    """
    サーバーリソースに対する操作
    """
    pass


@vpsc.group()
def nfs_server():
    """
    NFSサーバーのリソースに対する操作
    """


@vpsc.group()
def apikey():
    """
    APIキーのリソースに対する操作
    """


@click.command(name="list")
@click.option("--server-id", "-id", help="サーバーID", required=False, type=int)
def get_servers(server_id):
    """サーバー情報の取得"""
    if server_id is not None:
        _print(client.get_server(server_id=server_id))
    else:
        for item in client.get_servers():
            _print(item)


@click.command(name="update")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
@click.option("--name", "-n", help="名前", required=False, type=str, default="")
@click.option("--description", "-d", help="説明", required=False, type=str, default="")
def update_server(server_id, name, description):
    """サーバー情報更新"""
    data = UpdateServer(name=name, description=description)
    res = client.update_server(server_id=server_id, data=data)
    _print(res)


@click.command(name="power-status")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
def get_server_power_status(server_id):
    """サーバーの電源状態を取得"""
    _print(client.get_server_power_status(server_id=server_id))


@click.command(name="power-on")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
def power_on_server(server_id):
    """サーバーを起動"""
    client.power_on_server(server_id=server_id)
    sleep(5)
    _print(client.get_server_power_status(server_id=server_id))


@click.command(name="shutdown")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
@click.option("--force", "-f", help="強制的にシャットダウン", required=False, type=bool, default=False, is_flag=True)
def shutdown_server(server_id, force):
    """サーバーをシャットダウン"""
    client.shutdown_server(server_id=server_id, force=force)
    sleep(5)
    _print(client.get_server_power_status(server_id=server_id))


@click.command(name="ptr-record")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
@click.option(
    "--type", "-t", "type_", help="設定タイプ", required=True, type=click.Choice(["ipv4", "ipv6"], case_sensitive=False)
)
@click.option("--hostname", "-h", help="ホスト名", required=True, type=str)
def update_server_ptr_record(server_id, type_, hostname):
    """サーバーの逆引きホスト名を設定"""
    data = UpdateHost(hostname=hostname)
    if type_ == "ipv4":
        client.update_server_ipv4_ptr(server_id=server_id, data=data)
    elif type_ == "ipv6":
        client.update_server_ipv6_ptr(server_id=server_id, data=data)
    _print(client.get_server(server_id=server_id))


@click.command(name="limitation")
@click.option("--server-id", "-id", help="サーバーID", required=True, type=int)
def get_server_limitation(server_id):
    """サーバーの電源状態を取得"""
    _print(client.get_server_limitation(server_id=server_id))


@click.command(name="list")
@click.option("--nfs-server-id", "-id", help="NFSサーバーID", required=False, type=int)
def get_nfs_servers(nfs_server_id):
    """NFSサーバー情報の取得"""
    if nfs_server_id is not None:
        _print(client.get_nfs_server(nfs_server_id=nfs_server_id))
    else:
        for item in client.get_nfs_servers():
            _print(item)


@click.command(name="update")
@click.option("--nfs-server-id", "-id", help="NFSサーバーID", required=False, type=int)
@click.option("--name", "-n", help="名前", required=False, type=str, default="")
@click.option("--description", "-d", help="説明", required=False, type=str, default="")
def update_nfs_server(nfs_server_id, name, description):
    """サーバー情報更新"""
    data = UpdateNfsServer(name=name, description=description)
    res = client.update_nfs_server(nfs_server_id=nfs_server_id, data=data)
    _print(res)


@click.command(name="update-ipv4")
@click.option("--nfs-server-id", "-id", help="NFSサーバーID", required=False, type=int)
@click.option("--hostname", "-h", help="ホスト名", required=True, type=str)
def update_nfs_server_ipv4(nfs_server_id, address, netmask):
    """NFSサーバーのipv4を設定"""
    data = UpdateNfsServerIpv4(address=address, netmask=netmask)
    client.update_nfs_server_ipv4(nfs_server_id=nfs_server_id, data=data)
    _print(client.get_nfs_server(nfs_server_id=nfs_server_id))


@click.command(name="power-status")
@click.option("--nfs-server-id", "-id", help="サーバーID", required=True, type=int)
def get_nfs_server_power_status(nfs_server_id):
    """NFSサーバーの電源状態を取得"""
    _print(client.get_nfs_server_power_status(nfs_server_id=nfs_server_id))


@click.command(name="list")
@click.option("--key-id", "-id", help="APIキーID", required=False, type=int)
def get_api_keys(key_id):
    """APIキー情報の取得"""
    if key_id is not None:
        _print(client.get_api_key(key_id=key_id))
    else:
        for item in client.get_api_keys():
            _print(item)


@click.command(name="create")
@click.option("--name", "-n", help="名前", required=False, type=str, default="")
@click.option("--role-id", "-rid", help="ロールID", required=True, type=int)
def create_api_key(name, role_id):
    data = CreateApiKey(name=name, role=role_id)
    res = client.create_api_key(data=data)
    _print(res)


@click.command(name="update")
@click.option("--key-id", "-id", help="APIキーID", required=True, type=int)
@click.option("--name", "-n", help="名前", required=False, type=str, default="")
@click.option("--role-id", "-rid", help="ロールID", required=True, type=int)
def update_api_key(key_id, name, role_id):
    data = UpdateApiKey(name=name, role=role_id)
    res = client.update_api_key(key_id=key_id, data=data)
    _print(res)


# server commands
server.add_command(get_servers)
server.add_command(update_server)
server.add_command(get_server_power_status)
server.add_command(power_on_server)
server.add_command(shutdown_server)
server.add_command(update_server_ptr_record)
server.add_command(get_server_limitation)

# nfs server commands
nfs_server.add_command(get_nfs_servers)
nfs_server.add_command(update_nfs_server)
nfs_server.add_command(update_nfs_server_ipv4)
nfs_server.add_command(get_nfs_server_power_status)

# TODO: switch

# api key
apikey.add_command(get_api_keys)
apikey.add_command(create_api_key)
apikey.add_command(update_api_key)


def entry_point():
    try:
        vpsc()
    except APIException as e:
        exception_handler(e)
    except Exception as e:
        click.echo(e)
