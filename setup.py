from setuptools import setup

setup(
    name="rss",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Command-line RSS manager.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/rss",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["rss"],
    install_requires=[
        "mysql.connector",
        "colr",
        "questionary",
        "click",
    ],
    include_package_data=True,
)
