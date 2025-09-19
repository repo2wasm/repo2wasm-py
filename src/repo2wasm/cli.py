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
        action='store_true',
        help="Print the version and exit.",
    )

    args = parser.parse_args()

    if args.version:
        from . import __version__
        
        print(__version__)

    repo2wasm(ide=args.ide, output_dir=args.output_dir)
