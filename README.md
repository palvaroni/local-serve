# What is it?

A python based application for serving static files locally.

Can be compiled into an executable with
```
python -m pip install pyinstaller
pyinstaller -F serve.py
```

Serve with `serve.exe -p <rootPath>`. The `rootPath` parameter is defined relative to, and defaults to the current working directory.

## How to use
1. Download `run.exe` from the latest release.
2. Put `run.exe` into the directory that contains the files to serve.
3. Create `index.html` to the root if it does not exist.
4. Run the executable.
5. Navigate to `localhost:5000` with any browser.
