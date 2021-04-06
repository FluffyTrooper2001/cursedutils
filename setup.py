import pathlib
from setuptools import setup
HERE=pathlib.Path(__file__).parent
README=(HERE/"README.md").read_text()
setup(
    name="cursedutils",
    version="4.2.1",
    description="Do unholy things to python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/FluffyTrooper2001/cursedutils",
    author="FluffyTrooper2001",
    author_email="michaelisaiah01@gmail.com",
    license="XD License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ],
    packages=['cursedutils'],
    include_package_data=True,
    entry_points={"console_scripts":["cursedutils=cursedutils.__main__:main"]})
