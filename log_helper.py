import logging
import os
import shutil
from pathlib import Path


def init_log(name):
    if not os.path.exists('log'):
        os.makedirs('log')
    FORMAT = '%(asctime)-15s - %(levelname)s - %(name)s - %(message)s'
    formatter = logging.Formatter(FORMAT)
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    file_path = 'log/' + name + '.log'
    fh = logging.FileHandler(file_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Stream Handler doesn't seem to be doing much.
    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger


def delete_log(name):
    path = 'log/' + name + ".log"
    file = Path(path)
    if file.is_file():
        os.remove(path)
        logging.getLogger('logging').info("delete_log: %s deleted", name)
    else:
        logging.getLogger('logging').info("delete_log: %s doesn't exist", path)


def purge_logs(ask=True):
    if not ask:
        if os.path.exists('log'):
            shutil.rmtree('log')
            print("All logs were deleted. I hope you know what you're doing.")
        return
    in1 = input("Are you sure to delete ALL logs? [y/N]")
    if in1 == 'y' or in1 == 'Y':
        if os.path.exists('log'):
            shutil.rmtree('log')
            print("All logs were deleted. I hope you know what you're doing.")