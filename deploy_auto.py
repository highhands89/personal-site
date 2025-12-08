#!/usr/bin/env python3
"""
Automated Deployment Script with .env file support
Loads credentials from .env file automatically
"""

import ftplib
import os
import sys
from pathlib import Path

# Try to load python-dotenv if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # If dotenv not available, manually load .env file
    env_file = Path(__file__).parent / '.env'
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

# Import the main deployment function
from deploy import main

if __name__ == "__main__":
    main()

