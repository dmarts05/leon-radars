import pytest
from leon_radars.config_parser.helpers import verify_telegram_section


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
