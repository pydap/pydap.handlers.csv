from setuptools import setup, find_packages
import sys, os


version = '0.2'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    "Pydap>=3.2",
]


setup(name='pydap.handlers.csv',
    version=version,
    description="A handler that allows Pydap to server CSV files.",
    long_description="""
This handler allows Pydap to serve data from a file with comma separated
values. Here's a simple example:

.. code-block:: bash

    $ cat simple.csv
    "index","temperature","site"
    10,15.2,"Diamond_St"
    11,13.1,"Blacktail_Loop"
    12,13.3,"Platinum_St"
    13,12.1,"Kodiak_Trail"

Note that strings must be explicitely quoted. Additional metadata may be added
by creating a JSON file with the same name (`simple.csv.json` in this case):

.. code-block:: json

    {
        "sequence": {
            "temperature": {
                "units": "degC"
            }
        }
    }

""",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='csv opendap pydap dap data access',
    author='Roberto De Almeida',
    author_email='roberto@dealmeida.net',
    url='https://github.com/robertodealmeida/pydap.handlers.csv',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['pydap', 'pydap.handlers'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [pydap.handler]    
        csv = pydap.handlers.csv:CSVHandler
    """,
)
