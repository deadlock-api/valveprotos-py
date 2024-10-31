import os

import requests
from github import Github
from github.ContentFile import ContentFile
from github.Repository import Repository

REPO = "SteamDatabase/Protobufs"


def download(c: ContentFile, out: str):
    r = requests.get(c.download_url)
    output_path = f"{out}/{c.path}"  #
    filename = os.path.basename(c.path)
    if not filename.startswith("citadel") and filename not in [
        "citadel_gcmessages_client.proto",
        "gcsdk_gcmessages.proto",
        "steammessages_steamlearn.steamworkssdk.proto",
        "citadel_gcmessages_common.proto",
        "netmessages.proto",
        "steammessages_unified_base.steamworkssdk.proto",
        "citadel_usermessages.proto",
        "networkbasetypes.proto",
        "usermessages.proto",
        "demo.proto",
        "network_connection.proto",
        "gameevents.proto",
        "steammessages.proto",
        "valveextensions.proto",
        "usercmd.proto",
    ]:
        return
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        print(f"downloading {c.path} to {out}")
        f.write(r.content)


def download_folder(repo: Repository, folder: str, out: str, recursive: bool):
    contents = repo.get_contents(folder)
    for c in contents:
        if c.download_url is None:
            if recursive:
                download_folder(repo, c.path, out, recursive)
            continue
        download(c, out)


if __name__ == "__main__":
    g = Github()
    repo = g.get_repo(REPO)
    # download_folder(repo, "steam", 'protos', False)
    download_folder(repo, "deadlock", "protos", False)
