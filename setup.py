from setuptools import setup


setup(
    name = 'wm_flow_creation', 
    version = '0.1.0',
    description = 'This is a module to automatically partition an array of records into multiple buckets in the most optimal manner',
    py_modules = ["wm_flow_creation"],
    package_dir = {'':'src'},
    author = 'Walmart Global Tech',
    author_email = 'mohsin.kaleem@walmart.com',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/jinhangjiang/morethansentiments',
    include_package_data=True,
    keywords = ['Algorithm', 'Partition', 'Array', 'Flow','Binary Search'],
)
