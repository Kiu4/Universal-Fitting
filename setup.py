import os 

from setuptools import find_namespace_packages, setup
cwd = os.path.abspath(os.path.dirname(__file__))

###
# get description from README.md
###
with open(os.path.join(cwd, "README.md"), encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    # published project name
    name="tcspcfit",

    # from dev to release
    #   bumpversion release
    # to next version
    #   bump patch/minor/major
    version='0.0.1.dev',

    # one-line description for the summary field
    description="TCSPC fitting",

    long_description=long_description,
    long_description_content_type='text/markdown',

    # project homepage
    url="https://github.com/Kiu4/TCSPC-Fit",

    # name or organization
    author="Homo sapiens",

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research'
    ],

    keywords="tcspc",

    packages=find_namespace_packages(include=['tcspcfit.*']),

    python_requires='>=3.6',

    # use pyproject.toml to define build system requirement
    #setup_requires=[
    #],

    # other packages the project depends on to run
    #   install_requires -> necessity
    #   requirements.txt
    install_requires=[
        # core

        # numeric and processing
        'numpy',
        'scipy',
        'pandas',

        # utils
        'click',
        'coloredlogs',
        'tqdm'
    ],

    # additional groups of dependencies here for the "extras" syntax
    extras_require={
    },

    # data files included in packages
    package_data={
    },
    # include all package data found implicitly
    #include_package_data=True,

    # data files outside of packages, installed into '<sys.prefix>/my_data'
    data_files=[
    ],

    # executable scripts
    entry_points={
        'console_scripts': [
        ]
    }, 

    # contains c source, cannot safely run in compressed form
    zip_safe=True
)
