
class SubscriptionService:
    def create_subscription(self, user_id: int, plan: str):
        return {"user_id": user_id, "plan": plan}
