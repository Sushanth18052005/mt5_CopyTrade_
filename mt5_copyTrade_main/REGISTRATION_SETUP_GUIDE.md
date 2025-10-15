# Complete Registration Flow Setup Guide

This guide explains how to set up the complete registration flow with database storage, Twilio SMS verification, and email verification.

## Features Implemented

✅ **Complete User Registration**
- Stores all user data in MongoDB
- Includes personal info, trading account details, and IB requirements
- Validates all required fields

✅ **Twilio SMS Integration**
- Sends OTP via SMS using Twilio
- Supports multiple SMS providers (Fast2SMS, TextLocal, MSG91)
- Fallback to demo mode for development

✅ **Email Verification with Nodemailer-like Service**
- Sends OTP via email using SMTP
- Beautiful HTML email templates
- Welcome emails and notifications

✅ **Complete OTP Flow**
- Mobile OTP verification
- Email OTP verification
- Secure OTP storage and validation

✅ **IB Proof Upload**
- Base64 image upload
- Admin approval workflow
- Email notifications

## Environment Variables Setup

Create a `.env` file in the `backend` directory with the following variables:

```bash
# Database
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority&appName=cluster
DATABASE_NAME=mt5_copy_trading

# SMS Settings (Twilio)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=+1234567890

# Email Settings (SMTP)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com

# Security
SECRET_KEY=your-super-secret-key-change-in-production
```

## SMS Provider Setup

### Option 1: Twilio (Recommended)
1. Sign up at [Twilio](https://www.twilio.com/try-twilio)
2. Get your Account SID and Auth Token
3. Purchase a phone number
4. Set the environment variables

### Option 2: Fast2SMS (India)
1. Sign up at [Fast2SMS](https://www.fast2sms.com/)
2. Get your API key
3. Set `FAST2SMS_API_KEY` in environment

### Option 3: TextLocal
1. Sign up at [TextLocal](https://www.textlocal.in/)
2. Get your API key
3. Set `TEXTLOCAL_API_KEY` in environment

## Email Setup

### Gmail Setup
1. Enable 2-factor authentication
2. Generate an App Password
3. Use the App Password as `EMAIL_PASSWORD`

### Other SMTP Providers
- **Outlook**: `smtp-mail.outlook.com:587`
- **Yahoo**: `smtp.mail.yahoo.com:587`
- **Custom SMTP**: Update `SMTP_SERVER` and `SMTP_PORT`

## API Endpoints

### Registration Flow
```
POST /api/v1/auth/register
POST /api/v1/auth/send-otp
POST /api/v1/auth/verify-otp
POST /api/v1/auth/upload-ib-proof
```

### Request Examples

#### 1. Register User
```json
{
  "name": "John Doe",
  "mobile": "+1234567890",
  "email": "john@example.com",
  "country": "United States",
  "state": "California",
  "city": "Los Angeles",
  "pin_code": "90210",
  "password": "password123",
  "broker": "Vantage",
  "account_no": "12345678",
  "trading_password": "trading123",
  "referral_code": "optional_code"
}
```

#### 2. Send OTP
```json
{
  "mobile_or_email": "+1234567890",
  "otp_type": "mobile"
}
```

#### 3. Verify OTP
```json
{
  "mobile_or_email": "+1234567890",
  "otp": "123456",
  "otp_type": "mobile"
}
```

#### 4. Upload IB Proof
```json
{
  "proof_image": "base64_encoded_image",
  "broker": "Vantage",
  "account_number": "12345678",
  "trading_password": "trading123"
}
```

## Database Schema

### Users Collection
```javascript
{
  "_id": ObjectId,
  "name": String,
  "mobile": String,
  "email": String,
  "country": String,
  "state": String,
  "city": String,
  "pin_code": String,
  "password_hash": String,
  "broker": String,
  "account_no": String,
  "trading_password_hash": String,
  "ib_status": String,
  "ib_proof_image_data": String,
  "mobile_verified": Boolean,
  "email_verified": Boolean,
  "status": String,
  "created_at": Date,
  "updated_at": Date
}
```

### OTP Records Collection
```javascript
{
  "_id": ObjectId,
  "mobile_or_email": String,
  "otp_code": String,
  "otp_type": String,
  "purpose": String,
  "expires_at": Date,
  "status": String,
  "created_at": Date
}
```

## Testing

Run the complete registration flow test:

```bash
python test_complete_registration.py
```

This will test:
- User registration
- SMS OTP sending
- Email OTP sending
- OTP verification
- User login
- IB proof upload

## Frontend Integration

The frontend `RegistrationFlow.tsx` component is already configured to work with these endpoints. It includes:

- Multi-step registration form
- OTP verification for both mobile and email
- IB proof upload
- Progress tracking
- Error handling

## Security Features

- Password hashing with SHA256
- OTP expiration (5 minutes)
- Rate limiting on OTP attempts
- Secure token-based authentication
- Input validation and sanitization

## Monitoring and Logs

- All OTP sends are logged
- Email delivery status is tracked
- Database operations are logged
- Error handling with detailed messages

## Production Considerations

1. **Environment Variables**: Use secure environment variable management
2. **Database**: Use MongoDB Atlas with proper security
3. **SMS**: Monitor SMS costs and usage
4. **Email**: Set up proper SPF/DKIM records
5. **Rate Limiting**: Implement API rate limiting
6. **Monitoring**: Set up application monitoring
7. **Backup**: Regular database backups

## Troubleshooting

### Common Issues

1. **SMS not sending**: Check Twilio credentials and phone number format
2. **Email not sending**: Verify SMTP credentials and firewall settings
3. **Database connection**: Check MongoDB connection string
4. **OTP verification failing**: Check OTP expiration and format

### Debug Mode

Set `DEBUG=True` in environment to enable detailed logging.

## Support

For issues or questions:
- Check the logs for detailed error messages
- Verify all environment variables are set correctly
- Test individual components using the test script
- Contact support with specific error messages

