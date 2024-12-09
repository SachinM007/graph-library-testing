from setuptools import setup, find_packages

setup(
    name='graph-library-testing',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
    author='Sachin Miryala',
    author_email='sm4335@nau.edu',
    description='A comprehensive graph library with advanced algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    install_requires=[],
    
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'mutmut',
            'tstl'
        ]
    },
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    
    project_urls={
        'Source': 'https://github.com/SachinM007/graph-library-testing',
        'Bug Reports': 'https://github.com/SachinM007/graph-library-testing/issues'
    }
)
