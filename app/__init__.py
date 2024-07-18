from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes.upload import upload_bp
    from .routes.analyze import analyze_bp

    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(analyze_bp, url_prefix='/analyze')

    return app
