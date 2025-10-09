(supported-configuration-files)=

# Supported configuration files

## Users

### `environment.yml`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.3.0](https://img.shields.io/badge/version-0.3.0-blue)

```{note}
The Python kernel is always installed when using `environment.yml` because, different than R, the Python packages don't have its own namespace.
```

### `requirements.txt`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.4.0](https://img.shields.io/badge/version-0.4.0-blue)

```{important}
The dependencies are installed from [conda-forge] instead of [PyPI](https://pypi.org/).
```

### `install.R`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.4.0](https://img.shields.io/badge/version-0.4.0-blue)

```{important}
The dependencies are installed from [conda-forge] instead of [CRAN](https://cran.r-project.org/).
```

### `Project.toml`

![status: not planned](https://img.shields.io/badge/status-not_planned-red)

### `Pipfile` and/or `Pipfile.lock`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

## Package Developers

### `Pipfile` and/or `Pipfile.lock`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

### `setup.py`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

### `DESCRIPTION`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

## System-wide configuration

### `apt.txt`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

### `runtime.txt`

![status: not implemented](https://img.shields.io/badge/status-not_implemented-pink)

### `default.nix`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

### `Dockerfile`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

## Post-build actions

### `postBuild`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

### `start`

![status: not supported](https://img.shields.io/badge/status-not_supported-red)

[conda-forge]: https://conda-forge.org/