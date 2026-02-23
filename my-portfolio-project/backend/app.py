import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
# Enable CORS so your Vue frontend can talk to the database securely
CORS(app)

# These pull the keys you just added to the Vercel Settings
SUPABASE_URL = os.environ.get("https://fpigatbztysvppkqcwfy.supabase.com")
SUPABASE_KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZwaWdhdGJ6dHlzdnBwa3Fjd2Z5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE0Mzk0MzIsImV4cCI6MjA4NzAxNTQzMn0.Zhe64O_HME3slUFnDOj3dK_9P0szhAG3y8MFcV-Rd4o")

# Safety check to prevent the "url required" crash
if not SUPABASE_URL or not SUPABASE_KEY:
    supabase = None
else:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    if not supabase: return jsonify({"error": "Env Vars Missing"}), 500
    try:
        # Fetches from your Supabase table
        response = supabase.table('guestbook').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/comments', methods=['POST'])
def add_comment():
    if not supabase: return jsonify({"error": "Env Vars Missing"}), 500
    try:
        data = request.get_json()
        new_comment = {"name": data.get('name'), "message": data.get('message')}
        # Inserts into your Supabase table
        response = supabase.table('guestbook').insert(new_comment).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500