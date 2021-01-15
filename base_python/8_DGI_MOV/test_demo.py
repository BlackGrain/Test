import yaml
import pytest


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("env.yaml")))  # only read keys,put dict into a list is ok
    def test_demo(self, env):
        if "test" in env:
            print("the ip of test is:", env["test"])
        elif "dev" in env:
            print("the ip of dev is:", env["dev"])

