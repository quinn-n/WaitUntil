import datetime
from unittest.mock import Mock, patch

import hypothesis
import hypothesis.strategies as st

import waituntil


@hypothesis.given(
    time=st.datetimes(),
    hours=st.integers(0, 100000),
    minutes=st.integers(0, 59),
    seconds=st.integers(0, 59),
)
def test_wait_until(
    *,
    time: datetime.datetime,
    hours: int,
    minutes: int,
    seconds: int,
) -> None:
    time_str = f"{hours}:{minutes}:{seconds}"
    # Patch `datetime.now` to return the same `now` used later to avoid
    # (extremely rare) flaky test failures due to time passing.
    datetime_mock = Mock(wraps=datetime.datetime)
    datetime_now_mock = Mock(wraps=datetime.datetime.now)
    datetime_mock.attach_mock(datetime_now_mock, "now")

    datetime_now_mock.return_value = time

    with patch(
        f"{waituntil.__name__}.datetime",
        new=datetime_mock,
    ):
        wait_time = waituntil.get_waitfor_wait_time(time_str)

    minutes += hours * 60
    seconds += minutes * 60

    expected_result = datetime.datetime.fromtimestamp(time.timestamp() + seconds)

    assert wait_time.day == expected_result.day
    assert wait_time.hour == expected_result.hour
    assert wait_time.minute == expected_result.minute
    assert wait_time.second == expected_result.second


def test_get_idx_else_none() -> None:
    lst = [1, 2, 3]
    assert waituntil.get_idx_else_none(lst, 0) == 1
    assert waituntil.get_idx_else_none(lst, -1) == 3
    assert waituntil.get_idx_else_none(lst, 3) is None
    assert waituntil.get_idx_else_none(lst, 5) is None
