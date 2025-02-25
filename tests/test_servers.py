import unittest

from vpsc.models.custom import UpdateServer, ShutdownServer, UpdateHost
from vpsc.client import Client, APIConfig
from tests.patch_request import patch_request


class TestServers(unittest.TestCase):
    def setUp(self):
        self.client = Client(config=APIConfig(api_key="test"))

    @patch_request("server_200")
    def test_get_server(self, patched):
        server = self.client.get_server(server_id=1)
        assert 0 == server.id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/servers/1",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("servers_200")
    def test_get_servers(self, patched):
        servers = self.client.get_servers()
        assert 1 == len(servers)
        assert 0 == list(servers)[0].id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/servers",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("empty_list_200")
    def test_get_servers_empty(self, patched):
        servers = self.client.get_servers()
        assert 0 == len(servers)
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/servers",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("server_200")
    def test_update_servers(self, patched):
        data = UpdateServer(name="name_test", description="description_test")
        result = self.client.update_server(server_id=0, data=data)
        assert 0 == result.id
        patched.assert_called_once_with(
            method="put",
            url=f"{self.client.config.host}/servers/0",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
            data=data.model_dump_json(exclude_unset=True).encode("utf-8"),
        )

    @patch_request("server_power_status_200")
    def test_get_power_status(self, patched):
        result = self.client.get_server_power_status(server_id=0)
        assert "power_on" == result.status
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/servers/0/power-status",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("status_202")
    def test_power_on_server(self, patched):
        result = self.client.power_on_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/power-on",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("status_202")
    def test_shutdown_server(self, patched):
        result = self.client.power_on_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/power-on",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("status_202")
    def test_force_reboot_server(self, patched):
        result = self.client.power_on_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/power-on",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("status_202")
    def test_power_on_server(self, patched):
        result = self.client.power_on_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/power-on",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("status_202")
    def test_shutdown_server(self, patched):
        result = self.client.shutdown_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/shutdown",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
            data=ShutdownServer(force=False).model_dump_json(exclude_unset=True).encode("utf-8"),
        )

        patched.reset_mock()
        result = self.client.shutdown_server(server_id=0, force=True)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/shutdown",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
            data=ShutdownServer(force=True).model_dump_json(exclude_unset=True).encode("utf-8"),
        )

    @patch_request("status_202")
    def test_force_reboot_server(self, patched):
        result = self.client.force_force_reboot_server(server_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/servers/0/force-reboot",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("server_ptr_200")
    def test_server_ipv4_ptr(self, patched):
        data = UpdateHost(hostname="example.com")
        result = self.client.update_server_ipv4_ptr(server_id=0, data=data)
        assert result.ptr == "example.jp"
        patched.assert_called_once_with(
            method="put",
            url=f"{self.client.config.host}/servers/0/ipv4-ptr",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
            data=data.model_dump_json(exclude_unset=True).encode("utf-8"),
        )

    @patch_request("server_ptr_200")
    def test_server_ipv6_ptr(self, patched):
        data = UpdateHost(hostname="example.com")
        result = self.client.update_server_ipv6_ptr(server_id=0, data=data)
        assert result.ptr == "example.jp"
        patched.assert_called_once_with(
            method="put",
            url=f"{self.client.config.host}/servers/0/ipv6-ptr",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
            data=data.model_dump_json(exclude_unset=True).encode("utf-8"),
        )

    @patch_request("server_limitation_200")
    def test_server_limitation(self, patched):
        result = self.client.get_server_limitation(server_id=0)
        assert result.cpu_performance_limit == "enabled"
        assert result.network_bandwidth_limit == "disabled"
        assert result.outbound_port_25_blocking == "disabled"
        assert result.storage_iops_limit == "disabled"
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/servers/0/limitation",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )
