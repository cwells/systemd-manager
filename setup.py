from setuptools import setup, find_packages

setup(
    name = "systemd-manager",
    version = "0.1.2",
    license = "BSD-3",
    author = "Cliff Wells",
    author_email = "cliff.wells@gmail.com",
    url = "https://github.com/cwells/systemd-manager",
    packages = find_packages(exclude=["tests"])
)
