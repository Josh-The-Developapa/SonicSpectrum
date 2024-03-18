#!/bin/zsh

# Directory containing the repositories
repo_dir="$HOME/repos"

# Function to merge panic branch into master and delete panic branch
merge_and_delete_panic_branch() {
    local repo=$1
    cd "$repo" || { echo "Error: Directory not found - $repo"; return 1; }

    # Check if panic branch exists
    if git show-ref --verify --quiet "refs/heads/panic"; then
        echo "Merging panic branch into master for repo: $repo"
        git checkout master && git merge --no-ff panic && git branch -d panic
        echo "Panic branch merged and deleted for repo: $repo"
    else
        echo "Panic branch does not exist for repo: $repo"
    fi
}

# Iterate over each repository in the directory
for repo in "$repo_dir"/*; do
    if [ -d "$repo" ]; then
        merge_and_delete_panic_branch "$repo"
    fi
done

