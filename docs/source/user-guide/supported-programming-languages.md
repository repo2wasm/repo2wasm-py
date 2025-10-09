(supported-programming-languages)=

# Supported programming languages

`repo2wasm` only suports programming languages already compiled to Wasm.

## Python

| Version | Available | Latest release if available | Latest release date |
| --- | --- | --- | --- |
| 3.14 | ❌ | | |
| 3.13 | ✔️ | 3.13.1 | 2024-12 |
| 3.12 | ❌ | | |
| 3.11 | ❌ | | |
| 3.10 | ❌ | | |
| 3.9  | ❌ | | |

## R

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

[`tidyverse`] is a collection of R packages popular in data science. Unfortunately, [`tidyverse`] is not available at `repo2wasm` because [`lubridate`](https://cran.r-project.org/web/packages/lubridate/index.html), one of the packages in of [core `tidyverse`], is missing. All other packages from [core `tidyverse`] are available.

```{note}
Visit [jupyterlite/jupyterlite#1753](https://github.com/jupyterlite/jupyterlite/discussions/1753) for updated regarding the availability of `tidyverse`.
```

[`tidyverse`]: https://cran.r-project.org/web/packages/tidyverse/index.html
[core `tidyverse`]: https://www.tidyverse.org/packages/#core-tidyverse