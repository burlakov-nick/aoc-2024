from os import listdir, makedirs
from shutil import copyfile

import click

import aoc


def get_last_day() -> int:
    return max(
        [int(f[4:6]) for f in listdir(".") if f.startswith("day_") and f[4:6].isdigit()]
    )


@click.group()
def cli():
    pass


@click.command()
@click.option("-d", "--day", type=int)
@click.option("-s", "--sample", is_flag=True, default=False)
@click.option("-t", "--test", is_flag=True, default=False)
def run(day, sample, test):
    if not day:
        day = get_last_day()
    if not sample and not test:
        sample = test = True
    aoc.run(day, sample, test)


@click.command()
@click.option("-d", "--day", type=int)
def next(day):
    if not day:
        day = get_last_day() + 1

    makedirs(f"day_{day:02d}")
    for filename in ["sample.txt", "test.txt", "run.py", "__init__.py"]:
        copyfile(f"day_00/{filename}", f"day_{day:02d}/{filename}")


cli.add_command(run)
cli.add_command(next)


if __name__ == "__main__":
    cli()
