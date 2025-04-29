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
        event_time=event['created_at']

        if event_type== "PushEvent":
            commit_count=len(event['payload']['commits'])
            print(f"Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {event_repo} at {event_time}")
        elif event_type == "WatchEvent":
            print(f"Starred on {event_repo}")
        elif event_type=="CommitCommentEvent":
            action = event['payload']['action']
            print(f"{action} a comment on a commit on {event_repo} at {event_time} ")
        elif event_type == "CreateEvent":
            ref_type = event['payload']['ref_type']
            print(f"Created a {ref_type} on {event_repo} at {event_time}")
        else:
            print(f"{event_type} on {event_repo} at {event_time}")

        

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="fetch users Github activity")
    parser.add_argument("--username",type=str,required=True,help="Github username")
    args = parser.parse_args()
    
    fetch_user_activity(args.username)



