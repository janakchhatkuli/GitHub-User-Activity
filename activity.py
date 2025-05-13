#!/usr/bin/env python3
import requests


def fetch_user_activity(username,event_type_filter=None):
    url = f"https://api.github.com/users/{username}/events"
    fetched = requests.get(url)

    if fetched.status_code != 200:
        return {"error":"failed to fetch from the username!!! "}
        
    
    events=fetched.json()
    result =[]

    for event in events:
        event_type=event['type']

        if event_type_filter and event_type != event_type_filter:
            continue
        
        event_repo=event['repo']['name']
        event_time=event['created_at']

        if event_type== "PushEvent":
            commit_count=len(event['payload']['commits'])
            result.append(f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {event_repo} at {event_time}")
        elif event_type == "WatchEvent":
            result.append(f"- Starred on {event_repo}")
        elif event_type=="CommitCommentEvent":
            action = event['payload']['action']
            result.append(f"- {action} a comment on a commit on {event_repo} at {event_time} ")
        elif event_type == "CreateEvent":
            ref_type = event['payload']['ref_type']
            ref = event['payload']['ref']
            result.append(f"- Created a {ref_type} {f": {ref} on {event_repo}" if ref != None else f' {event_repo}'} at {event_time}")
        elif event_type == "DeleteEvent":
            ref_type = event['payload']['ref_type']
            ref = event['payload']['ref']
            result.append(f"- Deleted a {ref_type} {f": {ref} on {event_repo}" if ref != None else f' {event_repo}'} at {event_time}")
        elif event_type == "ForkEvent":
            result.append(f"- Forked  {event_repo} repo  at {event_time}")

        elif event_type == "IssueCommentEvent":
            action = event['payload']['action']
            result.append(f"- {action.capitalize()} a comment on {event_repo} at {event_time}")
        
        elif event_type == "IssuesEvent" :
            action = event['payload']['action']
            result.append(f"- {action.capitalize()} a Issue on {event_repo} at {event_type} ")

        elif event_type == "PullRequestEvent" :
            action = event['payload']['action']
            pull_req = event['payload']['pull_request']['title']
            result.append(f"- {action.capitalize()} a Pull Request \"{pull_req}\" on {event_repo} at {event_time}")


        else:
            result.append(f"- {event_type} on {event_repo} at {event_time}")

    return result if result else ["No matching activities found."]  



    



