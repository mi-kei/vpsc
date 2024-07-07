import os
import re
from unittest import mock

import requests

path = os.path.dirname(os.path.realpath(__file__))


def patch_request(response_name: str):
    def _decorate(func):
        def loader(*args, **kwargs):
            filename = response_name if re.match(r".+\.json$", response_name) else f"{response_name}.json"
            with open(f"{path}/responses/{filename}", mode="r") as f:
                data = f.readlines()
            response = requests.Response()
            response.status_code = int(response_name.split("_")[-1])
            response._content = "\n".join(data).encode("utf-8")

            with mock.patch("requests.request", return_value=response) as patched:
                kwargs["patched"] = patched
                func(*args, **kwargs)

        return loader

    return _decorate
