class Repo2WasmError(Exception):
    documentation_url = "https://repo2wasm.readthedocs.io/en/latest/common-errors/"
    error_page = ""
    long_message = ""

    def __init__(self, msg="", *args, **kwargs):
        final_message = (
            f"{self.long_message}\nSee {self.documentation_url}{self.error_page}"
        )

        super().__init__(final_message, *args, **kwargs)


class TidyVerseError(Repo2WasmError):
    error_page = "tidyverse"
    long_message = "tidyverse library is NOT supported."
