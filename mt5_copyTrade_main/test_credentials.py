#!/usr/bin/env python3
"""
Test script to verify Twilio and SMTP credentials
Run this after setting up your .env file
"""

import asyncio
import os
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

from backend.services.real_sms_service import real_sms_service
from backend.services.email_service import email_service

async def test_twilio_sms():
    """Test Twilio SMS functionality"""
    print("📱 Testing Twilio SMS...")
    print("-" * 40)
    
    try:
        # Test with a demo number (won't actually send in demo mode)
        result = await real_sms_service.send_otp_sms("+1234567890", "123456", "test")
        
        if result["status"]:
            print("✅ Twilio SMS: SUCCESS")
            print(f"   Message: {result['message']}")
            if result.get("data", {}).get("otp"):
                print(f"   Demo OTP: {result['data']['otp']}")
        else:
            print("❌ Twilio SMS: FAILED")
            print(f"   Error: {result['message']}")
            
    except Exception as e:
        print("❌ Twilio SMS: ERROR")
        print(f"   Exception: {str(e)}")
    
    print()

async def test_smtp_email():
    """Test SMTP Email functionality"""
    print("📧 Testing SMTP Email...")
    print("-" * 40)
    
    try:
        # Test with a demo email
        result = await email_service.send_otp_email("test@example.com", "123456", "test")
        
        if result["status"]:
            print("✅ SMTP Email: SUCCESS")
            print(f"   Message: {result['message']}")
        else:
            print("❌ SMTP Email: FAILED")
            print(f"   Error: {result['message']}")
            
    except Exception as e:
        print("❌ SMTP Email: ERROR")
        print(f"   Exception: {str(e)}")
    
    print()

def check_env_file():
    """Check if .env file exists and show current settings"""
    print("🔍 Checking Environment Configuration...")
    print("-" * 40)
    
    env_path = Path(__file__).parent / "backend" / ".env"
    
    if not env_path.exists():
        print("❌ .env file not found!")
        print("   Please create backend/.env file with your credentials")
        print("   See CREDENTIALS_SETUP_GUIDE.md for instructions")
        return False
    
    print("✅ .env file found")
    
    # Load and check key settings
    try:
        from backend.core.config import settings
        
        print(f"   Twilio Account SID: {'✅ Set' if settings.TWILIO_ACCOUNT_SID else '❌ Missing'}")
        print(f"   Twilio Auth Token: {'✅ Set' if settings.TWILIO_AUTH_TOKEN else '❌ Missing'}")
        print(f"   Twilio From Number: {'✅ Set' if settings.TWILIO_FROM_NUMBER else '❌ Missing'}")
        print(f"   Email Username: {'✅ Set' if settings.EMAIL_USERNAME else '❌ Missing'}")
        print(f"   Email Password: {'✅ Set' if settings.EMAIL_PASSWORD else '❌ Missing'}")
        print(f"   SMTP Server: {settings.SMTP_SERVER}")
        print(f"   SMTP Port: {settings.SMTP_PORT}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading settings: {str(e)}")
        return False

async def main():
    """Main test function"""
    print("🧪 CREDENTIALS TEST SCRIPT")
    print("=" * 50)
    print()
    
    # Check environment
    env_ok = check_env_file()
    print()
    
    if not env_ok:
        print("❌ Please fix environment configuration first")
        return
    
    # Test services
    await test_twilio_sms()
    await test_smtp_email()
    
    print("🎯 Test Complete!")
    print("=" * 50)
    print()
    print("📋 Next Steps:")
    print("1. If SMS/Email tests failed, check your credentials in backend/.env")
    print("2. Run 'python test_complete_registration.py' to test full flow")
    print("3. Check CREDENTIALS_SETUP_GUIDE.md for detailed setup instructions")

if __name__ == "__main__":
    asyncio.run(main())


