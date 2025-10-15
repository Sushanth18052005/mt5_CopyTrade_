#!/usr/bin/env python3
"""
Fix Frontend to use Local Backend
This script will update the frontend to use the local backend instead of production
"""

import re
from pathlib import Path

def fix_frontend_backend_urls():
    """Update frontend to use local backend URLs"""
    
    frontend_file = Path("frontend/src/app/components/RegistrationFlow.tsx")
    
    if not frontend_file.exists():
        print("❌ Frontend file not found!")
        return False
    
    # Read the file
    with open(frontend_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace production URLs with local URLs
    old_url = "https://mt5-copytrade.onrender.com"
    new_url = "http://localhost:8000"
    
    # Count occurrences
    old_count = content.count(old_url)
    
    if old_count == 0:
        print("✅ No production URLs found in frontend")
        return True
    
    # Replace all occurrences
    new_content = content.replace(old_url, new_url)
    
    # Write back to file
    with open(frontend_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated {old_count} URLs from {old_url} to {new_url}")
    return True

def add_otp_display_to_frontend():
    """Add OTP display to frontend for testing"""
    
    frontend_file = Path("frontend/src/app/components/RegistrationFlow.tsx")
    
    if not frontend_file.exists():
        print("❌ Frontend file not found!")
        return False
    
    # Read the file
    with open(frontend_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add OTP display after OTP sent message
    otp_display_code = '''
        {otpSent && (
          <div className="alert alert-info">
            OTP sent to {formData.mobile} and {formData.email}
            {mobileResult?.data?.otp && (
              <div style={{marginTop: '10px', padding: '10px', background: '#e0f2fe', borderRadius: '5px'}}>
                <strong>Mobile OTP (for testing):</strong> {mobileResult.data.otp}
              </div>
            )}
            {emailResult?.data?.otp && (
              <div style={{marginTop: '10px', padding: '10px', background: '#e8f5e8', borderRadius: '5px'}}>
                <strong>Email OTP (for testing):</strong> {emailResult.data.otp}
              </div>
            )}
          </div>
        )}'''
    
    # Find the existing OTP sent message and replace it
    old_otp_message = '''        {otpSent && (
          <div className="alert alert-info">
            OTP sent to {formData.mobile} and {formData.email}
          </div>
        )}'''
    
    if old_otp_message in content:
        new_content = content.replace(old_otp_message, otp_display_code)
        
        # Write back to file
        with open(frontend_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Added OTP display to frontend")
        return True
    else:
        print("⚠️  Could not find OTP sent message to replace")
        return False

def main():
    """Main function"""
    print("🔧 FIXING FRONTEND-BACKEND CONNECTION")
    print("=" * 50)
    print()
    
    # Fix URLs
    print("1. Updating frontend URLs...")
    if fix_frontend_backend_urls():
        print("   ✅ URLs updated successfully")
    else:
        print("   ❌ Failed to update URLs")
    
    print()
    
    # Add OTP display
    print("2. Adding OTP display for testing...")
    if add_otp_display_to_frontend():
        print("   ✅ OTP display added")
    else:
        print("   ❌ Failed to add OTP display")
    
    print()
    print("🎯 NEXT STEPS:")
    print("1. Start your backend: cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000")
    print("2. Start your frontend: cd frontend && npm run dev")
    print("3. Test registration with a real phone number")
    print("4. The OTP will be displayed on screen for testing")

if __name__ == "__main__":
    main()


