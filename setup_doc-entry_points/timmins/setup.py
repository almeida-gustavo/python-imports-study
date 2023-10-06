from setuptools import setup


setup(
    name='timmins',
    version='1',
    entry_points={
        'console_scripts': ['hello-world=app_sub_folder.timmins:main'],
        # 'timmins.display': ['default = my_name:default_output'],
    }
)