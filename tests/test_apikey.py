import unittest

from tests.patch_request import patch_request
from vpsc.client import Client, APIConfig
from vpsc.models.custom import CreateApiKey, UpdateApiKey


class TestApiKeys(unittest.TestCase):
    def setUp(self):
        self.client = Client(config=APIConfig(api_key="test"))

    @patch_request("apikey_201")
    def test_create_api_key(self, patched):
        data = CreateApiKey(
            name="APIキー",
            role=1,
        )
        key = self.client.create_api_key(
            data=data,
        )
        assert 0 == key.id
        patched.assert_called_once_with(
            method="post",
            url=f"{self.client.config.host}/api-keys",
            data=data.model_dump_json(exclude_unset=True).encode("utf-8"),
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("apikeys_200")
    def test_get_api_keys(self, patched):
        keys = self.client.get_api_keys()
        assert 1 == len(keys)
        assert 0 == list(keys)[0].id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/api-keys",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("apikey_200")
    def test_get_api_key(self, patched):
        key = self.client.get_api_key(key_id=0)
        assert 0 == key.id
        patched.assert_called_once_with(
            method="get",
            url=f"{self.client.config.host}/api-keys/0",
            headers={"Authorization": f"Bearer {self.client.config.api_key}"},
        )

    @patch_request("apikey_200")
    def test_update_api_key(self, patched):
        data = UpdateApiKey(
            name="APIキー",
            role=1,
        )
        key = self.client.update_api_key(
            key_id=0,
            data=data,
        )
        assert 0 == key.id
        patched.assert_called_once_with(
            method="put",
            url=f"{self.client.config.host}/api-keys/0",
            data=data.model_dump_json(exclude_unset=True).encode("utf-8"),
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )

    @patch_request("status_204")
    def test_delete_switch(self, patched):
        result = self.client.delete_api_key(key_id=0)
        assert result is None
        patched.assert_called_once_with(
            method="delete",
            url=f"{self.client.config.host}/api-keys/0",
            headers={"Authorization": f"Bearer {self.client.config.api_key}", "content-type": "application/json"},
        )
