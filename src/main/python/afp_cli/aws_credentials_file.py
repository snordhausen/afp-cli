#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import os

def write(aws_credentials, filename=None, profile_name='default'):

    # WTF
    ORIG_DEFAULTSECT = ConfigParser.DEFAULTSECT
    ConfigParser.DEFAULTSECT = 'default'

    try:

        if not filename:
            filename = os.path.expanduser("~") + '/.aws/credentials'

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        config = ConfigParser.RawConfigParser()
        config.read(filename)

        if not config.has_section(profile_name) and profile_name.lower() != 'default':
            config.add_section(profile_name)

        config.set(profile_name, 'aws_access_key_id', aws_credentials['AWS_ACCESS_KEY_ID'])
        config.set(profile_name, 'aws_secret_access_key', aws_credentials['AWS_SECRET_ACCESS_KEY'])
        config.set(profile_name, 'aws_session_token', aws_credentials['AWS_SESSION_TOKEN'])

        with open(filename, 'w') as config_file:
                config.write(config_file)

    finally:
        ConfigParser.DEFAULTSECT = ORIG_DEFAULTSECT
