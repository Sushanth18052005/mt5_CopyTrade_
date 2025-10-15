#!/usr/bin/env python3
"""
Startup script for FastAPI backend
"""
import sys
import os

# Add the parent directory to Python path so we can import modules properly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Now we can import and run main
from backend.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )