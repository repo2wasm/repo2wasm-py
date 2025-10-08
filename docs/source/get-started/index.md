# Get started

This tutorial guides you through installing `repo2wasm` and building your first environment image.

## Dependencies

- [Mamba](https://github.com/mamba-org/mamba) package manager
- [Python](https://www.python.org/)

## Install `repo2wasm`

Run

```bash
python -m pip install repo2wasm
```

## Build a repository with `repo2wasm`

 We'll use the [Binder `conda` example](https://github.com/binder-examples/conda), which installs a Python environment. Run

 ```bash
 repo2wasm https://github.com/binder-examples/conda
 ```