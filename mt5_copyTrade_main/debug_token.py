#!/usr/bin/env python3
"""Debug the actual token from login"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.core.security import decode_token

# Token from the login response
token = "30Mc3yyyrp0Ev025rYtT2jYOya9Q2MebnDycjy3R1gw"

print(f"Testing token: {token}")

try:
    payload = decode_token(token)
    print(f"✅ Token decoded successfully: {payload}")
except Exception as e:
    print(f"❌ Token decode failed: {e}")
    print(f"Token length: {len(token)}")
    print(f"Token type: {type(token)}")