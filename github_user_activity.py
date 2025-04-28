import argparse
import requests


def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    fetched = requests.get(url)

    if fetched.status_code != 200:
        print("failed to fetch from the username!!! ")
        return
    
    events=fetched.json()

    for event in events:
        event_type=event['type']
        event_repo=event['repo']['name']
        created_time=event['created_at']
        print(f"{event_type} on {event_repo} repo at {created_time}")

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="fetch users Github activity")
    parser.add_argument("--username",type=str,required=True,help="Github username")
    args = parser.parse_args()
    
    fetch_user_activity(args.username)



