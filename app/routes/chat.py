from flask import Blueprint, request, jsonify
from app.utils.context_management import ContextManager

chat_bp = Blueprint('chat', __name__)
context_manager = ContextManager()

@chat_bp.route('/', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    session_id = data.get('session_id')
    response = context_manager.process(query, session_id)
    return jsonify({'response': response, 'conversation': context_manager.get_conversation(session_id)})
