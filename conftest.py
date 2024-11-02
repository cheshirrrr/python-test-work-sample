import json
import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--block_data",
        action="append",
        default="base_text_block_test_data.json",
        help="name of the file containing test data for text block test",
    )
    parser.addoption(
        "--verb_data",
        action="append",
        default="base_verbalization_test_data.json",
        help="name of the file containing test data for verbalization test",
    )

def pytest_generate_tests(metafunc):
    if "block_data" in metafunc.fixturenames:
        text_blocks_data = open(metafunc.config.getoption("block_data"))
        block_json = json.load(text_blocks_data)
        metafunc.parametrize("block_data", block_json)
    if "verb_data" in metafunc.fixturenames:
        verb_data = open(metafunc.config.getoption("verb_data"))
        verb_json = json.load(verb_data)
        metafunc.parametrize("verb_data", verb_json)