import humanize

from odoo import http
from odoo.http import request


class Hello(http.Controller):
    @http.route("/wodby/hello", type="http", auth="public")
    def hello(self):
        params = request.env["ir.config_parameter"].sudo()
        # Odoo 20 replaced get_param with typed getters.
        greeting = (params.get_str if hasattr(params, "get_str") else params.get_param)("wodby_hello.greeting")
        return f"{greeting} {humanize.intcomma(1234567)}"
