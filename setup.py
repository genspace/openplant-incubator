import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openplant",
    version="0.0.1",
    author="Genspace",
    description="Open Plant Incubator",
    url="https://github.com/genspace/openplant-incubator",
    packages=setuptools.find_packages(
        include=[
            'app', 'app.*'
        ]
    ),
    package_dir= {
        '': 'v2'
    },
    entry_points={
        'console_scripts': [
            'test-incubator=app.incubator.raspberrypi.test:main'
        ]
    },
    install_requires=[
        'sqlalchemy',
        'adafruit-circuitpython-htu21d',
        'picamera',
        'loguru',
        'adafruit-blinka',
        'RPI.GPIO'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)