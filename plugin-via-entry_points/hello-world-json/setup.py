from setuptools import setup


setup(
    name='hello-world-json',
    version='1',
    py_modules=['hello_world_json'],
    entry_points={
        # This this_name_can_be_what_i_want.output has to be the same name as you put on the other repo
        # you are linking... this name can be whatever you want
        'this_name_can_be_what_i_want': ['json=hello_world_json:json_output'],
    },
)