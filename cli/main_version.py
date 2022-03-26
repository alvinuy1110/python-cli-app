import click
import codecs
import os


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


# The expose_value parameter prevents the pretty pointless version parameter from being passed to the callback.
# If that was not specified, a boolean would be passed to the hello script.
# The resilient_parsing flag is applied to the context if Click wants to parse the command line without
# any destructive behavior that would change the execution flow. In this case, because we would exit the program,
# we instead do nothing.

@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,

    ))
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def hello():
    click.echo('Hello World!')


if __name__ == '__main__':
    hello()
