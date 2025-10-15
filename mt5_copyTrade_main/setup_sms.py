#!/usr/bin/env python3
"""
SMS Setup Script for MT5 Copy Trading Platform
This script helps configure real SMS providers
"""
import os
import sys

def print_banner():
    print("=" * 70)
    print("🚀 MT5 Copy Trading Platform - SMS Setup")
    print("=" * 70)

def display_providers():
    print("\n📱 Available SMS Providers:")
    print("\n1. Fast2SMS (India) - Recommended for Indian numbers")
    print("   - Website: https://www.fast2sms.com/")
    print("   - Cost: Very affordable for Indian SMS")
    print("   - Setup: Create account, get API key")
    print("   - Features: Bulk SMS, OTP services")

    print("\n2. Twilio (Global) - International coverage")
    print("   - Website: https://www.twilio.com/")
    print("   - Cost: Pay per SMS, credit card required")
    print("   - Setup: Create account, get SID, Auth Token, Phone Number")
    print("   - Features: Global coverage, reliable delivery")

    print("\n3. TextLocal (UK/India)")
    print("   - Website: https://www.textlocal.in/")
    print("   - Cost: Competitive pricing")
    print("   - Setup: Create account, get API key")
    print("   - Features: UK and India focused")

    print("\n4. MSG91 (Global)")
    print("   - Website: https://msg91.com/")
    print("   - Cost: Global pricing")
    print("   - Setup: Create account, get API key and Template ID")
    print("   - Features: Template-based SMS, global coverage")

def setup_fast2sms():
    print("\n🚀 Setting up Fast2SMS (Recommended for India)")
    print("\nStep-by-step setup:")
    print("1. Go to https://www.fast2sms.com/")
    print("2. Sign up for a free account")
    print("3. Verify your mobile number")
    print("4. Go to your dashboard and find 'API Keys'")
    print("5. Copy your API key")
    print("6. Come back here and enter your API key")

    api_key = input("\nEnter your Fast2SMS API key (or press Enter to skip): ").strip()

    if api_key:
        # Update .env file
        env_path = "/Users/kapardhikannekanti/Freelance/mt5_CopyTrade/.env"

        try:
            # Read existing .env
            env_content = ""
            if os.path.exists(env_path):
                with open(env_path, 'r') as f:
                    env_content = f.read()

            # Update or add Fast2SMS configuration
            lines = env_content.split('\n')
            updated = False

            for i, line in enumerate(lines):
                if line.startswith('FAST2SMS_API_KEY='):
                    lines[i] = f"FAST2SMS_API_KEY={api_key}"
                    updated = True
                    break

            if not updated:
                lines.append(f"FAST2SMS_API_KEY={api_key}")

            # Write back to .env
            with open(env_path, 'w') as f:
                f.write('\n'.join(lines))

            print(f"✅ Fast2SMS API key saved to .env file")
            print("✅ SMS provider configured successfully!")

            return True

        except Exception as e:
            print(f"❌ Error saving configuration: {e}")
            return False
    else:
        print("⏭️ Skipping Fast2SMS setup")
        return False

