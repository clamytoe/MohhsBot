# -*- coding: utf-8 -*-
from keys import BOT_ID, BOT_NAME, CHANNEL_ID, SLACK_BOT_TOKEN
import mohhsbot


def test_environment_variables():
    assert BOT_ID == 'U854JKLNS'
    assert BOT_NAME == 'mohh'
    assert CHANNEL_ID.startswith('xoxp')
    assert SLACK_BOT_TOKEN.startswith('xoxb')


def test_slack_connection():
    assert isinstance(mohhsbot.SLACK_CLIENT, mohhsbot.SlackClient)


def test_bot_id():
    assert mohhsbot.AT_BOT == f'<@{BOT_ID}>'


def test_save_keywords():
    assert 'archive' in mohhsbot.STORE_COMMANDS
    assert 'backup' in mohhsbot.STORE_COMMANDS
    assert 'keep' in mohhsbot.STORE_COMMANDS
    assert 'put' in mohhsbot.STORE_COMMANDS
    assert 'remember' in mohhsbot.STORE_COMMANDS
    assert 'save' in mohhsbot.STORE_COMMANDS
    assert 'store' in mohhsbot.STORE_COMMANDS


def test_retrieve_keywords():
    assert 'find' in mohhsbot.RETRIEVE_COMMANDS
    assert 'get' in mohhsbot.RETRIEVE_COMMANDS
    assert 'give' in mohhsbot.RETRIEVE_COMMANDS
    assert 'lookup' in mohhsbot.RETRIEVE_COMMANDS
    assert 'retrieve' in mohhsbot.RETRIEVE_COMMANDS
    assert 'search' in mohhsbot.RETRIEVE_COMMANDS
