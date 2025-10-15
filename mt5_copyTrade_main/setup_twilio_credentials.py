#!/usr/bin/env python3
"""
Setup Twilio Credentials in Backend Configuration
This will help you set up your Twilio credentials
"""

import os
import sys
from pathlib import Path

def setup_twilio_credentials():
    """Setup Twilio credentials in the backend"""
    print("🔧 TWILIO CREDENTIALS SETUP")
    print("=" * 40)
    print()
    
    # Get credentials from user
    print("Please enter your Twilio credentials:")
    print("(You can find these at: https://console.twilio.com/)")
    print()
    
    account_sid = "AC2469e58e3a8bc6504c38b20937dfc67e"
    auth_token = "69088e4a465643bc5e79131264bfca74"
    from_number = "+12294715571"
    
    if not all([account_sid, auth_token, from_number]):
        print("❌ All fields are required!")
        return False
    
    print()
    print("📝 Creating environment configuration...")
    
    # Create .env content
    env_content = f"""# ===================================
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
# ===================================
TWILIO_ACCOUNT_SID={account_sid}
TWILIO_AUTH_TOKEN={auth_token}
TWILIO_FROM_NUMBER={from_number}

# ===================================
# EMAIL SMTP CREDENTIALS
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
    
    # Write to backend/.env
    backend_dir = Path(__file__).parent / "backend"
    env_file = backend_dir / ".env"
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        
        print(f"✅ .env file created: {env_file}")
        print()
        print("🧪 Testing Twilio credentials...")
        
        # Test the credentials
        try:
            from twilio.rest import Client
            client = Client(account_sid, auth_token)
            
            # Try to get account info
            account = client.api.accounts(account_sid).fetch()
            print(f"✅ Twilio credentials are valid!")
            print(f"   Account Name: {account.friendly_name}")
            print(f"   Account Status: {account.status}")
            print()
            
            # Test phone number
            print("📱 Testing phone number...")
            try:
                incoming_phone_numbers = client.incoming_phone_numbers.list()
                if incoming_phone_numbers:
                    print(f"✅ Phone number found: {incoming_phone_numbers[0].phone_number}")
                    if incoming_phone_numbers[0].phone_number == from_number:
                        print("✅ Phone number matches your input!")
                    else:
                        print(f"⚠️  Your input ({from_number}) doesn't match Twilio number ({incoming_phone_numbers[0].phone_number})")
                else:
                    print("❌ No phone numbers found in your Twilio account")
            except Exception as e:
                print(f"⚠️  Could not verify phone number: {str(e)}")
            
        except Exception as e:
            print(f"❌ Twilio credentials test failed: {str(e)}")
            print("   Please check your Account SID and Auth Token")
        
        print()
        print("🎯 Next Steps:")
        print("1. Run 'python test_twilio_direct.py' to test SMS sending")
        print("2. Run 'python test_backend_sms.py' to test backend integration")
        print("3. Start your backend server: cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating .env file: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 TWILIO SETUP WIZARD")
    print("=" * 40)
    print()
    
    success = setup_twilio_credentials()
    
    if success:
        print()
        print("🎉 Setup completed successfully!")
    else:
        print()
        print("❌ Setup failed. Please try again.")

if __name__ == "__main__":
    main()
