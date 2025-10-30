# GitHub Actions and GitHub Pages

`repo2docker` is available as a [GitHub Action](https://docs.github.com/en/actions) from [GitHub Marketplace](https://github.com/marketplace) under the same name, i.e. [`repo2docker`](https://github.com/marketplace/actions/repo2wasm), to publish the integrated development environment (IDE) to [GitHub Pages](https://docs.github.com/en/pages).

## Usage

Create the file `.github/workflows/repo2wasm.yml` with

```yaml
name: Convert repository to Wasm-powered integrated development environment
on:
  push:
    branches:
      - main
jobs:
  create-ide:
    runs-on: ubuntu-24.04
    permissions:
      pages: write
      id-token: write
    steps:
      - name: Create IDE and publish to GitHub Pages
        uses: repo2wasm/gh-actions@0.2.0
```
