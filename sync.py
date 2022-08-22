
import sys
from git import Repo
from Track.colab_sync import download_from_drive

repo_path = "D:\Github\DS_Algo_Playground"
colab_tracker_path = "D:\Github\DS_Algo_Playground\Track"

def update_push_to_gitub(commit_msg="Files changed/updated", branch_name = "master"):
    repo = Repo(repo_path)
    repo.remotes.origin.pull()
    
    # git add . | git add -all
    repo.git.add(all=True)

    # git commit -m "Message"
    repo.git.commit(m=commit_msg)

    repo.git.push('--set-upstream', repo.remote().name, branch_name)


if __name__ == "__main__":
    '''
        Git Add -> Commit -> Push : python sync.py
        Git Add -> Commit(msg) -> Push : $python sync.py "commit_msg"
        Colab Sync -> Git Add -> Commit(msg) -> Push : $python sync.py "commit_msg" csync
    '''
    n_args = len(sys.argv)
    print("Arguments passed: ", sys.argv)
    file_name = sys.argv[0]

    # update from colab if passed
    if sys.argv[-1] == "csync":
        download_from_drive(colab_tracker_path)

    # commit message specified
    if n_args == 2:
        update_push_to_gitub(commit_msg=sys.argv[1])
    else: # no commit message passed
        update_push_to_gitub()