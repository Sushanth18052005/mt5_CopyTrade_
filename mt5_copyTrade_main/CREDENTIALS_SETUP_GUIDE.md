# 🔐 **Credentials Setup Guide**

This guide will help you set up Twilio (SMS) and SMTP (Email) credentials for the registration flow.

## 📁 **Where to Add Credentials**

Create a `.env` file in the `backend` directory with the following content:

```env
# ===================================
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
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_FROM_NUMBER=+1234567890

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
```

---

## 📱 **How to Get Twilio Credentials**

### Step 1: Create Twilio Account
1. Go to [https://www.twilio.com](https://www.twilio.com)
2. Click "Sign up for free"
3. Verify your phone number
4. Complete the account setup

### Step 2: Get Your Credentials
1. After logging in, go to the [Twilio Console Dashboard](https://console.twilio.com/)
2. You'll see your **Account SID** and **Auth Token** on the main dashboard
3. Copy these values to your `.env` file

### Step 3: Get a Phone Number
1. In the Twilio Console, go to **Phone Numbers** → **Manage** → **Buy a number**
2. Choose a number (preferably toll-free for better delivery)
3. Copy the phone number to `TWILIO_FROM_NUMBER` in your `.env` file

### Step 4: Verify Your Account (Free Trial)
- Twilio gives you $15 free credit
- You can send SMS to verified numbers only during trial
- To send to any number, you need to upgrade to a paid account

---

## 📧 **How to Get SMTP Credentials**

### Option 1: Gmail (Recommended for Development)

#### Step 1: Enable 2-Factor Authentication
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click **Security** → **2-Step Verification**
3. Enable 2-factor authentication

#### Step 2: Generate App Password
1. In Google Account Settings, go to **Security**
2. Click **App passwords** (you might need to search for it)
3. Select **Mail** and **Other (Custom name)**
4. Enter "MT5 Copy Trading" as the name
5. Copy the generated 16-character password
6. Use this password in `EMAIL_PASSWORD` in your `.env` file

#### Step 3: Update .env File
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your_gmail@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
EMAIL_FROM=your_gmail@gmail.com
```

### Option 2: Other Email Providers

#### Outlook/Hotmail
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@outlook.com
EMAIL_PASSWORD=your_password
EMAIL_FROM=your_email@outlook.com
```

#### Yahoo
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@yahoo.com
EMAIL_PASSWORD=your_app_password
EMAIL_FROM=your_email@yahoo.com
```

#### Custom SMTP Server
```env
SMTP_SERVER=your_smtp_server.com
SMTP_PORT=587
EMAIL_USERNAME=your_username
EMAIL_PASSWORD=your_password
EMAIL_FROM=your_email@yourdomain.com
```

---

## 🚀 **Testing Your Setup**

### 1. Test SMS (Twilio)
```bash
# Run this in your backend directory
python -c "
import asyncio
from backend.services.real_sms_service import real_sms_service

async def test_sms():
    result = await real_sms_service.send_otp_sms('+1234567890', '123456', 'test')
    print('SMS Test Result:', result)

asyncio.run(test_sms())
"
```

### 2. Test Email (SMTP)
```bash
# Run this in your backend directory
python -c "
import asyncio
from backend.services.email_service import email_service

async def test_email():
    result = await email_service.send_otp_email('test@example.com', '123456', 'test')
    print('Email Test Result:', result)

asyncio.run(test_email())
"
```

### 3. Test Complete Registration Flow
```bash
# Run the complete test
python test_complete_registration.py
```

---

## 🔧 **Troubleshooting**

### Common Twilio Issues:
- **"Authentication Error"**: Check Account SID and Auth Token
- **"Invalid phone number"**: Ensure phone number includes country code (+1 for US)
- **"Trial account"**: Verify the destination number in Twilio Console

### Common Email Issues:
- **"Authentication failed"**: Use App Password, not regular password
- **"Connection refused"**: Check SMTP server and port
- **"SSL/TLS error"**: Try port 465 with SSL instead of 587 with STARTTLS

### Debug Mode:
The system will show detailed error messages in the console when credentials are missing or incorrect.

---

## 💰 **Cost Estimates**

### Twilio SMS:
- **Free Trial**: $15 credit (about 1,500 SMS)
- **Paid**: ~$0.0075 per SMS in US
- **Phone Number**: ~$1/month

### Email (Gmail):
- **Free**: Up to 500 emails/day
- **Google Workspace**: $6/month for 2,000 emails/day

---

## 🛡️ **Security Notes**

1. **Never commit `.env` file to Git**
2. **Use App Passwords, not regular passwords**
3. **Rotate credentials regularly**
4. **Use environment variables in production**
5. **Monitor usage to avoid unexpected charges**

---

## 📞 **Support**

If you encounter issues:
1. Check the console logs for detailed error messages
2. Verify all credentials are correct
3. Test individual services using the test scripts above
4. Check Twilio/Email provider status pages

The system is designed to work even without credentials (demo mode), but real SMS/Email requires proper setup.
