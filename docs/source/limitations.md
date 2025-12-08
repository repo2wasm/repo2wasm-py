# Limitations

Web browsers execute the [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly) (Wasm) bytecode in a sandboxed environment separated from the host. The sandboxed environment has some limitations, including

- maximum of 4 GB because of the use of 32-bit indexes.
- multithreading is still being standardized and implemented by browsers.
- [single instruction, multiple data (SIMD)](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) is still being standardized and implemented by browsers.
- can **only** escape the sandbox going through appropriate APIs.

## Network

The biggest limitation for the end user is probably related with access to the internet that can happen using [Fetch API] or proxy.

## Fetch API

The Wasm code uses the [Fetch API] directly and follows the same security of JavaScript running in the browser, for example [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).

# Proxy

The Wasm code uses the [Fetch API] to contact a proxy server that is responsible to fulfill the access to the internet.

## References

- [WebAssembly - Documentation - Security](https://webassembly.org/docs/security/)
- [The State of WebAssembly – 2024 and 2025](https://platform.uno/blog/state-of-webassembly-2024-2025/) by
C. Gerard Gallant.
- [Emscripten Documentation](https://emscripten.org/docs/index.html)
- [Easier WebAssembly with twr-wasm: Wasm Runtime Limitations](https://twiddlingbits.dev/docsite/more/wasm-problem/)
- [Making libcurl work in webassembly](https://jeroen.github.io/notes/webassembly-curl/) by Jeroen.
- [libcurl.js](https://libcurl.js.org/)
- [webR - Networking](https://docs.r-wasm.org/webr/latest/networking.html)
- [Making HTTP Requests with Pyodide](https://nickgeorge.net/pyodide-http-requests/) by Nick George.

[Fetch API]: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
