(supported-programming-languages)=

# Supported programming languages

`repo2wasm` only suports programming languages already compiled to Wasm, packaged by the [`emscripten-forge` organisation on GitHub](https://github.com/emscripten-forge), and available on the [`emscripten-forge-dev` channel hosted by Prefix.dev GmbH](https://prefix.dev/channels/emscripten-forge-dev). 

## Python

```{note}
Check the [`python` package](https://prefix.dev/channels/emscripten-forge-dev/packages/python) for updated information.
```

| Version | Available | Latest release if available | Latest release date |
| --- | --- | --- | --- |
| 3.14 | ❌ | | |
| 3.13 | ✔️ | 3.13.1 | 2024-12 |
| 3.12 | ❌ | | |
| 3.11 | ❌ | | |
| 3.10 | ❌ | | |
| 3.9  | ❌ | | |

## R

```{note}
Check the [`r-base` package](https://prefix.dev/channels/emscripten-forge-dev/packages/r-base) for updated information.
```

| Version | Available | Latest release if available | Latest release date |
| --- | --- | --- | --- |
| 4.5 | ✔️ | 4.5.1 | 2025-06 |
| 4.4 | ✔️ | 4.4.3 | 2025-03 
| 4.3 | ❌ | | |
| 4.2 | ❌ | | |
| 4.1 | ❌ | | |
| 4.0 | ❌ | | |
| 3.6 | ❌ | | |

### `tidyverse`

[`tidyverse`] is a collection of R packages popular in data science. Unfortunately, [`tidyverse`] is not available at `repo2wasm` because some packages depend on `curl` that is not available.

```{note}
Visit [jupyterlite/jupyterlite#1753](https://github.com/jupyterlite/jupyterlite/discussions/1753) for updated regarding the availability of `tidyverse`.
```

[`tidyverse`]: https://cran.r-project.org/web/packages/tidyverse/index.html
[core `tidyverse`]: https://www.tidyverse.org/packages/#core-tidyverse