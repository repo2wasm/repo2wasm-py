# `tidyverse`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.5.0](https://img.shields.io/badge/version-0.5.0-blue)

[`tidyverse`] is a collection of R packages popular in data science. Unfortunately, [`tidyverse`] is not available at `repo2wasm` because some packages depend on `curl` that is not available.

```{note}
Visit [jupyterlite/jupyterlite#1753](https://github.com/jupyterlite/jupyterlite/discussions/1753) for updated regarding the availability of `tidyverse`.
```

## Problematic Code

```yaml
name: r
dependencies:
  - r-tidyverse
```

## Correct Code

Only load the parts of `tidyverse` that are used.

```yaml
name: r
dependencies:
  - r-dplyr
  - r-ggplot2
```

[`tidyverse`]: https://cran.r-project.org/web/packages/tidyverse/index.html
[core `tidyverse`]: https://www.tidyverse.org/packages/#core-tidyverse