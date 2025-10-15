# MT5 Copy Trading Platform - Complete Testing Guide

## 🚀 Getting Started

### Prerequisites
- Node.js installed
- Application running on `http://localhost:3001`

### Starting the Application
```bash
cd frontend
npm run dev
```
The application will start on `http://localhost:3001`

---

## 🔐 Authentication System Testing

### Login Types Available
The platform supports three login types with different interfaces:

1. **User Login** - Copy trading members
2. **Admin Login** - Platform administrators
3. **Master Login** - Group master traders

### Demo Credentials

#### User Login
- **Email:** `user@test.com`
- **Password:** `user123`
- **Mobile:** `+1234567890`

#### Admin Login
- **Email:** `admin@test.com`
- **Password:** `admin123`
- **Mobile:** `+1234567891`

#### Master Login
- **Email:** `master@test.com`
- **Password:** `master123`
- **Mobile:** `+1234567892`

---

## 📱 SMS/OTP System Testing

### How it Works
1. Enter email and password for any user type
2. Click "Send OTP" - system sends SMS to the associated mobile number
3. **In Demo Mode:** OTP appears in console log AND as a visual notification on screen
4. Enter the 6-digit OTP to complete login

### Demo Mode Features
- **Visual Notification:** Black popup shows OTP details for 10 seconds
- **Console Logging:** Check browser console for OTP details
- **No Real SMS:** Safe for testing without actual SMS costs

### Testing Steps
1. **Login Process:**
   - Select login type (User/Admin/Master)
   - Enter demo credentials
   - Click "Send OTP"
   - Watch for popup notification with OTP
   - Enter OTP and verify

2. **OTP Features to Test:**
   - **Resend OTP:** Click "Resend OTP" button
   - **Wrong OTP:** Enter incorrect OTP (3 attempts max)
   - **Expired OTP:** Wait 5 minutes for expiry
   - **Back to Login:** Return to credential entry

### Expected Behavior
- ✅ OTP popup appears immediately after "Send OTP"
- ✅ Console shows detailed OTP information
- ✅ Valid OTP logs in successfully
- ✅ Invalid OTP shows error with attempts remaining
- ✅ Expired OTP shows expiry message

---

## 👤 User Panel Testing

### Available Screens
1. **Dashboard** - Overview and performance metrics
2. **Available Groups** - Browse trading groups to join
3. **My Groups** - Groups you've joined
4. **Profile** - Personal information
5. **Accounts** - Trading account management

### Testing Checklist
- [ ] Dashboard loads with performance statistics
- [ ] Available Groups shows group listings with join buttons
- [ ] My Groups displays joined groups and copy settings
- [ ] Profile shows user information and edit functionality
- [ ] Accounts displays linked trading accounts
- [ ] Navigation between screens works smoothly
- [ ] Logout functionality works

---

## ⚙️ Admin Panel Testing

### Available Screens
1. **Group Creation** - Create new trading groups
2. **Group Management** - Manage existing groups
3. **Settlement Management** - Approve/manage settlements
4. **Member Approvals** - Approve new member registrations
5. **Master Management** - Manage master trader accounts
6. **Error Reporting** - View system errors and logs
7. **Symbol Mapping** - Configure trading symbol mappings

### Testing Checklist
- [ ] Group Creation form works with validation
- [ ] Group Management shows active groups with controls
- [ ] Settlement Management displays pending settlements
- [ ] Member Approvals shows pending member requests
- [ ] Master Management lists all master traders
- [ ] Error Reporting displays system errors
- [ ] Symbol Mapping allows configuration changes
- [ ] All forms submit successfully
- [ ] Data displays correctly in tables

---

## 📈 Master Panel Testing

### Available Screens
1. **Dashboard** - Group performance overview
2. **My Group** - Detailed group management
3. **Members** - Manage group members
4. **Performance** - Detailed analytics
5. **Settings** - Group configuration
6. **Accounts** - Trading account management

### Testing Checklist
- [ ] Dashboard shows group statistics and performance
- [ ] My Group displays detailed group information
- [ ] Members screen shows follower list and management
- [ ] Performance displays trading analytics and charts
- [ ] Settings allows group configuration changes
- [ ] Accounts shows linked trading accounts
- [ ] Real-time data updates work
- [ ] Member management functions work

