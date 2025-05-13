import argparse
from activity import fetch_user_activity

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="fetch users Github activity")
    parser.add_argument("--username",type=str,required=True,help="Github username")
    parser.add_argument("--type",type=str,required=False,help = "filter by event type like --event_type PushEvent")
    args = parser.parse_args()
    
    fetch_user_activity(args.username,args.type)
    