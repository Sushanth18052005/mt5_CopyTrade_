#!/usr/bin/env python3
"""
Direct Twilio SMS Test Script
This will test your Twilio credentials directly without the backend
"""

import asyncio
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioException

async def test_twilio_direct():
    """Test Twilio SMS directly"""
    print("📱 DIRECT TWILIO SMS TEST")
    print("=" * 50)
    print()
    
    # Get credentials from user
    print("Please enter your Twilio credentials:")
    account_sid = input("Account SID: ").strip()
    auth_token = input("Auth Token: ").strip()
    from_number = input("From Number (e.g., +1234567890): ").strip()
    to_number = input("To Number (your verified number): ").strip()
    
    if not all([account_sid, auth_token, from_number, to_number]):
        print("❌ All fields are required!")
        return
    
    print()
    print("🧪 Testing Twilio SMS...")
    print("-" * 30)
    
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Send test SMS
        message = client.messages.create(
            body="🧪 MT5 Copy Trading Test SMS - If you receive this, Twilio is working!",
            from_=from_number,
            to=to_number
        )
        
        print("✅ SMS SENT SUCCESSFULLY!")
        print(f"   Message SID: {message.sid}")
        print(f"   Status: {message.status}")
        print(f"   From: {message.from_}")
        print(f"   To: {message.to}")
        print(f"   Body: {message.body}")
        print()
        print("📱 Check your phone for the message!")
        
    except TwilioException as e:
        print("❌ TWILIO ERROR:")
        print(f"   Error Code: {e.code}")
        print(f"   Error Message: {e.msg}")
        print()
        print("🔍 Common Issues:")
        print("   - Wrong Account SID or Auth Token")
        print("   - From number not verified in Twilio Console")
        print("   - To number not verified (for trial accounts)")
        print("   - Insufficient account balance")
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {str(e)}")

async def test_twilio_with_credentials(account_sid, auth_token, from_number, to_number):
    """Test Twilio with provided credentials"""
    print("📱 TESTING TWILIO WITH PROVIDED CREDENTIALS")
    print("=" * 50)
    print()
    
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Send test SMS
        message = client.messages.create(
            body="🧪 MT5 Copy Trading Test SMS - If you receive this, Twilio is working!",
            from_=from_number,
            to=to_number
        )
        
        print("✅ SMS SENT SUCCESSFULLY!")
        print(f"   Message SID: {message.sid}")
        print(f"   Status: {message.status}")
        print(f"   From: {message.from_}")
        print(f"   To: {message.to}")
        print(f"   Body: {message.body}")
        print()
        print("📱 Check your phone for the message!")
        return True
        
    except TwilioException as e:
        print("❌ TWILIO ERROR:")
        print(f"   Error Code: {e.code}")
        print(f"   Error Message: {e.msg}")
        print()
        print("🔍 Common Issues:")
        print("   - Wrong Account SID or Auth Token")
        print("   - From number not verified in Twilio Console")
        print("   - To number not verified (for trial accounts)")
        print("   - Insufficient account balance")
        return False
        
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {str(e)}")
        return False

def check_twilio_console():
    """Provide instructions for checking Twilio Console"""
    print("🔍 CHECKING TWILIO CONSOLE")
    print("=" * 50)
    print()
    print("1. Go to: https://console.twilio.com/")
    print("2. Check your Account SID and Auth Token")
    print("3. Go to Phone Numbers → Manage → Active numbers")
    print("   - Verify your 'From' number is active")
    print("4. For trial accounts, go to Phone Numbers → Manage → Verified Caller IDs")
    print("   - Add your 'To' number if not already verified")
    print("5. Check Account → Usage → Account Balance")
    print("   - Ensure you have sufficient balance")
    print()

async def main():
    """Main function"""
    print("🚀 TWILIO SMS TESTING TOOL")
    print("=" * 50)
    print()
    
    # Check if user wants to use existing credentials
    use_existing = input("Do you want to enter credentials manually? (y/N): ").lower()
    
    if use_existing == 'y':
        await test_twilio_direct()
    else:
        # Try with some common test credentials (user should replace these)
        print("Please update the credentials in this script and run again")
        print("Or run with manual input: python test_twilio_direct.py")
        
        # Example credentials (replace with real ones)
        account_sid = "your_account_sid_here"
        auth_token = "your_auth_token_here"
        from_number = "+1234567890"  # Your Twilio number
        to_number = "+1234567890"    # Your verified number
        
        if account_sid == "your_account_sid_here":
            print("❌ Please update the credentials in the script first!")
            check_twilio_console()
        else:
            await test_twilio_with_credentials(account_sid, auth_token, from_number, to_number)

if __name__ == "__main__":
    asyncio.run(main())


