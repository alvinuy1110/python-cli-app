import click


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,

    ))
@click.option('--name', prompt='Your name',
              help='The person to greet.', default="test")
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == '__main__':
    hello()
