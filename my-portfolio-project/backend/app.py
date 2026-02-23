import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
# This allows your frontend to talk to the backend without security blocks
CORS(app)

# Your confirmed Supabase credentials
SUPABASE_URL = "https://kowqprybqprnrutcsfuk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtvd3FwcnlicXBybnJ1dGNzZnVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4Mzk2MzQsImV4cCI6MjA4NzQxNTYzNH0.P8QqFv6S1OLhyZ9OaYJKaKmY0zsQoCwVuqT_e0xtPGg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/comments', methods=['GET'])
def get_comments():
    try:
        # Fetches messages from your 'guestbook' table
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

if __name__ == '__main__':
    # Port 5000 is standard for Flask
    app.run(host='0.0.0.0', port=5000, debug=True)