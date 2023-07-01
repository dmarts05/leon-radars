import pytest
from leon_radars.config_parser.helpers import verify_streets_section, verify_telegram_section


def test_verify_streets_section_valid():
    streets = ["Street 1", "Street 2", "Street 3"]
    result = verify_streets_section(streets)
    assert result == streets


def test_verify_streets_section_missing():
    with pytest.raises(ValueError):
        verify_streets_section([])


def test_verify_telegram_section_valid():
    telegram = {"token": "your_token", "chat_id": "your_chat_id"}
    result = verify_telegram_section(telegram)
    assert result == telegram


def test_verify_telegram_section_missing_fields():
    telegram = {"token": "your_token"}
    with pytest.raises(ValueError):
        verify_telegram_section(telegram)
    telegram = {"chat_id": "your_chat_id"}
    with pytest.raises(ValueError):
        verify_telegram_section(telegram)
