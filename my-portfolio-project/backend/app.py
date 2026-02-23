import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app) # Allows your Vue frontend to talk to this backend

# Use the exact names from your Vercel/Codespaces environment
URL = os.environ.get("https://dppypjnbrmhrenarjbvp.supabase.co")
KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRwcHlwam5icm1ocmVuYXJqYnZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4NDUyNzksImV4cCI6MjA4NzQyMTI3OX0.Y8JCPbmF-ygNT9MWpn9pwTNaVYb9A0zgfFVu0qoZfFU")

# Safety check: Prevents the "supabase_url is required" error
if not URL or not KEY:
    supabase = None
    print("WARNING: Supabase keys not found in environment!")
else:
    supabase: Client = create_client(URL, KEY)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    if not supabase:
        return jsonify({"error": "Backend not connected to database"}), 500
    try:
        response = supabase.table('guestbook').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST method logic goes here...

if __name__ == '__main__':
    # host='0.0.0.0' is required for GitHub Codespaces to see the app
    app.run(host='0.0.0.0', port=5000, debug=True)