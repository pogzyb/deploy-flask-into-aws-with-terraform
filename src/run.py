# src/run.py
# application entrypoint used by gunicorn
from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=os.getenv('APP_PORT'))
