# catcollector-review


Connect to the Remote
Let’s connect to a remote repo that you can sync with just in case you can’t resolve typos within a reasonable amount of time:

git init
git add -A
git commit -m "Initial commit"
git remote add origin https://git.generalassemb.ly/sei-blended-learning/catcollector.git
git fetch --all
👀 Got some typos or errors and need to sync your code?
**`git reset --hard origin/sync-1-setup`**