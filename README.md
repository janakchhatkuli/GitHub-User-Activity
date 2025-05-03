# GitHub-User-Activity
GitHub API to fetch user activity and display it in the terminal.

URL of the Project Guideline : https://roadmap.sh/projects/github-user-activity

All commands are listed below :

# Fetching activity from username
python activity.py --username your_username

# Filtering by event_type
python activity.py --username your_username --type event_name

# All the event_type:
| Event Type                      | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| `CommitCommentEvent`            | A comment on a commit.                              |
| `CreateEvent`                   | A repository, branch, or tag was created.           |
| `DeleteEvent`                   | A branch or tag was deleted.                        |
| `ForkEvent`                     | A repository was forked.                            |
| `GollumEvent`                   | A wiki page was created or updated.                 |
| `IssueCommentEvent`             | A comment on an issue.                              |
| `IssuesEvent`                   | An issue was opened, closed, labeled, etc.          |
| `MemberEvent`                   | A user was added as a collaborator.                 |
| `PublicEvent`                   | A repository was made public.                       |
| `PullRequestEvent`              | A pull request was opened, closed, or synchronized. |
| `PullRequestReviewEvent`        | A review was submitted on a pull request.           |
| `PullRequestReviewCommentEvent` | A comment was made on a pull request's diff.        |
| `PushEvent`                     | Code was pushed to a repository.                    |
| `ReleaseEvent`                  | A release was published.                            |
| `SponsorshipEvent`              | A sponsorship activity occurred.                    |
| `WatchEvent`                    | A user starred a repository.                        |


