import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omorfi", # Replace with your own username
    version="0.0.1",
    author="Flammie A Pirinen",
    author_email="flammie@iki.fi",
    description="Open morphology for Finnish, python bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flammie/omorfi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['hfst'],
)
