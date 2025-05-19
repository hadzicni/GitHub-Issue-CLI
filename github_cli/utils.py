def validate_repo_name(repo: str) -> bool:
    return "/" in repo and len(repo.split("/")) == 2
