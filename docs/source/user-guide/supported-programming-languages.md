(supported-programming-languages)=

# Supported programming languages

`repo2wasm` only suports programming languages already compiled to Wasm, packaged by the [`emscripten-forge` organisation on GitHub](https://github.com/emscripten-forge), and available on the [`emscripten-forge-dev` channel hosted by Prefix.dev GmbH](https://prefix.dev/channels/emscripten-forge-dev).

```{important}
The list included in this section is a **non**-exhaustive list.
```

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

```{warning}
Access to the internet is **not** possible. The R package [`curl`](https://cran.r-project.org/web/packages/curl/index.html) was not ported to Wasm.
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

## Octave

```{note}
Check the [`octave` package](https://prefix.dev/channels/emscripten-forge-dev/packages/octave) for updated information.
```

```{warning}
Access to the internet is **not** possible, in other words, the functions `web()`, `urlread()`, `urlwrite()`, `webread()`, and `webwrite() described in the section [WWW Access](https://docs.octave.org/latest/WWW-Access.html) do **not** work.
```

| Version | Available | Latest release if available | Latest release date |
| --- | --- | --- | --- |
| 10.3 | ✔️ | 10.3.0 | 2025-09 |
| 10.2 | ✔️ | 10.2.0 | 2025-05 |
| 10.1 | ❌ | | |
| 9.4 | ❌ | | |
| 9.3 | ❌ | | |
| 9.2 | ❌ | | |
| 9.1 | ❌ | | |
| 8.4 | ❌ | | |
| 8.3 | ❌ | | |
| 8.2 | ❌ | | |
| 8.1 | ❌ | | |
