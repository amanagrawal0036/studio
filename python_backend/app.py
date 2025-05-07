from flask import Flask, request, jsonify
from rag import answer_query_with_rag
from vector_db import VectorDB
from database import get_player_stats

app = Flask(__name__)

# Initialize VectorDB
vector_db = VectorDB()
# Add data from your database to the VectorDB
# vector_db.add_data(...)

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    try:
        answer = answer_query_with_rag(query, vector_db)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)