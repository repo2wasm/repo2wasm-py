import logging

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)


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
        "-o",
        "--output-dir",
        default="public",
        help="The directory to write the files.",
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
        help="Git repository to build. Default to current directory.",
    )

    args = parser.parse_args()

    if args.version:
        from . import __version__

        print(__version__)
        exit()

    repo2wasm(args.repository, ide=args.ide, output_dir=args.output_dir)
