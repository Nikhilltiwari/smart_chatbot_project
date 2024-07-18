from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationMemory

class ContextManager:
    def __init__(self):
        self.sessions = {}
        self.conversation_memory = {}

    def create_session(self, session_id):
        self.sessions[session_id] = ConversationChain(llm=OpenAI(), memory=ConversationMemory())
        self.conversation_memory[session_id] = []

    def process(self, query, session_id):
        if session_id not in self.sessions:
            self.create_session(session_id)
        self.conversation_memory[session_id].append(query)
        response = self.sessions[session_id].predict(input=query)
        self.conversation_memory[session_id].append(response)
        return response

    def get_conversation(self, session_id):
        return self.conversation_memory.get(session_id, [])
