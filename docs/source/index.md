# `repo2wasm` documentation

`repo2wasm` is a clone of [`jupyter-repo2docker`] targeting [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly) (Wasm) environment.

[`jupyter-repo2docker`] supports a large number of [configuration files](https://repo2docker.readthedocs.io/en/latest/configuration/) and only a subset is supported by `repo2wasm` because of the nature of `repo2wasm`. `repo2wasm` has no plans to support

- [`apt.txt`](https://repo2docker.readthedocs.io/en/latest/configuration/system/#apt-txt-install-packages-with-apt-get)
- [`default.nix`](https://repo2docker.readthedocs.io/en/latest/configuration/system/#default-nix-the-nix-package-manager)
- [`Dockerfile`](https://repo2docker.readthedocs.io/en/latest/configuration/system/#dockerfile-advanced-environments)
- [`postBuild`](https://repo2docker.readthedocs.io/en/latest/configuration/actions/#postbuild-run-code-after-installing-the-environment)
- [`start`](https://repo2docker.readthedocs.io/en/latest/configuration/actions/#start-run-code-before-the-user-sessions-starts)

```{toctree}
:maxdepth: 2
:caption: Table of Contents

architecture.md
jupyterlite.md
```

[`jupyter-repo2docker`]: https://github.com/jupyterhub/repo2docker