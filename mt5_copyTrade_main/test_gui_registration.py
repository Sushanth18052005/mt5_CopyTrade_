#!/usr/bin/env python3
"""
Test GUI Registration Flow
This will test the complete registration flow that the frontend uses
"""

import asyncio
import aiohttp
import json
import sys
from pathlib import Path

async def test_gui_registration_flow():
    """Test the complete GUI registration flow"""
    print("🎯 GUI REGISTRATION FLOW TEST")
    print("=" * 50)
    print()
    
    # Test data (use different phone number than your Twilio number)
    test_data = {
        "name": "Test User",
        "email": "nikithakambhampati123@gmail.com",
        "mobile": "+1234567890",  # Use a different number than your Twilio number
        "password": "testpassword123",
        "country": "United States",
        "state": "California",
        "city": "San Francisco",
        "pin_code": "94102",
        "referral_code": None
    }
    
    base_url = "http://localhost:8000"
    
    print("📋 Test Data:")
    print(f"   Name: {test_data['name']}")
    print(f"   Email: {test_data['email']}")
    print(f"   Mobile: {test_data['mobile']}")
    print()
    
    try:
        async with aiohttp.ClientSession() as session:
            
            # Step 1: Test Mobile OTP
            print("📱 Step 1: Testing Mobile OTP...")
            mobile_otp_url = f"{base_url}/api/v1/auth/send-otp"
            mobile_otp_data = {
                "mobile_or_email": test_data["mobile"],
                "otp_type": "mobile"
            }
            
            async with session.post(mobile_otp_url, json=mobile_otp_data) as response:
                mobile_result = await response.json()
                print(f"   Status: {response.status}")
                print(f"   Success: {mobile_result.get('success', False)}")
                print(f"   Message: {mobile_result.get('message', 'No message')}")
                
                if mobile_result.get('data', {}).get('otp'):
                    print(f"   OTP: {mobile_result['data']['otp']}")
                    mobile_otp = mobile_result['data']['otp']
                else:
                    print("   ❌ No OTP received")
                    mobile_otp = None
            
            print()
            
            # Step 2: Test Email OTP
            print("📧 Step 2: Testing Email OTP...")
            email_otp_data = {
                "mobile_or_email": test_data["email"],
                "otp_type": "email"
            }
            
            async with session.post(email_otp_url, json=email_otp_data) as response:
                email_result = await response.json()
                print(f"   Status: {response.status}")
                print(f"   Success: {email_result.get('success', False)}")
                print(f"   Message: {email_result.get('message', 'No message')}")
                
                if email_result.get('data', {}).get('otp'):
                    print(f"   OTP: {email_result['data']['otp']}")
                    email_otp = email_result['data']['otp']
                else:
                    print("   ❌ No OTP received")
                    email_otp = None
            
            print()
            
            # Step 3: Test Registration
            print("👤 Step 3: Testing User Registration...")
            register_url = f"{base_url}/api/v1/auth/register"
            
            async with session.post(register_url, json=test_data) as response:
                register_result = await response.json()
                print(f"   Status: {response.status}")
                print(f"   Success: {register_result.get('success', False)}")
                print(f"   Message: {register_result.get('message', 'No message')}")
                
                if register_result.get('data'):
                    print(f"   User ID: {register_result['data'].get('user_id', 'N/A')}")
                    print(f"   Access Token: {'Yes' if register_result['data'].get('access_token') else 'No'}")
            
            print()
            
            # Summary
            print("📊 SUMMARY:")
            print(f"   Mobile OTP: {'✅ Working' if mobile_otp else '❌ Failed'}")
            print(f"   Email OTP: {'✅ Working' if email_otp else '❌ Failed'}")
            print(f"   Registration: {'✅ Working' if register_result.get('success') else '❌ Failed'}")
            
            if mobile_otp and email_otp:
                print()
                print("🎉 All systems working! The issue might be:")
                print("   1. Frontend not calling the correct API endpoints")
                print("   2. CORS issues between frontend and backend")
                print("   3. Frontend not handling errors properly")
                print("   4. Different phone number used in frontend")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

async def test_frontend_api_calls():
    """Test the exact API calls the frontend makes"""
    print("🔍 FRONTEND API CALLS TEST")
    print("=" * 40)
    print()
    
    # These are the exact calls the frontend makes
    base_url = "http://localhost:8000"
    
    # Test data
    mobile = "+1234567890"  # Use different number than Twilio
    email = "nikithakambhampati123@gmail.com"
    
    try:
        async with aiohttp.ClientSession() as session:
            
            # Call 1: Send Mobile OTP (exactly as frontend does)
            print("📱 Frontend Call 1: Send Mobile OTP")
            mobile_url = f"{base_url}/api/v1/auth/send-otp"
            mobile_payload = {
                "mobile_or_email": mobile,
                "otp_type": "mobile"
            }
            
            async with session.post(mobile_url, json=mobile_payload) as response:
                result = await response.json()
                print(f"   URL: {mobile_url}")
                print(f"   Payload: {json.dumps(mobile_payload, indent=2)}")
                print(f"   Response: {json.dumps(result, indent=2)}")
                print()
            
            # Call 2: Send Email OTP (exactly as frontend does)
            print("📧 Frontend Call 2: Send Email OTP")
            email_otp_url = f"{base_url}/api/v1/auth/send-otp"
            email_payload = {
                "mobile_or_email": email,
                "otp_type": "email"
            }
            
            async with session.post(email_otp_url, json=email_payload) as response:
                result = await response.json()
                print(f"   URL: {email_otp_url}")
                print(f"   Payload: {json.dumps(email_payload, indent=2)}")
                print(f"   Response: {json.dumps(result, indent=2)}")
                print()
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")

async def main():
    """Main function"""
    print("🚀 GUI REGISTRATION DEBUGGING")
    print("=" * 50)
    print()
    
    print("🔧 IMPORTANT: Use a DIFFERENT phone number than your Twilio number!")
    print("   Your Twilio number: +12294715571")
    print("   Use a different number for testing (e.g., +1234567890)")
    print()
    
    # Test frontend API calls
    await test_frontend_api_calls()
    print()
    
    # Test complete flow
    await test_gui_registration_flow()

if __name__ == "__main__":
    asyncio.run(main())
