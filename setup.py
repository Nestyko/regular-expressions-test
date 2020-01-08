
from setuptools import setup

# # TODO: ugly hack for old nosetests runner
# if '--with-xunit' in sys.argv:
#     sys.argv.remove('--with-xunit')

# packages = [
#   'pytest==4.6.4',
#   'pytest-timeout==1.3.3',
#   'pytest-runner',
# ]

setup(
    name='regex_excercises',
    version='1.0.0',
    author='Nestor Tobon',
    author_email='ntobon@truelogic.software',
    # packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    zip_safe=False,
    # install_requires=packages + [
    #     'wheel',
    #     'setuptools==41.0.1',
    # ],
    # setup_requires=packages,
    # tests_require=packages,
)
