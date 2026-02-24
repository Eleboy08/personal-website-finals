from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
# Allow the browser to securely connect
CORS(app, resources={r"/*": {"origins": "*"}})

url = "https://dppypjnbrmhrenarjbvp.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRwcHlwam5icm1ocmVuYXJqYnZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4NDUyNzksImV4cCI6MjA4NzQyMTI3OX0.Y8JCPbmF-ygNT9MWpn9pwTNaVYb9A0zgfFVu0qoZfFU"
supabase: Client = create_client(url, key)

# Catch-all route to prevent any path mismatches
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    try:
        if request.method == 'GET':
            response = supabase.table('guestbook').select("*").execute()
            return jsonify(response.data if hasattr(response, 'data') else []), 200
        
        if request.method == 'POST':
            # force=True stops the server from crashing if Vue misses a header
            data = request.get_json(force=True, silent=True) or {}
            
            # Extract exactly what your Supabase table requires
            safe_data = {
                "name": data.get("name", "Anonymous"),
                "message": data.get("message", "No message provided")
            }
            
            supabase.table('guestbook').insert(safe_data).execute()
            return jsonify({"status": "success", "inserted": safe_data}), 201
            
    except Exception as e:
        print(f"CRASH REPORT: {str(e)}")
        return jsonify({"error": str(e)}), 500