from Cython.Build import cythonize
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension  # lint:ok

extension_modules = [
        Extension('examples.cython.std_dev_pure', ['examples/cython/std_dev_pure.py']),
        Extension('examples.cython.std_dev_cython', ['examples/cython/std_dev_cython.pyx'])
    ]

setup(
    ext_modules=cythonize(extension_modules)
)
