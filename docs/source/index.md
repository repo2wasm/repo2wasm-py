# `repo2wasm` documentation

`repo2wasm` is a clone of [`jupyter-repo2docker`] targeting [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly) (Wasm) environment. If [`jupyter-repo2docker`] is a wrapper around [Docker Engine](https://docs.docker.com/engine/), `repo2wasm` is a wrapper around [JupyterLite].

```{important}
Only programming languages already compiled to Wasm are supported, more details in the section "[](#supported-programming-languages)".
```

Like [`jupyter-repo2docker`], `repo2wasm` provides [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) in the form of [JupyterLite] as integrated development environment (IDE) out of the box. Support to other environments are planned for the future. Different than [`jupyter-repo2docker`], `repo2wasm` provides a single integrated development environment (IDE) per build.

[`jupyter-repo2docker`] supports a large number of [configuration files](https://repo2docker.readthedocs.io/en/latest/configuration/) and only a subset is supported by `repo2wasm` because of the nature of `repo2wasm`, more details in the section "[](#supported-configuration-files)".

```{toctree}
:maxdepth: 2
:caption: Table of Contents

get-started/index.md
limitations.md
user-guide/index.md
common-errors/index.md
contributor-guide/index.md
changelog.md
```

[`jupyter-repo2docker`]: https://github.com/jupyterhub/repo2docker
[JupyterLite]: https://jupyterlite.readthedocs.io/