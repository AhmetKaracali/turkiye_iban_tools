from setuptools import setup, find_packages

setup(
    name='turkiye_iban_tools',
    version='0.1.0',
    author='Ahmet KARAÇALI',
    author_email='akaracali58@gmail.com',
    description='IBAN Verification and information tools for IBAN numbers in Turkiye',
    long_description=open('README_EN.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AhmetKaracali/turkiye_iban_tools',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True
)