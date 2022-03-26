import click
import codecs
import os

@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,

    ))
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True
)
@click.option(
    "--username", prompt=True,
    default=lambda: os.environ.get("USER", ""),
    show_default="current user"
)
def hello(password, username):
    click.echo(f"encoded: {codecs.encode(password, 'rot13')}")
    click.echo(f"Hello, {username}!")

if __name__ == '__main__':
    hello()
