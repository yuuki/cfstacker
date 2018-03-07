#!/usr/bin/env python3
# coding: utf-8

import optparse
import sys
from . import version


def action_create(stack, args):
    pass


def action_update(stack, args):
    pass


def action_delete(stack, args):
    pass


def action_validate(stack, args):
    pass


help_text = """%prog [OPTIONS] ACTION STACK

Actions:
    create      create stack
    update      update stack after show diffs with currently deployed stack
    delete      delete stack
    validate    validate template

Options:
    -n, --dry-run       only shows command-lines
    -s, --stack-name    specify stack name
    -c, --capabilities  specify capabilities
    -e, --environment   specify environment
    -p, --profile       specify AWS_PROFILE
"""


def main():
    parser = optparse.OptionParser(
        usage=help_text,
        version='%prog v'+version,
    )
    parser.add_option('-s', '--stack-name', dest='stackname')
    parser.add_option('-c', '--capabilities', dest='capabilities')
    parser.add_option('-e', '--environment', dest='environment')
    parser.add_option('-p', '--profile', dest='profile')
    parser.add_option('--dry-run', action='store_true')

    opts, args = parser.parse_args()
    if len(args) != 2:
        parser.print_help()
        sys.exit(129)
    try:
        action, stack = args[0], args[1]
        if action == 'create':
            action_create(stack, opts)
        elif action == 'update':
            action_update(stack, opts)
        elif action == 'delete':
            action_delete(stack, opts)
        elif action == 'validate':
            action_validate(stack, args)
        else:
            raise UsageError()
    except UsageError:
        parser.print_help()
        sys.exit(129)


if __name__ == '__main__':
    main()
