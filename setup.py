import os
import time
import setuptools
import subprocess
import distutils.cmd
import distutils.log


with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(distutils.cmd.Command):
    """Post-installation for installation mode."""
    def run(self):
        self.announce('Sourcing local profile', level=distutils.log.INFO)
        if os.path.exists('~/.profile'):
            subprocess.check_call(['source', '~/.profile'])
        self.announce('Please set config', level=distutils.log.INFO)
        time.sleep(5)
        subprocess.check_call(['set-config'])


setuptools.setup(
    name="openplant",
    version="0.1.6",
    author="Genspace",
    description="Open Plant Incubator",
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
            'test-camera=incubator.raspberrypi.scripts:test_camera',
            'incubate-me=incubator.raspberrypi.basic_all:main'
        ]
    },
    install_requires=[
        'loguru',
        'cowsay',
        'python-dotenv',
        'sqlalchemy',
        'adafruit-circuitpython-htu21d',
        'picamera',
        'adafruit-blinka',
        'RPI.GPIO',
        'pymysql'
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
