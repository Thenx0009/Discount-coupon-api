from flask import Flask
from flaskr.routes import bp as coupon_bp
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev')
    )
    
    # Register the coupon blueprint
    app.register_blueprint(coupon_bp, url_prefix='/api')
    
    return app