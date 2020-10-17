import os
import configparser
from loguru import logger
from incubator.raspberrypi.config import DEFAULT_CONFIG_PARAMS


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS = os.path.join(SCRIPT_DIR, 'requirements.txt')
BASE_CONFIG = os.path.join(SCRIPT_DIR, 'base.ini')
GPG_SECRET = os.path.join(SCRIPT_DIR, 'db.env.gpg')
DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser('~/incubator.ini'))
DEFAULT_CRED_PATH = os.path.join(os.path.expanduser('~/db.env'))


def say_hello():
    logger.info("Hello, friend!")
    return None


def install_requirements():
    os.system(f"pip3 install --update -r {REQUIREMENTS}")
    return None


def set_config():
    # get base config and specify config / cred path
    base_config = configparser.ConfigParser()
    base_config.read(BASE_CONFIG)
    config_path = input(f"Set config path [{DEFAULT_CONFIG_PATH}]:") or DEFAULT_CONFIG_PATH
    base_config['BASE']['config_path'] = config_path
    cred_path = input(f"Set cred path [{DEFAULT_CRED_PATH}]:") or DEFAULT_CRED_PATH
    base_config['BASE']['cred_path'] = cred_path
    # use gpg to unpack secrets
    if not os.path.exists(cred_path):
        logger.info(f"Unpacking secrets to: {cred_path}")
        os.system(f'cp {GPG_SECRET} {cred_path}.gpg')
        os.system(f'gpg {cred_path}.gpg')
        os.system(f'rm {cred_path}.gpg')
    # write config
    with open(BASE_CONFIG, 'w') as fin:
        base_config.write(fin)
    # read config file
    config = configparser.ConfigParser()
    config.read(config_path)
    # update defaults
    if 'INCUBATOR' in config:
        DEFAULT_CONFIG_PARAMS.update(dict(config['INCUBATOR']))
    else:
        config['INCUBATOR'] = {}
    # check with user for input
    for k, val in DEFAULT_CONFIG_PARAMS.items():
        uval = None
        while not uval:
            uval = input(f"{k} [{val}]: ") or (str(val) if val else "")
        config['INCUBATOR'][k] = uval
    # write to file
    with open(config_path, 'w') as fin:
        config.write(fin)
