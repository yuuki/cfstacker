# stacker

[license]: https://github.com/yuuki/stacker/blob/master/LICENSE

A CLI tool to manage AWS CloudFormation stack in Python.

## Usage

```shell
% stacker
Usage: stacker.py [OPTIONS] ACTION STACK

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
```

## Installation

With homebrew:

```shell
brew install --HEAD yuuki/stacker/stacker
```

Or with pip:


```shell
pip3 install git+https://github.com/yuuki/stacker
```

## Requirements

- [AWS CLI](https://aws.amazon.com/jp/cli/)

## Directory Layout

```shell
% tree examples/
examples/
├── Makefile
├── bin
│   └── stacker
└── stacks
    ├── iam
    │   ├── parameters
    │   │   ├── prod.json
    │   │   └── staging.json
    │   ├── policy.json
    │   └── templates
    │       ├── prod.yml
    │       └── staging.yml
    └── s3
        ├── parameters
        │   ├── prod.json
        │   └── staging.json
        ├── policy.json
        └── template.yml
```

## License

[MIT][license]

## Thanks

[chrolis](https://github.com/chrolis) (Original version writer)
