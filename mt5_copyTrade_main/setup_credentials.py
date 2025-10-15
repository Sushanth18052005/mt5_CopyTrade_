#!/usr/bin/env python3
"""
Setup script to create .env file with credentials template
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file in backend directory"""
    
    # Get the backend directory path
    backend_dir = Path(__file__).parent / "backend"
    env_file = backend_dir / ".env"
    
    # Check if .env already exists
    if env_file.exists():
        print("⚠️  .env file already exists!")
        response = input("Do you want to overwrite it? (y/N): ").lower()
        if response != 'y':
            print("❌ Setup cancelled")
            return
    
    # Create the .env content
    env_content = """# ===================================
# BACKEND/.env FILE
# ===================================

# App Settings
APP_NAME=MT5 Copy Trading Backend
DEBUG=True
API_V1_STR=/api/v1

# Security (CHANGE IN PRODUCTION!)
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Database
MONGODB_URL=mongodb+srv://kapardhikannekanti_db_user:3XoNc2gtr9lGY4oi@mt5-cluster.njyntuk.mongodb.net/?retryWrites=true&w=majority&appName=mt5-cluster
DATABASE_NAME=mt5_copy_trading

# CORS
ALLOWED_HOSTS=*

# OTP Settings
OTP_EXPIRE_MINUTES=5
OTP_LENGTH=6

# ===================================
# TWILIO SMS CREDENTIALS
# Get these from: https://console.twilio.com/
# ===================================
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_FROM_NUMBER=+1234567890

# ===================================
# EMAIL SMTP CREDENTIALS
# For Gmail: Use App Password (not regular password)
# ===================================
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_FROM=your_email@gmail.com

# ===================================
# TRADE COPIER INTEGRATION
# ===================================
TRADE_COPIER_BASE_URL=http://localhost:8001
TRADE_COPIER_API_KEY=your_trade_copier_api_key
"""
    
    try:
        # Write the .env file
        with open(env_file, 'w') as f:
            f.write(env_content)
        
        print("✅ .env file created successfully!")
        print(f"   Location: {env_file}")
        print()
        print("📋 Next Steps:")
        print("1. Edit the .env file and add your real credentials")
        print("2. For Twilio: Get credentials from https://console.twilio.com/")
        print("3. For Gmail: Use App Password (not regular password)")
        print("4. Run 'python test_credentials.py' to test your setup")
        print("5. See CREDENTIALS_SETUP_GUIDE.md for detailed instructions")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {str(e)}")

if __name__ == "__main__":
    print("🔧 CREDENTIALS SETUP SCRIPT")
    print("=" * 40)
    print()
    create_env_file()


