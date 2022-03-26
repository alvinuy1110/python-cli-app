import click


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,

    ))
@click.option('--count', default=1, help='Number of greetings.', show_default=True, type=int)
@click.option('--name', prompt='Your name',
              help='The person to greet.', default="test")
@click.option('-m', '--message', multiple=True,
              help='message')
@click.option('-v', '--verbose', count=True)
@click.option('--shout', is_flag=True)
@click.option('--choice-type',
              type=click.Choice(['APPLE', 'BANANA'], case_sensitive=False))
def hello(count, name, message, verbose, shout, choice_type):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

    click.echo('\n'.join(message))
    click.echo(f"Verbosity: {verbose}")
    shout_func(shout)
    click.echo(f"Choice type: {choice_type}")

def shout_func(shout_input):
    if shout_input:
        click.echo("Is Shout")
    else:
        click.echo("Is NOT Shout")


if __name__ == '__main__':
    hello()
