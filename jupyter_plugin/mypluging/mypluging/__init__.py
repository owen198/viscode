from mypluging.handlers import setup_handlers 

def _jupyter_server_extension_paths():
    return [{
        "module": "mypluging"
    }]

def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="mypluging",
        # _also_ in the `nbextension/` namespace
        require="mypluging/cell_result_detect")]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp)
