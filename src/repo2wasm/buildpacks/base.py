from jupyterlite_core.manager import LiteManager


class BaseBuildPack(LiteManager):
    def __init__(
        self,
        repository,
        configuration_file,
        ide,
        output_dir,
        forgiving=False,
        ignore=[],
    ):
        super().__init__()
        self.initialize()

        # repo2wasm
        self.repository = repository
        self.configuration_file = configuration_file
        self.ide = ide
        self.forgiving = forgiving

        # JupyterLite
        if self.ide == "jupyterlab":
            self.apps = ("lab",)
        elif self.ide == "notebook":
            self.apps = ("tree",)
        else:
            self.apps = ("lab",)

        self.contents = (self.repository,)
        self.output_dir = output_dir

        # Append .pixi to be ignore
        self.ignore_contents = (*self.ignore_contents, "/\\.pixi")
