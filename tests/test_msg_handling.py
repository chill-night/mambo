# tests/test_message_handling.py
import pytest
from unittest.mock import AsyncMock, MagicMock, patch, PropertyMock
from src import main

@pytest.mark.asyncio
async def test_profanity_filter():
    """Test that profanity is filtered"""

    # Create mock message with profanity
    mock_message = MagicMock()
    mock_message.content = "This is shit"
    mock_message.author = MagicMock()
    mock_message.author.mention = "@TestUser"
    mock_message.delete = AsyncMock()
    mock_message.channel.send = AsyncMock()

    # Create a different mock for bot user
    mock_bot_user = MagicMock()
    mock_bot_user.id = 12345
    mock_message.author.id = 67890  # Different ID

    # Patch the user property using PropertyMock
    with patch.object(type(main.bot), 'user', new_callable=PropertyMock) as mock_user_prop:
        mock_user_prop.return_value = mock_bot_user
        main.bot.process_commands = AsyncMock()

        # Call the on_message event
        await main.on_message(mock_message)

    # Verify message was deleted
    mock_message.delete.assert_called_once()
    mock_message.channel.send.assert_called_once()

    # Check the warning message was sent
    call_args = mock_message.channel.send.call_args[0][0]
    assert "not very sigma" in call_args

@pytest.mark.asyncio
async def test_bot_ignores_own_messages():
    """Test that bot ignores its own messages"""

    # Create mock message from bot itself
    mock_message = MagicMock()
    mock_message.author = main.bot.user
    mock_message.content = "Bot message"

    # This should return early without processing
    result = await main.on_message(mock_message)

    # Since it returns early, result should be None
    assert result is None