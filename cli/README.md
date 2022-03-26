Click Example
=============
CLI using Click

# Setup

* pip install click

## Commands

* --help - show help

### Ignore unknown

```
@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,

    ))
```
### Multiple value
```
python.exe .\cli\main.py -m 1 -m 2 -vvv
```

### List of Values

```
python.exe .\cli\main.py -m 1 -m 2 --choice-type Apple
```
Note: careful about the variable name and snake_case

### Callback
```
python.exe .\cli\main_version.py
python.exe .\cli\main_version.py --version
```


## Options

see https://click.palletsprojects.com/en/8.0.x/options/

## Setup Tools
Instead of using main, this will be like a packaged  cli

### How to Setup
see https://click.palletsprojects.com/en/8.0.x/setuptools/#setuptools-integration

