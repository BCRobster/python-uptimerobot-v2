import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uptimerobot.py",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="python-uptimerobot-APIv2 implementation",
    long_description=long_description,
    long_description_content_type="python-uptimerobot-APIv2 is an Uptime Robot http://uptimerobot.com integration for your Python project, implementing uptimerobot API v2 version.",
    url="https://github.com/pypa/change",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)