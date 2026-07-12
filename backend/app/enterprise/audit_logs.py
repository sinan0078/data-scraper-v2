
class AuditLogger:
    def log(self, user_id, action):
        return {
            "user_id": user_id,
            "action": action
        }
