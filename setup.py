from setuptools import setup, find_packages


setup(
    name="temp_mail",
    version="0.1.0",
    description="Simple API wrapper 10MinuteMail.net.",
    url="https://github.com/cardisnotvalid/10MinuteMail.net",
    author="Danil Cardinal",
    author_email="deadcardinal293@gmail.com",
    include_package_data=True,
    packages=find_packages(),
    install_requires=["requests", "pydantic"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet"
    ]
)