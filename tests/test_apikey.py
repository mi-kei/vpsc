import unittest

from vpsc.models.custom import UpdateServer, ShutdownServer, UpdateHost
from vpsc.client import Client, APIConfig
from tests.patch_request import patch_request


class TestApiKeys(unittest.TestCase):
    def setUp(self):
        self.client = Client(config=APIConfig(api_key="test"))

    @patch_request("apikeys_200")
    def test_api_keys(self, patched):
        keys = self.client.get_api_keys()
        assert 1 == len(keys)
        assert 0 == list(keys)[0].id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/api-keys",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("apikey_200")
    def test_get_server(self, patched):
        key = self.client.get_api_key(key_id=0)
        assert 0 == key.id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/api-keys/0",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )
