import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openplant",
    version="0.0.42",
    author="Genspace",
    description="Open Plant Incubator",
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