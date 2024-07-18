from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes.upload import upload_bp
    from .routes.analyze import analyze_bp
    from .routes.query import query_bp
    from .routes.visualize import visualize_bp
    from .routes.chat import chat_bp

    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(analyze_bp, url_prefix='/analyze')
    app.register_blueprint(query_bp, url_prefix='/query')
    app.register_blueprint(visualize_bp, url_prefix='/visualize')
    app.register_blueprint(chat_bp, url_prefix='/chat')

    return app

