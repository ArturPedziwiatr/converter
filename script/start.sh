source ~/venv/bin/activate
cd /opt/app
uvicorn appmain:app --host 0.0.0.0 --port 80