#!python3

import argparse
import logging
import os
import platformdirs
from . import Engine, Config, test

"""The command line arguments"""
args = None


def main():
    """Perform command line steamback operations"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Show debug log messages",
                        action="store_true")
    parser.add_argument("--test", help="Run integration code test",
                        action="store_true")

    global args
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    logger = logging.getLogger()
    logger.info(f'Steamback running...')

    # FIXME - I bet the following will need tweaking for Windows
    steam_dir = os.path.join(os.path.expanduser(
        "~"), ".steam", "debian-installation")

    app_name = "steamback"
    app_author = "geeksville"
    app_dir = platformdirs.user_data_dir(app_name, app_author)

    config = Config(logger, app_dir, steam_dir)
    e = Engine(config)
    if args.test:
        test.testAll(e)


if __name__ == "__main__":
    main()
