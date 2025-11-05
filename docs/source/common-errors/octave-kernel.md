# `octave_kernel`

![status: implemented](https://img.shields.io/badge/status-implemented-green)
![version: 0.6.0](https://img.shields.io/badge/version-0.6.0-blue)

[`octave_kernel`] is a Jupyter kernel for [GNU Octave](https://octave.org/) that is **not** supported by `repo2wasm`.
The alternative [`xeus-octave`] Jupyter kernel is supported.

## Problematic Code

```yaml
name: octave
dependencies:
  - octave_kernel
```

## Correct Code

```yaml
name: octave
dependencies:
  - xeus-octave
```

[`octave_kernel`]: https://github.com/Calysto/octave_kernel
[`xeus-octave`]: https://github.com/jupyter-xeus/xeus-octave
