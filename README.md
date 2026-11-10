# CaptureMock self-tests

These are the [TextTest](https://www.texttest.org) tests for
[CaptureMock](https://github.com/texttest/capturemock). The TextTest application name is `cpmock`.

The tests run entirely from a Python virtual environment. TextTest's "checkout" (`-c`) is the venv itself,
not the CaptureMock source tree: the tests run the venv's `capturemock` script and its Python, and
put the venv's `bin` (or `Scripts` on Windows) directory first on `PATH`.

## Setting up

Create a venv and install CaptureMock into it. Install it in editable mode if you want the tests to pick up
changes to the source without reinstalling. Then install the third-party packages some tests need:

```
python -m venv capturemock_venv
capturemock_venv/bin/pip install -e ../capturemock
capturemock_venv/bin/pip install -r requirements.txt
```

On Windows, use `capturemock_venv\Scripts\pip` instead.

You can create several venvs, one for each Python version you want to test against.

## Running

Run the tests with TextTest, pointing the checkout at the venv:

```
texttestc -c /path/to/capturemock_venv -b local -d /path/to/capturemock-selftest -a cpmock
```

Alternatively, start the TextTest UI and point it at your venv via "Use checkout" in the Running tab.
