#!/usr/bin/env python3
"""
Debug OTP issue
"""
import asyncio
import httpx
from datetime import datetime

BASE_URL = "http://localhost:8000"

async def debug_otp():
    client = httpx.AsyncClient(timeout=30.0)
    
    # Generate unique test data
    timestamp = int(datetime.now().timestamp())
    mobile = f"+1234567{timestamp % 10000:04d}"
    email = f"test{timestamp}@example.com"
    
    print(f"Testing with mobile: {mobile}")
    print(f"Testing with email: {email}")
    
    try:
        # Send mobile OTP
        print("\n1. Sending mobile OTP...")
        response = await client.post(
            f"{BASE_URL}/api/v1/auth/send-otp",
            json={
                "mobile_or_email": mobile,
                "otp_type": "mobile"
            }
        )
        
        result = response.json()
        print(f"Response: {result}")
        
        if result.get("success") and result.get("data", {}).get("otp"):
            otp = result["data"]["otp"]
            print(f"OTP received: {otp}")
            
            # Try to verify
            print("\n2. Verifying mobile OTP...")
            verify_response = await client.post(
                f"{BASE_URL}/api/v1/auth/verify-otp",
                json={
                    "mobile_or_email": mobile,
                    "otp": otp,
                    "otp_type": "mobile"
                }
            )
            
            verify_result = verify_response.json()
            print(f"Verify response: {verify_result}")
        else:
            print("Failed to get OTP")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.aclose()

if __name__ == "__main__":
    asyncio.run(debug_otp())

