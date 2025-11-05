# `irkernel`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.6.0](https://img.shields.io/badge/version-0.6.0-blue)

[`irkernel`] is a Jupyter kernel for [R] that is **not** supported by `repo2wasm`.
The alternative [`xeus-r`] Jupyter kernel is supported.

## Problematic Code

```yaml
name: r
dependencies:
  - r-irkernel
```

## Correct Code

```{important}
`repo2wasm` automatically adds [`xeus-r`] if it detects any [R] dependence.
```

```yaml
name: r
dependencies:
  - xeus-r
```

[`irkernel`]: https://github.com/IRkernel/IRkernel
[`xeus-r`]: https://github.com/jupyter-xeus/xeus-r
[R]: (https://www.r-project.org/)
