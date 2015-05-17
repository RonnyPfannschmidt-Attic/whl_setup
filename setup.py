"""



"""


from whl_setup import setup, Lazy

@Lazy
def long_description():
    with open('README.rst') as fp:
        return fp.read()


if __name__ == '__main__':
    setup(
        name='whl.setup',
        description='a pip based replacement for ez_setup and setup_requires',
        long_description=long_description,
        use_scm_version=True,
        setup_requires=[
            'setuptools',
            'setuptools_scm',
        ],
        entry_points={
            'console_scripts': {
                'whl_setup_script_install = whl_setup:install',
            }

        },
        py_modules=[
            'whl_setup',
        ],
    )
