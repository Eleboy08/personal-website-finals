from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# Pull secure keys from Vercel Environment Variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# strict_slashes=False stops Vercel from getting confused by trailing slashes
# We MUST include 'OPTIONS' for the browser's security preflight checks
@app.route('/api/comments', methods=['GET', 'POST', 'OPTIONS'], strict_slashes=False)
def handle_comments():
    # 1. Handle CORS Preflight (Fixes the 405 error)
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    try:
        # 2. Handle Fetching Messages
        if request.method == 'GET':
            response = supabase.table('guestbook').select("*").execute()
            # Return empty list instead of crashing if table is completely empty
            return jsonify(response.data if response.data else []), 200
        
        # 3. Handle New Messages
        if request.method == 'POST':
            data = request.json
            response = supabase.table('guestbook').insert(data).execute()
            return jsonify(response.data), 201
            
    except Exception as e:
        # If Supabase fails, this catches it so the server doesn't crash
        print(f"Database Error: {e}")
        return jsonify({"error": str(e)}), 500

# Catch-all route to help debug if Vercel routes something weirdly
@app.route('/api/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    return jsonify({"error": f"Route /api/{path} not found in Flask"}), 404