# 🚀 Complete Vercel Deployment Guide for MT5 Copy Trading Platform

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code should be in a GitHub repository
3. **MongoDB Atlas**: Set up a MongoDB database (if not already done)
4. **Domain** (Optional): Custom domain for your application

## Step-by-Step Deployment Process

### Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Verify project structure:**
   ```
   mt5_CopyTrade/
   ├── api/
   │   └── index.py              # ✅ Created
   ├── backend/
   │   ├── main.py              # ✅ Your FastAPI app
   │   ├── core/
   │   ├── api/
   │   ├── services/
   │   └── ...
   ├── vercel.json              # ✅ Created
   ├── requirements.txt         # ✅ Updated
   ├── .vercelignore           # ✅ Created
   └── .env.production         # ✅ Template created
   ```

### Step 2: Set Up MongoDB Atlas (Production Database)

1. **Go to [MongoDB Atlas](https://cloud.mongodb.com/)**

2. **Create/Configure Cluster:**
   - Create a new cluster or use existing
   - Choose a region close to your users
   - Use M0 (free tier) for testing, M2+ for production

3. **Set up Database Access:**
   - Database Access → Add New Database User
   - Username: `mt5_production_user`
   - Password: Generate a strong password
   - Built-in Role: `Read and write to any database`

4. **Configure Network Access:**
   - Network Access → Add IP Address
   - Add `0.0.0.0/0` (Allow access from anywhere)
   - ⚠️ For production, restrict to specific IPs if possible

5. **Get Connection String:**
   - Clusters → Connect → Connect your application
   - Copy the connection string
   - Replace `<username>`, `<password>`, and `<database>` with your values

### Step 3: Deploy to Vercel

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**

2. **Import Project:**
   - Click "New Project"
   - Import your GitHub repository
   - Select the `mt5_CopyTrade` repository

3. **Configure Build Settings:**
   - Framework Preset: **Other**
   - Root Directory: **/** (leave empty)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

4. **Click "Deploy"** (initial deployment will likely fail - that's normal)

### Step 4: Configure Environment Variables

1. **Go to Project Settings:**
   - In your Vercel project dashboard
   - Click "Settings" tab
   - Click "Environment Variables"

2. **Add ALL environment variables from `.env.production`:**

   **Required Variables:**
   ```
   SECRET_KEY = your-production-secret-key-min-32-characters-long
   MONGODB_URL = mongodb+srv://username:password@cluster.mongodb.net/mt5_copy_trading?retryWrites=true&w=majority
   DATABASE_NAME = mt5_copy_trading
   DEBUG = false
   ```

   **SMS Provider (Choose ONE):**
   ```
   # For Twilio
   TWILIO_ACCOUNT_SID = your_account_sid
   TWILIO_AUTH_TOKEN = your_auth_token
   TWILIO_FROM_NUMBER = +1234567890

   # OR for Fast2SMS (India)
   FAST2SMS_API_KEY = your_api_key

   # OR for TextLocal
   TEXTLOCAL_API_KEY = your_api_key

   # OR for MSG91
   MSG91_API_KEY = your_api_key
   MSG91_TEMPLATE_ID = your_template_id
   ```

   **Email Settings (Optional):**
   ```
   EMAIL_USERNAME = your_email@gmail.com
   EMAIL_PASSWORD = your_app_password
   EMAIL_FROM = your_email@gmail.com
   ```

3. **Important Notes:**
   - Set all variables for **Production** environment
   - Use strong, unique values for SECRET_KEY
   - Double-check MongoDB connection string
   - Don't include quotes around values

### Step 5: Set Up CORS for Production

1. **Update ALLOWED_HOSTS in environment variables:**
   ```
   ALLOWED_HOSTS = ["https://your-project-name.vercel.app"]
   ```

2. **If using custom domain:**
   ```
   ALLOWED_HOSTS = ["https://your-project-name.vercel.app", "https://your-custom-domain.com"]
   ```

### Step 6: Redeploy and Test

1. **Trigger Redeployment:**
   - Go to "Deployments" tab
   - Click "Redeploy" on the latest deployment
   - OR push a new commit to trigger auto-deployment

2. **Check Deployment Status:**
   - Wait for deployment to complete
   - Check for any build errors
   - Review function logs if needed

3. **Test Your API:**
   ```bash
   # Health check
   curl https://your-project-name.vercel.app/health

   # API documentation
   curl https://your-project-name.vercel.app/api/docs
   ```

### Step 7: Initialize Database (One-time setup)

1. **Run database initialization:**
   ```bash
   # Create admin user
   curl -X POST https://your-project-name.vercel.app/api/v1/auth/register \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Admin User",
       "email": "admin@yourdomain.com",
       "mobile": "+1234567890",
       "password": "Admin@123456",
       "country": "Your Country",
       "state": "Your State",
       "city": "Your City",
       "pin_code": "12345"
     }'
   ```

2. **Manually activate admin user in database** (if needed)

### Step 8: Set Up Custom Domain (Optional)

1. **Add Custom Domain:**
   - Project Settings → Domains
   - Add your domain name
   - Follow Vercel's DNS configuration instructions

2. **Update Environment Variables:**
   ```
   ALLOWED_HOSTS = ["https://your-custom-domain.com", "https://your-project-name.vercel.app"]
   ```

## Important Production Considerations

### Security Checklist
- ✅ Use strong SECRET_KEY (min 32 characters)
- ✅ Set DEBUG=false
- ✅ Configure proper CORS origins
- ✅ Use environment variables for all secrets
- ✅ Set up proper MongoDB user permissions
- ✅ Enable MongoDB authentication

### Performance Optimization
- ✅ Use MongoDB Atlas (managed service)
- ✅ Configure proper database indexes
- ✅ Set appropriate timeout values
- ✅ Monitor function execution time

### Monitoring and Logging
- ✅ Check Vercel function logs regularly
- ✅ Set up MongoDB Atlas monitoring
- ✅ Monitor API response times
- ✅ Set up error alerting

## Troubleshooting Common Issues

### Issue 1: Deployment Fails
**Solution:**
- Check build logs in Vercel dashboard
- Verify requirements.txt has all dependencies
- Ensure Python version compatibility

### Issue 2: Database Connection Fails
**Solution:**
- Verify MongoDB connection string
- Check MongoDB Atlas network access settings
- Ensure database user has proper permissions

### Issue 3: CORS Errors
**Solution:**
- Update ALLOWED_HOSTS environment variable
- Include both Vercel subdomain and custom domain
- Redeploy after changing environment variables

### Issue 4: Function Timeout
**Solution:**
- Optimize database queries
- Check for infinite loops
- Consider breaking large operations into smaller functions

### Issue 5: SMS/Email Not Working
**Solution:**
- Verify SMS provider credentials
- Check provider API documentation
- Test with demo mode first

## API Endpoints After Deployment

```
Base URL: https://your-project-name.vercel.app

Authentication:
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/send-otp
POST /api/v1/auth/verify-otp

Users:
GET /api/v1/users/profile
PUT /api/v1/users/profile

Groups:
GET /api/v1/groups
POST /api/v1/groups

Admin:
GET /api/v1/admin/users
POST /api/v1/admin/users/activate

Documentation:
GET /api/docs (Swagger UI)
GET /api/redoc (ReDoc)
```

## Post-Deployment Testing Script

Create this test script to verify your deployment:

```bash
#!/bin/bash
BASE_URL="https://your-project-name.vercel.app"

echo "Testing MT5 Copy Trading API Deployment..."

# Test 1: Health Check
echo "1. Health Check:"
curl -s "$BASE_URL/health" | jq

# Test 2: API Documentation
echo "2. API Documentation:"
curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/api/docs"

# Test 3: Registration
echo "3. User Registration:"
curl -X POST "$BASE_URL/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "mobile": "+1234567890",
    "password": "Test@123456",
    "country": "Test Country",
    "state": "Test State",
    "city": "Test City",
    "pin_code": "12345"
  }' | jq

echo "Deployment testing complete!"
```

## Support and Maintenance

### Regular Tasks:
1. **Monitor Vercel function usage** - Check for usage limits
2. **Update dependencies** - Keep packages up to date
3. **Review logs** - Check for errors and performance issues
4. **Backup database** - Regular MongoDB Atlas backups
5. **Security updates** - Monitor for security advisories

### Scaling Considerations:
- Monitor MongoDB Atlas performance metrics
- Consider upgrading Vercel plan for higher limits
- Implement caching strategies for frequently accessed data
- Set up load balancing if traffic increases significantly

---

🎉 **Congratulations!** Your MT5 Copy Trading platform is now deployed on Vercel!

For support, check:
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/)