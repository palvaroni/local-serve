A python based application for serving static files locally.

Can be compiled into an executable with
```
python -m pip install pyinstaller
pyinstaller -F serve.py
```

Serve with `serve.exe -p <rootPath>`. The `rootPath` parameter is defined relative to, and defaults to the current working directory.
