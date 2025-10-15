# Limitations

Web browsers execute the [WebAssembly](https://en.wikipedia.org/wiki/WebAssembly) (Wasm) bytecode in a sandboxed environment separated from the host. The sandboxed environment has some limitations, including

- maximum of 4 GB because of the use of 32-bit indexes.
- multithreading is still being standardized and implemented by browsers. 
- [single instruction, multiple data (SIMD)](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) is still being standardized and implemented by browsers.
- can **only** escape the sandbox going through appropriate APIs.

## References

- [WebAssembly - Documentation - Security](https://webassembly.org/docs/security/)
- [The State of WebAssembly – 2024 and 2025](https://platform.uno/blog/state-of-webassembly-2024-2025/) by 
C. Gerard Gallant.
- [Emscripten Documentation](https://emscripten.org/docs/index.html)
- [Easier WebAssembly with twr-wasm: Wasm Runtime Limitations](https://twiddlingbits.dev/docsite/more/wasm-problem/)