from flask import Flask, jsonify
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.common.puertos.api_v1_0.resources import puertos_v1_0_bp
from app.ext import ma, migrate
from flask_login import LoginManager
from app.web.routes import web_bp
from app.common.puertos.models import User
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))
def create_app(settings_module):
    app = Flask(__name__)
    app.register_blueprint(web_bp)
    app.config.from_object(settings_module)
    app.config["SECRET_KEY"] = "Koala"

    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Deshabilita strict slashes
    app.url_map.strict_slashes = False

    # Registrar blueprint
    app.register_blueprint(puertos_v1_0_bp)

    # Registrar manejadores de errores
    register_error_handlers(app)

    # Mostrar rutas disponibles
    print("Rutas registradas:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.methods}")

    login_manager.login_view = 'web.login'
    login_manager.init_app(app)
    return app



def register_error_handlers(app):
    import traceback

    @app.errorhandler(Exception)
    def handle_general_exception(e):
        print(traceback.format_exc())  # imprime el error en terminal
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({'msg': 'Not Found'}), 404

    @app.errorhandler(405)
    def handle_405(e):
        return jsonify({'msg': 'Method Not Allowed'}), 405

    @app.errorhandler(403)
    def handle_403(e):
        return jsonify({'msg': 'Forbidden'}), 403

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found(e):
        return jsonify({'msg': str(e)}), 404