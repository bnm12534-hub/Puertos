import os

from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE', 'app.settings.DevelopmentConfig')
app = create_app(settings_module)