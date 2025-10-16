(supported-configuration-files)=

# Supported configuration files

## Users

### `environment.yml`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.3.0](https://img.shields.io/badge/version-0.3.0-blue)

```{note}
The Python kernel is always installed when using `environment.yml` because, different than R, the Python packages don't have its own namespace.
```

More details in [repo2docker > User guide > environment.yml - Install a conda environment](https://repo2docker.readthedocs.io/en/latest/configuration/research/#environment-yml-install-a-conda-environment).

### `requirements.txt`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.4.0](https://img.shields.io/badge/version-0.4.0-blue)

```{important}
The dependencies are installed from [conda-forge] instead of [PyPI](https://pypi.org/).
```

More details in [repo2docker > User guide > requirements.txt - Install a Python environment](https://repo2docker.readthedocs.io/en/latest/configuration/development/#requirements-txt-install-a-python-environment).

### `install.R`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.4.0](https://img.shields.io/badge/version-0.4.0-blue)

```{important}
The dependencies are installed from [conda-forge] instead of [CRAN](https://cran.r-project.org/).
```

More details in [repo2docker > User guide > install.R - Install R packages](https://repo2docker.readthedocs.io/en/latest/configuration/research/#install-r-install-r-packages).

### `Project.toml`

![status: not planned](https://img.shields.io/badge/status-not_planned-red)

More details in [repo2docker > User guide > Project.toml - Install a Julia environment](https://repo2docker.readthedocs.io/en/latest/configuration/research/#project-toml-install-a-julia-environment).

## Package Developers

### `Pipfile` and/or `Pipfile.lock`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

More details in [repo2docker > User guide > Pipfile and/or Pipfile.lock - Install a Python environment](https://repo2docker.readthedocs.io/en/latest/configuration/development/#pipfile-and-or-pipfile-lock-install-a-python-environment).

### `setup.py`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

More details in [repo2docker > User guide > setup.py - Install Python packages](https://repo2docker.readthedocs.io/en/latest/configuration/development/#setup-py-install-python-packages).

### `DESCRIPTION`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

More details in [repo2docker > User guide > DESCRIPTION - Install as an R package](https://repo2docker.readthedocs.io/en/latest/configuration/research/#description-install-as-an-r-package).

## System-wide configuration

### `apt.txt`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

More details in [repo2docker > User guide > apt.txt - Install packages with apt-get](https://repo2docker.readthedocs.io/en/latest/configuration/system/#apt-txt-install-packages-with-apt-get).

### `runtime.txt`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

More details in [repo2docker > User guide > runtime.txt - Specifying runtimes](https://repo2docker.readthedocs.io/en/latest/configuration/system/#runtime-txt-specifying-runtimes).

### `default.nix`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

More details in [repo2docker > User guide > default.nix - the nix package manager](https://repo2docker.readthedocs.io/en/latest/configuration/system/#default-nix-the-nix-package-manager).

### `Dockerfile`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

More details in [repo2docker > User guide > Dockerfile - Advanced environments](https://repo2docker.readthedocs.io/en/latest/configuration/system/#dockerfile-advanced-environments).

## Post-build actions

### `postBuild`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

More details in [repo2docker > User guide > postBuild - Run code after installing the environment](https://repo2docker.readthedocs.io/en/latest/configuration/actions/#postbuild-run-code-after-installing-the-environment).

### `start`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

More details in [repo2docker > User guide > start - Run code before the user sessions starts](https://repo2docker.readthedocs.io/en/latest/configuration/actions/#start-run-code-before-the-user-sessions-starts).

[conda-forge]: https://conda-forge.org/