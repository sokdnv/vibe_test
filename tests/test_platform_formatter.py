import pytest
from services.platform_formatter import format_for_telegram, format_for_instagram


def test_telegram_hook_is_bold():
    result = format_for_telegram("Заголовок", "Основной текст", "Подпишись")
    assert "*Заголовок*" in result


def test_telegram_cta_is_italic():
    result = format_for_telegram("Заголовок", "Основной текст", "Подпишись")
    assert "_Подпишись_" in result


def test_telegram_body_present():
    result = format_for_telegram("Заголовок", "Основной текст", "Подпишись")
    assert "Основной текст" in result


def test_telegram_sections_separated():
    result = format_for_telegram("H", "B", "C")
    parts = result.split("\n\n")
    assert len(parts) == 3


def test_instagram_hook_is_unicode_bold():
    result = format_for_instagram("Hi", "Body text", "Follow us")
    # Unicode bold 'H' is 𝗛, 'i' is 𝗶
    assert "𝗛𝗶" in result


def test_instagram_cta_is_unicode_italic():
    result = format_for_instagram("Hi", "Body text", "ab")
    # Unicode italic 'a' is 𝘢, 'b' is 𝘣
    assert "𝘢𝘣" in result


def test_instagram_body_present():
    result = format_for_instagram("Hi", "Body text", "Follow")
    assert "Body text" in result


def test_instagram_has_emoji_separator():
    result = format_for_instagram("Hi", "Body text", "Follow")
    assert "—" in result or "✦" in result or "\n\n" in result
