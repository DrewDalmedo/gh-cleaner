from github import Github
import re
import os
import argparse

def get_args():
    """Get command-line args"""

    # set up argument parser
    parser = argparse.ArgumentParser(description='Delete Github repositories that match regex patterns')

    """-p / --patterns: What regex patterns to match repos against. Required."""
    parser.add_argument("-p", "--patterns", nargs='+', 
                        help="What regex patterns to match repos against. Required.")

    """-l / --list: List repos that would be deleted without deleting them"""
    parser.add_argument("-l", "--list", action="store_true",
                        help="List repos that would be deleted without deleting them")

    
    """-f / --force: Delete all repos without y/n confirmation"""
    parser.add_argument("-f", "--force", action="store_true",
                        help="Delete all repos without y/n confirmation")

    return parser.parse_args()

def confirm_deletion(repo_name, force=False):
    """Deletion confirmation logic"""
    if force:
        return True

    confirmation = input(f"Delete {repo_name}? (Y/n) ").lower()

    if confirmation in ['y', '']:
        return True
    if confirmation == 'n':
        return False

    raise ValueError("Invalid confirmation")

def delete_repo(repo, safe_mode=False):
    """Handle repo deletion with safe mode check"""

    if safe_mode:
        print(f"(SAFE_MODE) Would delete {repo.name}")
        return

    repo.delete()
    print(f"Deleted {repo.name}")

def main():
    args = get_args()
    
    if not args.patterns:
        raise ValueError("No patterns provided, please specify at least 1 regex pattern to match repositories against. See --help for more details.")

    patterns = [re.compile(pattern) for pattern in args.patterns]

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set.\nDid you set it in your .env file?")

    g = Github(token)
    user = g.get_user()

    for repo in user.get_repos():
        if any(pattern.search(repo.name) for pattern in patterns):
            if args.list:
                print(repo.name)
                continue
            
            if confirm_deletion(repo.name, args.force):
                delete_repo(repo, safe_mode=bool(os.getenv("SAFE_MODE") ) )

if __name__ == "__main__":
    main()
