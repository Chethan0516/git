import os

# create a repo
gh repo create <REPO_NAME>

gh repo create my-new-repo --public --description "My new project" --enable-issues

git clone https://github.com/YourUsername/my-new-repo.git

gh auth login


# Configure git( First-time setup)
# git config --global user.name "username"
# git config --global user.email "email"

# check configurations
# git config --list

# Initialize a Git Repository:
# git init

# Clone a Repository:
# repository_url = "https://github.com/username/repository.git"
# clone_directory = "/path/to/clone/directory"
# os.system(f"git clone {repository_url} {clone_directory}")
#   or
# git clone <repository_url>


# Staging and Committing Changes
# Check Current Status:
    # git status 
# Add changes 
    # git add filename or git add .
# commit changes 
    # git commit -m "message" or git commit -am "message"


# Branch Management
# Create a New Branch:
    # git branch branch_name
# switch to branch 
    # git checkout branch_name
# create and switch branch 
    # git chechout -b branch_name
# merge branch 
    # git merge branch_name
# delete branch
    # git branch -d branch_name // Locally
    # git branch -D branch_name // Force delete
# list branches
    # git branch -a




# Remote Repositories
# Add a Remote Repository
    # git remote add origin url
# View Remote Repositories
    # git remote -v 
# Push Changes to Remote Repository
    # git push origin branch_name
# Pull Changes from Remote Repository
    # git pull origin name
# fetch changes
    # git fetch
# Remove a Remote
    # git remote remove name


