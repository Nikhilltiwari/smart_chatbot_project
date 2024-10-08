from flask import Flask, render_template
import os

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
    print(f"Template directory: {template_dir}")
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object('config.Config')

    from .routes.upload import upload_bp
    from .routes.analyze import analyze_bp
    from .routes.chat import chat_bp
    from .routes.query import query_bp
    from .routes.visualize import visualize_bp

    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(analyze_bp, url_prefix='/analyze')
    app.register_blueprint(chat_bp, url_prefix='/chat')
    app.register_blueprint(query_bp, url_prefix='/query')
    app.register_blueprint(visualize_bp, url_prefix='/visualize')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app




