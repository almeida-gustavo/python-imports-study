from setuptools import setup


setup(
    name='timmins_plugin_fancy',
    version='1',
    entry_points={
        'timmins.display': [
            'excl=app_sub_folder.timmins_plugin_fancy:excl_display', 
            'lined = app_sub_folder.timmins_plugin_fancy:lined_display',
        ],
    }
)