from pathlib import Path

class DaddyConfig:

    def __init__(self, _name_):
        self.runner_path = Path(_name_).resolve()
        self.root_path = self.runner_path.parent
        self.template_path = self.root_path / "fuckend"

        self.STATUS_PAGES = {
            400: "Bad request",
            401: "Unauthorized",
            403: self.gimme_that_damn_page('../server/response_templates/forbidden.html'),
            404: self.gimme_that_damn_page('../server/response_templates/notfound.html'),
            405: "Method not allowed",
            500: self.gimme_that_damn_page('../server/response_templates/internalservererror.html'),
        }

