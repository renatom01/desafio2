import pathlib
import sys

from sitechecker.cli import read_user_cli_args


def main():
    # ...


def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)
