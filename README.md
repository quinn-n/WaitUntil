## WaitUntil

This is a Python script which waits until a given time, and then exits cleanly. I use it to delay execution of other programs using `&&`.

### Installation

The easy way:

- Download a binary built with pyinstaller from the releases page
- Put it in a folder on your `$PATH`

The hard way:

- Clone the repository
- Create a new virtual environment with ``pew new -a `pwd` .``
- Install poetry with `pip install poetry`
- Install the dependencies with `poetry install --without dev`
- Run the script with `py waituntil.py`

### Usage

waituntil can wait until a specific date or for a specific amount of time.

To wait until a specific date / time, invoke waituntil and provide the date in ISO8601 format:

`waituntil "2024-06-17 16:00:00"`

If you only want to wait until a certain time on the same day, you can pass `--today` and waituntil will auto-insert today's date into the ISO8601 string.

`waituntil --today 16:00:00`

If you want to wait a certain amount of time rather than until a certain date, add the `--waitfor` flag.

`waituntil --waitfor 5:00`
