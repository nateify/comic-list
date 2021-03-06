import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comic-list",
    version="0.2",
    author="nateify",
    author_email="nateify@users.noreply.github.com",
    description="Outputs list of missing comic book issue files in a folder given a range",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nateify/comic-list",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'comic-list = scripts.main:cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.2",
)