def setup_twilio():
    print("\n🚀 Setting up Twilio (Global)")
    print("\nStep-by-step setup:")
    print("1. Go to https://www.twilio.com/try-twilio")
    print("2. Sign up for a free trial account")
    print("3. Verify your phone number")
    print("4. Get your Account SID, Auth Token, and Phone Number from console")

    account_sid = input("\nEnter your Twilio Account SID (or press Enter to skip): ").strip()

    if account_sid:
        auth_token = input("Enter your Twilio Auth Token: ").strip()
        from_number = input("Enter your Twilio phone number (e.g., +1234567890): ").strip()

        if account_sid and auth_token and from_number:
            env_path = "/Users/kapardhikannekanti/Freelance/mt5_CopyTrade/.env"

            try:
                # Read existing .env
                env_content = ""
                if os.path.exists(env_path):
                    with open(env_path, 'r') as f:
                        env_content = f.read()

                # Update .env file
                lines = env_content.split('\n')

                # Remove existing Twilio config
                lines = [line for line in lines if not line.startswith(('TWILIO_ACCOUNT_SID=', 'TWILIO_AUTH_TOKEN=', 'TWILIO_FROM_NUMBER='))]

                # Add new Twilio config
                lines.extend([
                    f"TWILIO_ACCOUNT_SID={account_sid}",
                    f"TWILIO_AUTH_TOKEN={auth_token}",
                    f"TWILIO_FROM_NUMBER={from_number}"
                ])

                # Write back to .env
                with open(env_path, 'w') as f:
                    f.write('\n'.join(lines))

                print(f"✅ Twilio configuration saved to .env file")
                print("✅ SMS provider configured successfully!")

                return True

            except Exception as e:
                print(f"❌ Error saving configuration: {e}")
                return False
        else:
            print("⚠️ Missing required Twilio credentials")
            return False
    else:
        print("⏭️ Skipping Twilio setup")
        return False

def test_sms_config():
    print("\n🧪 Testing SMS Configuration")

    # Test phone number
    test_number = input("\nEnter your phone number to test SMS (e.g., +919876543210): ").strip()

    if not test_number:
        print("⏭️ Skipping SMS test")
        return

    print(f"\n📱 Testing SMS to: {test_number}")
    print("💡 Check your phone for incoming SMS...")

    # Make API call to test SMS
    import requests
    import json

    try:
        response = requests.post(
            'http://localhost:8000/api/v1/auth/send-otp',
            headers={'Content-Type': 'application/json'},
            json={
                'mobile_or_email': test_number,
                'otp_type': 'mobile'
            }
        )

        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ SMS sent successfully!")
                print(f"📱 Check your phone ({test_number}) for the OTP")

                # If demo mode, show OTP
                if result.get('data', {}).get('otp'):
                    print(f"🔍 Demo OTP: {result['data']['otp']}")

            else:
                print(f"❌ SMS failed: {result.get('message', 'Unknown error')}")
        else:
            print(f"❌ API error: {response.status_code}")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("💡 Make sure the backend server is running on port 8000")

def show_status():
    print("\n📊 Current SMS Configuration Status")

    env_path = "/Users/kapardhikannekanti/Freelance/mt5_CopyTrade/.env"

    if not os.path.exists(env_path):
        print("❌ No .env file found")
        return

    with open(env_path, 'r') as f:
        env_content = f.read()

    # Check providers
    providers = {
        'Fast2SMS': 'FAST2SMS_API_KEY=' in env_content,
        'Twilio': all(key in env_content for key in ['TWILIO_ACCOUNT_SID=', 'TWILIO_AUTH_TOKEN=', 'TWILIO_FROM_NUMBER=']),
        'TextLocal': 'TEXTLOCAL_API_KEY=' in env_content,
        'MSG91': 'MSG91_API_KEY=' in env_content
    }

    configured_providers = [name for name, configured in providers.items() if configured]

    if configured_providers:
        print(f"✅ Configured providers: {', '.join(configured_providers)}")
        print("🚀 Real SMS is enabled!")
    else:
        print("⚠️ No SMS providers configured")
        print("📱 Currently using demo mode")

def main():
    print_banner()

    while True:
        print("\n🛠️ SMS Setup Options:")
        print("1. View available providers")
        print("2. Setup Fast2SMS (India)")
        print("3. Setup Twilio (Global)")
        print("4. Test SMS configuration")
        print("5. Show current status")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == '1':
            display_providers()
        elif choice == '2':
            setup_fast2sms()
        elif choice == '3':
            setup_twilio()
        elif choice == '4':
            test_sms_config()
        elif choice == '5':
            show_status()
        elif choice == '6':
            print("\n✅ SMS setup complete!")
            print("🚀 Restart your backend server to apply changes")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()