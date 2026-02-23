import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

# Pulls the keys you just added to the Vercel Settings
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    try:
        response = supabase.table('guestbook').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/comments', methods=['POST'])
def add_comment():
    try:
        data = request.get_json()
        new_comment = {"name": data.get('name'), "message": data.get('message')}
        response = supabase.table('guestbook').insert(new_comment).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500