import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
# Allow your Vue frontend to communicate with this API
CORS(app)

# Pulls credentials from environment variables (important for Render deployment)
SUPABASE_URL = os.environ.get("SUPABASE_URL", "YOUR_SUPABASE_URL_HERE")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "YOUR_SUPABASE_ANON_KEY_HERE")

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
        name = data.get('name')
        message = data.get('message')

        if not name or not message:
            return jsonify({"error": "Name and message are required"}), 400

        new_comment = {"name": name, "message": message}
        response = supabase.table('guestbook').insert(new_comment).execute()
        
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)