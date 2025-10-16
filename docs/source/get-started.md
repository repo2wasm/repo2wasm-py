# Get started

This tutorial guides you through installing `repo2wasm` and building your first environment image.

## Dependencies

You must have

- [Mamba](https://github.com/mamba-org/mamba) package manager
- [Python](https://www.python.org/) with [pip](https://pypi.org/project/pip/)

installed in your machine.

## Install `repo2wasm`

Run

```bash
python -m pip install repo2wasm
```

## Build a repository with `repo2wasm`

 We'll use a fork of [Binder `requirements` example](https://github.com/repo2wasm/requirements), which installs a Python environment. Run

 ```bash
 repo2wasm https://github.com/repo2wasm/requirements
 ```