import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="client-bittrex-api",
    version="0.0.1",
    author="Ruben Colomina",
    author_email="rcolomina@gmail.com",
    description="This is a client to perfrom public and private queries to Bittrex API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rcolomina/python_client_bittrex_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
