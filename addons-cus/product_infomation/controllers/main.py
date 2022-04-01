import odoo
import logging
import json
_logger = logging.getLogger(__name__)


class getProductInformation(odoo.http.Controller):

    @odoo.http.route("/show", auth="public")
    def foo_handler(self):
        return json.dumps({
            "content": "Welcome to 'bar' API!"
        })

    @odoo.http.route(["/product/<dbname>/<id>"], type="http", auth="none", sitemap=False, cors="*", csrf=False)
    def handle_product(self, dbname, id):
        model_name = "pro.product.information"
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([("id", "=", int(id))], limit=1)
                response= {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                        "description": rec.description,
                        "amount": rec.amount,
                        "price": rec.price,
                        "made_in": rec.made_in,
                        "tax": rec.tax,
                        "import_price": rec.import_price,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)
