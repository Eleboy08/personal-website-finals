from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os

app = Flask(__name__)
CORS(app)

url = os.environ.get("https://dppypjnbrmhrenarjbvp.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRwcHlwam5icm1ocmVuYXJqYnZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4NDUyNzksImV4cCI6MjA4NzQyMTI3OX0.Y8JCPbmF-ygNT9MWpn9pwTNaVYb9A0zgfFVu0qoZfFU)
supabase: Client = create_client(url, key)

@app.route('/api/comments', methods=['GET', 'POST', 'OPTIONS'], strict_slashes=False)
def handle_comments():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    try:
        if request.method == 'GET':
            response = supabase.table('guestbook').select("*").execute()
            return jsonify(response.data if response.data else []), 200
        
        if request.method == 'POST':
            data = request.json
            response = supabase.table('guestbook').insert(data).execute()
            return jsonify(response.data), 201
            
    except Exception as e:
        print(f"Database Error: {e}")
        return jsonify({"error": str(e)}), 500