import importlib.metadata

def main():
    display_eps = importlib.metadata.entry_points(group='timmins.display')
    try:
        print(display_eps)
        display = display_eps[0].load()
        display('Hello world')
    except IndexError:
       default_output('Hello world - Im default')
    
    
def default_output(output: str) -> None:
    print(output)