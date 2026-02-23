import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
# Enable CORS so your Vue site can talk to this API
CORS(app)

# Pulls secrets from Vercel Settings
# Ensure these match the KEYS you typed in the Vercel Dashboard
URL = os.environ.get("https://fpigatbztysvppkqcwfy.supabase.co")
KEY = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZwaWdhdGJ6dHlzdnBwa3Fjd2Z5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE0Mzk0MzIsImV4cCI6MjA4NzAxNTQzMn0.Zhe64O_HME3slUFnDOj3dK_9P0szhAG3y8MFcV-Rd4o")

# Safety check to prevent the crash you saw earlier
if not URL or not KEY:
    supabase = None
else:
    supabase: Client = create_client(URL, KEY)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    if not supabase: return jsonify({"error": "Missing Vercel Env Vars"}), 500
    try:
        response = supabase.table('guestbook').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/comments', methods=['POST'])
def add_comment():
    if not supabase: return jsonify({"error": "Missing Vercel Env Vars"}), 500
    try:
        data = request.get_json()
        new_comment = {"name": data.get('name'), "message": data.get('message')}
        response = supabase.table('guestbook').insert(new_comment).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()