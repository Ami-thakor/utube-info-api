import instaloader, os
from instaloader import Post

# Get instance
L = instaloader.Instaloader()

# channie12@dependity.com
# vishalxverna
# UserName = "vishalxverna"
UserName = os.environ.get('username',
                           'user')
PassWord = os.environ.get('password',
                           'pass')

# PassWord = "Vishal@143"

# L.login(user=UserName, passwd=PassWord)
# L.save_session_to_file("mysession.session")
# L.load_session_from_file(username, "mysession.session")
L.load_session_from_file("vishalxverna", "mysession.session")

def get_video_info(link: str):
    ShortCode = link.split("/")[4]
    post = Post.from_shortcode(L.context, ShortCode)
    media_type = post.typename
    post_info = {
        "source_url": link,
        "owner_id": post.owner_username,
        "media_type": 1,
        "caption": post.caption,
        "download_links": [],
    }

    if media_type == "GraphImage":
        post_info["download_links"] = [{"thumb": post.url}]

    elif media_type == "GraphVideo":
        post_info["download_links"] = [{"thumb": post.url, "video_url": post.video_url}]
        post_info["media_type"] = 2

    elif media_type == "GraphSidecar":
        Posts = post.get_sidecar_nodes()
        # Collecting data for each post in GraphSidecar
        post_info["download_links"] = [
            {"is_video": p.is_video, "thumb": p.display_url, "video_url": p.video_url}
            for p in Posts
        ]
        post_info["media_type"] = 3
    else:
        return {"error": "something went wrong."}

    return post_info


# reel = "https://www.instagram.com/reel/C5MBjNbsqr3/?igsh=MWZ6ejZham5ienkwaQ=="
# carousel = "https://www.instagram.com/p/C9hMqN3SVFE"
# post = "https://www.instagram.com/p/CxLX1oGRKaP/?igsh=MXg0cmw2Z3RmcHl1bg=="
# data = get_video_info(post)
# print(data)
