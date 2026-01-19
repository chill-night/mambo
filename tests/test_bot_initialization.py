# tests/test_bot_initialization.py
from discord.ext import commands
from src import main

def test_bot_intents():
    """Test that bot has correct intents configured"""

    assert main.intents.message_content == True
    assert main.intents.guilds == True
    assert main.intents.members == True

def test_bot_command_prefix():
    """Test that bot has correct command prefix"""

    assert main.bot.command_prefix == "!"

def test_environment_variables():
    """Test that required environment variables are loaded"""

    # Check that DISCORD_TOKEN is loaded (we don't check the value for security)
    assert main.DISCORD_TOKEN is not None
    assert len(main.DISCORD_TOKEN) > 0

def test_log_paths_exist():
    """Test that log directory structure is correct"""

    # Verify paths are defined
    assert main.PROJ_SRC_PATH is not None
    assert main.PROJ_ROOT_PATH is not None
    assert main.PROJ_LOG_PATH is not None
    assert main.DISCORD_LOG_PATH is not None

    # Verify log path ends with expected file
    assert main.DISCORD_LOG_PATH.endswith("discord.log")

def test_bot_tree_commands_registered():
    """Test that slash commands are registered"""

    # Get all slash commands
    slash_commands = [cmd.name for cmd in main.bot.tree.get_commands()]

    assert "test123" in slash_commands

def test_bot_events_registered():
    """Test that event handlers are registered"""

    # Check that event handlers exist
    assert hasattr(main.bot, 'on_ready')
    assert hasattr(main.bot, 'on_member_join')
    assert hasattr(main.bot, 'on_message')