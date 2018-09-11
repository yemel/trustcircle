#!/usr/bin/env python
import os
import sys
import dotenv


if __name__ == "__main__":

    env = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))

    if os.path.isfile(env):
        dotenv.read_dotenv(env)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
