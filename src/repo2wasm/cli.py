import logging

logger = logging.getLogger(__name__)


def cli():
    import argparse

    from .repo2wasm import repo2wasm

    parser = argparse.ArgumentParser(
        prog="repo2wasm",
        description="Convert Git repository into integrated development environment (IDE) powered by Wasm.",
    )

    parser.add_argument(
        "--ide",
        choices=["jupyterlab"],
        default="jupyterlab",
        help="The integrated development environment (IDE) to configure.",
    )

    parser.add_argument(
        "-f",
        "--forgiving",
        action="store_true",
        help="Ignore the provided version number given that only a few versions are available in Wasm.",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        default="public",
        help="The directory to write the files.",
    )

    logging_level = parser.add_mutually_exclusive_group()
    logging_level.add_argument(
        "--info",
        action="store_true",
        help="Increase logging to info level.",
    )
    logging_level.add_argument(
        "--debug",
        action="store_true",
        help="Increase logging to debug level.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Print the version and exit.",
    )

    parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Repository to build. Default to current directory.",
    )

    args = parser.parse_args()

    if args.version:
        from . import __version__

        print(__version__)
        exit()

    if args.info:
        selected_logging_level = logging.INFO
    elif args.debug:
        selected_logging_level = logging.DEBUG
    else:
        selected_logging_level = logging.WARNING

    logging.basicConfig(encoding="utf-8", level=selected_logging_level)

    repo2wasm(
        args.repository,
        ide=args.ide,
        output_dir=args.output_dir,
        forgiving=args.forgiving,
    )
