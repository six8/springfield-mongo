from distutils.core import setup

def main():
    setup(
        name = 'springfield-mongo',
        packages=['springfield_mongo'],
        package_dir = {'springfield_mongo':'springfield_mongo'},
        version = open('VERSION.txt').read().strip(),
        author='Mike Thornton',
        author_email='six8@devdetails.com',
        url='',
        download_url='',
        keywords=['packaging'],
        license='MIT',
        description='',
        classifiers = [
            "Programming Language :: Python",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        long_description=open('README.rst').read(),
        install_requires = [
            'springfield>=0.7.6',
            'pymongo'
        ]
    )

if __name__ == '__main__':
    main()
