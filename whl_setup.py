import subprocess
import sys
import types
import os

import site
if not os.path.isdir('.setup_requires'):
    os.mkdir('.setup_requires')

site.addsitedir('.setup_requires')
sys.path.insert(0, sys.path.pop())


# VERSION GOES HERE


class Lazy(object):

    @staticmethod
    def resolve(obj):
        if isinstance(obj, Lazy):
            return obj.func()
        else:
            return obj

    def __init__(self, func):
        self.func = func


def setup(**kwargs):
    setup_requires = Lazy.resolve(kwargs.pop('setup_requires', None))
    if setup_requires:
        try:
            subprocess.check_output([
                sys.executable, __file__,
                'install', '--target', '.setup_requires'] + setup_requires,
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as ex:
            print(ex.command)
            print(ex.output)
            sys.exit(exself.returncode)

    from setuptools import setup as real_setup
    real_kwargs = {name: Lazy.resolve(value) for name, value in kwargs.items()}
    return real_setup(**real_kwargs)


def get_existing_version(path):
    if not os.path.isfile(path):
        return None
    with open(path) as fp:
        lines = list(fp)
    version = next((x for x in lines if x.startswith('__version__')), None)
    if version is None:
        return object
    return version[version.find("'"):].strip("'\n")


def install():
    from pkg_resources import get_distribution
    new_version = get_distribution('whl.setup').version
    version = get_existing_version('whl_setup.py')
    if version is object:
        return
    print(new_version, version)
    import inspect
    import whl_setup
    source = inspect.getsource(whl_setup).replace(
        "# VERSION GOES HERE", "__version__ = '%s'" % new_version)
    with open('whl_setup.py', 'w') as fp:
        fp.write(source)



if __name__ == '__main__' and sys.argv[1] == 'install':
    from pip import main

    main(sys.argv[1:])
