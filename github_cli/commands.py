import argparse
from github_cli.api import list_issues
from github_cli.utils import validate_repo_name

def run_cli():
    parser = argparse.ArgumentParser(description="GitHub Issue CLI")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List issues")
    list_parser.add_argument("--repo", required=True, help="user/repo")

    args = parser.parse_args()

    if args.command == "list":
        if not validate_repo_name(args.repo):
            print("❌ Invalid repository format. Use 'owner/repo'.")
            return
        list_issues(args.repo)