---

## 🔄 Registration Flow Testing

### 4-Step Process
1. **Personal Info** - Basic user details
2. **Verification** - Mobile and email OTP
3. **Account Linking** - MT4/MT5 account connection
4. **Review** - Account under review status

### Testing Steps
1. **Access Registration:**
   - Click "New User Registration" from login screen
   - Fill personal information form
   - Click "Send Verification Code"

2. **OTP Verification:**
   - Enter mobile OTP (check notification popup)
   - Enter email OTP (same OTP for demo)
   - Click "Verify & Continue"

3. **Account Linking:**
   - Select broker (Vantage, Exness, XM)
   - Choose account type and server
   - Enter Partner ID and account details
   - Submit for review

4. **Review Status:**
   - View submitted account details
   - See review status and timeline
   - Access dashboard after approval

---

## 🛠 Technical Testing

### Browser Compatibility
Test on:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

### Responsive Design
Test on:
- [ ] Desktop (1920x1080)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)

### Performance Testing
- [ ] Page load times under 3 seconds
- [ ] Smooth animations and transitions
- [ ] No console errors
- [ ] Memory usage stays reasonable

---

## 🐛 Common Issues & Solutions

### SMS/OTP Issues
**Problem:** OTP not showing
**Solution:** Check browser console and ensure popup blockers are disabled

**Problem:** OTP expired
**Solution:** Click "Resend OTP" to get a new code

### Authentication Issues
**Problem:** Login not working
**Solution:** Use exact demo credentials provided above

**Problem:** Session lost
**Solution:** Check localStorage for auth tokens

### Navigation Issues
**Problem:** Wrong panel showing
**Solution:** Logout and login with correct user type

---

## 🔧 Development Testing

### Build Testing
```bash
npm run build
```
Should complete without errors.

### Linting
```bash
npm run lint
```
Should pass all linting rules.

### Type Checking
TypeScript compilation should pass without errors.

---

## 📊 Test Data

### Demo Group Data
- **Group Names:** "Swing Traders Pro", "Day Trading Elite", "Scalping Masters"
- **Master Traders:** John Smith, Sarah Wilson, Mike Chen
- **Performance Metrics:** All positive returns for demo purposes

### Demo Trading Data
- **Symbols:** EURUSD, XAUUSD, GBPUSD, USDJPY
- **Trade Types:** BUY/SELL positions
- **P&L:** Mix of profitable and losing trades

---

## ✅ Final Verification Checklist

### Core Functionality
- [ ] All three login types work with OTP
- [ ] Each user type sees only their interface
- [ ] SMS/OTP system functions correctly
- [ ] All navigation works without errors
- [ ] Registration flow completes successfully
- [ ] Logout works from all panels

### UI/UX Testing
- [ ] Design matches provided mockups
- [ ] All buttons and forms are functional
- [ ] Responsive design works on all devices
- [ ] Loading states and animations work
- [ ] Error messages display correctly

### Production Readiness
- [ ] No console errors
- [ ] Build completes successfully
- [ ] All TypeScript types are properly defined
- [ ] No accessibility issues
- [ ] SEO meta tags are present

---

## 🚀 Production Deployment Notes

### Environment Variables
For production SMS functionality, configure:
```
NEXT_PUBLIC_SMS_API_KEY=your_twilio_key
NEXT_PUBLIC_TWILIO_ACCOUNT_SID=your_account_sid
NEXT_PUBLIC_TWILIO_AUTH_TOKEN=your_auth_token
NEXT_PUBLIC_TWILIO_PHONE_NUMBER=your_twilio_number
```

### Security Considerations
- Replace demo credentials with secure authentication
- Implement proper JWT token management
- Add rate limiting for OTP requests
- Enable HTTPS in production
- Implement proper CORS policies

---

## 📞 Support

For technical issues during testing:
1. Check browser console for errors
2. Verify all dependencies are installed
3. Ensure port 3001 is available
4. Clear browser cache if needed

**The application is now fully functional with all features working as intended!**