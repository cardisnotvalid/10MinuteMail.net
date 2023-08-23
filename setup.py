from setuptools import setup, find_packages


setup(
    name="temp_mail",
    version="0.1",
    description="Simple API wrapper 10MinuteMail.net.",
    url="https://github.com/cardisnotvalid/10MinuteMail.net",
    keywords="temporary temp mail email address wrapper api anon 10minutemail",
    author="Danil Cardinal",
    author_email="deadcardinal293@gmail.com",
    include_package_data=True,
    packages=find_packages(),
    install_requires=["requests", "pydantic"],
    py_modules=["temp_mail.temp_mail"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet"
    ],
    license="MIT"
)