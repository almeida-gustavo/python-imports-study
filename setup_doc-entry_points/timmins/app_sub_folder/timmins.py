import importlib.metadata

def main():
    display_eps = importlib.metadata.entry_points(group='timmins.display')
    try:
        print(display_eps)
        display = display_eps["excl"].load()
        # This lined is the value on /setup_doc-entry_points/timmins_plugin_fancy/setup.py
        # display = display_eps["lined"].load()
        display('Hello world')
    except IndexError:
       default_output('Hello world - Im default')
    
    
def default_output(output: str) -> None:
    print(output)