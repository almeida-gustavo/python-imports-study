from setuptools import setup


setup(
    name='hello-world',
    version='1',
    entry_points={
        # This hello-world is the name of the script you can use on the terminal
        # This console_scripts can not be the name you want... this is a pattern that you must follow
        'console_scripts': ['hello-world=hello_world:main'],
        
        # This is another method that is standard.
        'gui_scripts': ['my-method-name = second_level.hello_guid:hello_world'],
        
        
        # This is just for you to add an default value to when it is loading the entry_points. You can add whatever name you want, but this name will need to be included on the entry_points of the package you have installed... 
        # You add a default value just so it doesn't fail when you run the command    
        # eps = importlib.metadata.entry_points()['this_name_can_be_what_i_want']

        'this_name_can_be_what_i_want': ['default=hello_world:default_output'],
    }
)