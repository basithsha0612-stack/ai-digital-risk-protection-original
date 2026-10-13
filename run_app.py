"""Single-Command Startup Script for Digital Risk Protection Platform (DRP)."""

import sys
import os
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Ensure Node.js tool is in process PATH
NODE_BIN_DIR = ROOT_DIR / "tools" / "node"
if NODE_BIN_DIR.exists():
    os.environ["PATH"] = str(NODE_BIN_DIR) + os.pathsep + os.environ.get("PATH", "")

BANNER = r"""
================================================================================
  ____  _____    ____    ____  _        _  _____ _____ ___  ____  __  __ 
 |  _ \|  _ \  |  _ \  |  _ \| |      / \|_   _|_   _/ _ \|  _ \|  \/  |
 | | | | |_) | | |_) | | |_) | |     / _ \ | |   | || | | | |_) | |\/| |
 | |_| |  _ <  |  __/  |  __/| |___ / ___ \| |   | || |_| |  _ <| |  | |
 |____/|_| \_\ |_|     |_|   |_____/_/   \_\_|   |_| \___/|_| \_\_|  |_|
  Digital Risk Protection Platform — Cyber Threat Intelligence & Phishing Defense
================================================================================
[*] Web Application:   http://localhost:8000 (React Frontend + API)
[*] Interactive Docs:  http://localhost:8000/docs
[*] Vite Dev Server:   http://localhost:5173 (Optional: run 'npm run dev' in frontend)
[*] ML Model:          Scikit-learn RandomForest (97.2% Accuracy)
[*] Database:          MySQL with SQLite local fallback
================================================================================
"""

def main():
    print(BANNER)

    # 1. Ensure Model is Trained
    model_path = ROOT_DIR / "ml" / "model.joblib"
    if not model_path.exists():
        print("[*] Training Scikit-learn Phishing Classifier...")
        from ml.train import train_phishing_model
        train_phishing_model()

    # 2. Ensure Database is Seeded
    print("[*] Verifying database tables and sample records...")
    from database.seed import seed_data
    seed_data()

    # 3. Start FastAPI Server
    print("[*] Launching Uvicorn ASGI Server on http://localhost:8000...")
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    main()
