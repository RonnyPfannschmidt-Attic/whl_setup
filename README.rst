whl_setup
===========


an experiment to replace ez_setup and setup_requires with something that works
the provided mechanism adds a python path where very recent seupptools and setuptools extensions can be installed

installation::

    pip install -U whl_setup
    whl_setup_script_install


usage::

    # setup.py

    from whl_setup import setup, Lazy

    @Lazy
    def extensions():
        from setuptools import Extension
        return [...]

    if __name__ = '__main__':
        setup(
            ...
            use_scm_version=True,
            setup_requires=[
                'setuptools',
                'setuptools_scm'
            ]
            extensions=extensions,
            ...
        )
