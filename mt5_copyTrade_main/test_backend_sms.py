#!/usr/bin/env python3
"""
Test Backend SMS Integration
This will test the SMS functionality through the backend API
"""

import asyncio
import aiohttp
import json
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

async def test_backend_sms():
    """Test SMS through backend API"""
    print("🔧 BACKEND SMS INTEGRATION TEST")
    print("=" * 50)
    print()
    
    # Get test phone number
    phone_number = input("Enter your verified phone number (e.g., +1234567890): ").strip()
    
    if not phone_number:
        print("❌ Phone number is required!")
        return
    
    print(f"📱 Testing SMS to: {phone_number}")
    print()
    
    # Test data
    test_data = {
        "mobile_or_email": phone_number,
        "otp_type": "mobile"
    }
    
    # Backend URL (adjust if different)
    base_url = "http://localhost:8000"
    send_otp_url = f"{base_url}/api/v1/auth/send-otp"
    
    print("🧪 Sending OTP request to backend...")
    print(f"   URL: {send_otp_url}")
    print(f"   Data: {json.dumps(test_data, indent=2)}")
    print()
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                send_otp_url,
                json=test_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                
                response_text = await response.text()
                print(f"📡 Response Status: {response.status}")
                print(f"📡 Response Headers: {dict(response.headers)}")
                print(f"📡 Response Body: {response_text}")
                print()
                
                if response.status == 200:
                    result = await response.json()
                    if result.get("success"):
                        print("✅ Backend SMS request successful!")
                        print(f"   Message: {result.get('message', 'No message')}")
                        if result.get("data"):
                            print(f"   Data: {result['data']}")
                    else:
                        print("❌ Backend SMS request failed!")
                        print(f"   Error: {result.get('message', 'Unknown error')}")
                else:
                    print(f"❌ HTTP Error: {response.status}")
                    print(f"   Response: {response_text}")
                    
    except aiohttp.ClientConnectorError:
        print("❌ Cannot connect to backend!")
        print("   Make sure the backend server is running:")
        print("   cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000")
        
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

async def test_backend_health():
    """Test if backend is running"""
    print("🏥 TESTING BACKEND HEALTH")
    print("=" * 30)
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8000/api/docs") as response:
                if response.status == 200:
                    print("✅ Backend is running!")
                    return True
                else:
                    print(f"❌ Backend returned status: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ Backend is not running: {str(e)}")
        return False

async def main():
    """Main function"""
    print("🚀 BACKEND SMS TESTING TOOL")
    print("=" * 50)
    print()
    
    # Check if backend is running
    backend_ok = await test_backend_health()
    print()
    
    if not backend_ok:
        print("❌ Backend is not running!")
        print("   Please start the backend first:")
        print("   cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000")
        return
    
    # Test SMS
    await test_backend_sms()

if __name__ == "__main__":
    asyncio.run(main())


