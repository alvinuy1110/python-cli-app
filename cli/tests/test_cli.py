from click.testing import CliRunner
from cli.main_hello import hello


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(hello, ['--name', 'Peter'])
    print("t1")
    assert result.exit_code == 0
    assert result.output == 'Hello Peter!\n'

if __name__ == '__main__':
    test_hello_world()