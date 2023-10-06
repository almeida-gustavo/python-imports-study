This repo is implementing code from https://setuptools.pypa.io/en/latest/userguide/entry_point.html#entry-points-for-plugins

It is slightly different since the code itself from the link was not working as expected, maybe because the code was inside __main__?


### Steps to get this project ready
```
1. go inside the timmins folder
2. pip install ../timmins_plugin_fancy
3. pip install -e .
```

### Run
- On the terminal you can run `hello-world` and it will print the result
- Or you can open `python` and run the following code
  ```
    >>> from app_sub_folder.timmins import main
    >>> main()
  ```