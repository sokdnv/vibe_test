import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from services.ai_formatter import reformat_text


@pytest.mark.asyncio
async def test_reformat_returns_dict_with_required_keys():
    mock_response_text = '{"hook": "Заголовок", "body": "Текст", "cta": "Подпишись"}'

    mock_message = MagicMock()
    mock_message.content = mock_response_text

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_completion = MagicMock()
    mock_completion.choices = [mock_choice]

    with patch("services.ai_formatter.client") as mock_client:
        mock_client.chat.completions.create = AsyncMock(return_value=mock_completion)
        result = await reformat_text("Какой-то сырой текст")

    assert isinstance(result, dict)
    assert "hook" in result
    assert "body" in result
    assert "cta" in result


@pytest.mark.asyncio
async def test_reformat_returns_correct_values():
    mock_response_text = '{"hook": "Цепляющий заголовок", "body": "Основной текст поста", "cta": "Подпишись на канал"}'

    mock_message = MagicMock()
    mock_message.content = mock_response_text

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_completion = MagicMock()
    mock_completion.choices = [mock_choice]

    with patch("services.ai_formatter.client") as mock_client:
        mock_client.chat.completions.create = AsyncMock(return_value=mock_completion)
        result = await reformat_text("Сырой текст для теста")

    assert result["hook"] == "Цепляющий заголовок"
    assert result["body"] == "Основной текст поста"
    assert result["cta"] == "Подпишись на канал"


@pytest.mark.asyncio
async def test_reformat_handles_json_with_extra_whitespace():
    mock_response_text = '  { "hook": "H", "body": "B", "cta": "C" }  '

    mock_message = MagicMock()
    mock_message.content = mock_response_text

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_completion = MagicMock()
    mock_completion.choices = [mock_choice]

    with patch("services.ai_formatter.client") as mock_client:
        mock_client.chat.completions.create = AsyncMock(return_value=mock_completion)
        result = await reformat_text("Текст")

    assert result["hook"] == "H"
