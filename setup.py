import os
import setuptools
from setuptools.command.install import install

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        if os.path.exists('~/.profile'):
            os.system('source ~/.profile')
        os.system('install-requirements')
        os.system('set-config')


setuptools.setup(
    name="openplant",
    version="0.0.42",
    author="Genspace",
    description="Open Plant Incubator",
    cmdclass={
        'install': PostInstallCommand
    },
    long_description=long_description,
    url="https://github.com/genspace/openplant-incubator",
    packages=setuptools.find_packages(where="./v2/app"),
    package_dir= {
        '': 'v2/app'
    },
    entry_points={
        'console_scripts': [
            'say-hello=incubator.raspberrypi.scripts:say_hello',
            'install-requirements=incubator.raspberrypi.scripts:install_requirements',
            'set-config=incubator.raspberrypi.scripts:set_config',
            'incubate-me=incubator.raspberrypi.basic_all:main'
        ]
    },
    install_requires=[
        'loguru',
        'cowsay',
        'python-dotenv'
    ],
    package_data={
        "incubator": [
            "raspberrypi/*.txt",
            "raspberrypi/*.ini",
            "raspberrypi/*.gpg",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)