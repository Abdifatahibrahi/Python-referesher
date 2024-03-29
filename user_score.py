class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement = engagement

    def __repr__(self):
        return f'<user {self.name}>'
    
def get_user_score(user):
    try:
        return perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function")

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}.")

my_user = User('Rolf', {'clicks': 61, 'hits': 100})
get_user_score(my_user)


        