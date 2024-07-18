class ContextManager:
    def __init__(self):
        self.sessions = {}

    def process(self, query, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(query)
        # Implement your context management logic here
        response = f"Processed query: {query} in session: {session_id}"
        return response
