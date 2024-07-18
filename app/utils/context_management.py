from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain

class ContextManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id):
        self.sessions[session_id] = {
            'chain': ConversationChain(llm=OpenAI()),
            'memory': []
        }

    def process(self, query, session_id):
        if session_id not in self.sessions:
            self.create_session(session_id)
        self.sessions[session_id]['memory'].append(query)
        response = self.sessions[session_id]['chain'].predict(input=query)
        self.sessions[session_id]['memory'].append(response)
        return response

    def get_conversation(self, session_id):
        return self.sessions.get(session_id, {}).get('memory', [])





