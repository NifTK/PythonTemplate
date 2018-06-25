#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys

from {{ cookiecutter.pkg_name }}.ui.hello_world import hello_world
from versioneer import get_version


def main(args=None):
    """Entry point for {{ cookiecutter.project_name }} application"""

    parser = argparse.ArgumentParser(description='{{ cookiecutter.project_name }}')

    parser.add_argument("-t", "--text", required=False, default=None,
                        type=str
                        help="Text to display")
    version_string = get_version()
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='{{ cookiecutter.project_name }} version ' + friendly_version_string)

    args = parser.parse_args(args)

    {{ cookiecutter.pkg_name }}(args.text)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
