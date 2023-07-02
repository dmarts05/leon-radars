import pytest
from leon_radars.config_parser.helpers import verify_monitored_streets_section, verify_telegram_section


def test_verify_monitored_streets_section_valid():
    monitored_streets = ["street1", "street2"]
    result = verify_monitored_streets_section(monitored_streets)
    assert result == monitored_streets


def test_verify_monitored_streets_section_empty():
    monitored_streets = []
    with pytest.raises(ValueError):
        verify_monitored_streets_section(monitored_streets)


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
    telegram = {}
    with pytest.raises(ValueError):
        verify_telegram_section(telegram)
