from datetime import datetime
from time import sleep
from typing import TypeVar

import click


@click.command()
@click.option(
    "--waitfor",
    type=bool,
    is_flag=True,
    help="Wait for a specific period of time instead of waiting until a certain time. Provide in the format HH:MM:SS.",
)
@click.option(
    "--today",
    type=bool,
    is_flag=True,
    help="Auto-append today's date to the time argument. Does nothing if --waitfor is used.",
)
@click.argument(
    "time",
    type=str,
    required=True,
)
def main(waitfor: bool, today: bool, time: str):
    now = datetime.now()
    if waitfor:
        wait_time = get_waitfor_wait_time(time)
    else:
        if today:
            time = f"{now.date()} {time}"
        wait_time = datetime.fromisoformat(time)

    sleep_time = (wait_time - now).total_seconds()
    sleep(sleep_time)


def get_waitfor_wait_time(time: str) -> datetime:
    now = datetime.now()
    split_time = [int(t) for t in time.split(":")[::-1]]
    seconds = get_idx_else_none(split_time, 0) or 0
    minutes = get_idx_else_none(split_time, 1) or 0
    hours = get_idx_else_none(split_time, 2) or 0

    minutes += hours * 60
    seconds += minutes * 60

    wait_time = datetime.fromtimestamp(now.timestamp() + seconds)

    return wait_time


ElementType = TypeVar("ElementType")


def get_idx_else_none(lst: list[ElementType], idx: int) -> ElementType | None:
    """Get an element from a list if it exists, otherwise return None."""
    return lst[idx] if idx < len(lst) else None


if __name__ == "__main__":
    main()
