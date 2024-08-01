import yt_dlp
import re
from datetime import timedelta


def format_size(bytes_size):
    """Convert a file size in bytes to a human-readable string."""
    if bytes_size is None:
        return None
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"


def sanitize_filename(filename):
    """Sanitize the filename by removing or replacing invalid characters."""
    return re.sub(r'[<>:"/\\|?*]', "", filename)


def format_duration(seconds):
    """Convert a duration in seconds to a human-readable format."""
    return str(timedelta(seconds=int(seconds)))


# Define options
ydl_opts = {
    "format": "all",  # Get information about all formats
    "noplaylist": True,  # Ensure we're only processing a single video
    "quiet": True,  # Suppress verbose output
}


# Major video resolutions we are interested in
major_resolutions = ["240p", "360p", "480p", "720p", "1080p", "2160p"]


def yt_fetchData(video_url):

    # Create a YoutubeDL object with the specified options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video information
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get("title")
        video_id = info_dict.get("id")
        thumbnail_url = info_dict.get("thumbnail")
        duration_seconds = info_dict.get("duration")
        duration_readable = format_duration(duration_seconds)

        # Prepare format information
        formats_info = {"audio": [], "video": [], "video_with_audio": []}

        for format in info_dict["formats"]:
            ext = format.get("ext")
            if ext == "webm":
                continue  # Skip WebM formats

            has_audio = format.get("acodec") != "none"
            has_video = format.get("vcodec") != "none"
            resolution = format.get(
                "format_note"
            )  # Use 'format_note' to get resolution info

            format_info = {
                "ext": ext,
                "filesize": format.get("filesize"),
                "human_readable_size": format_size(format.get("filesize")),
                "download_url": format.get("url"),
                "resolution": resolution,
            }

            # Include only formats with known filesize
            if format_info["filesize"] is not None:
                if has_audio and has_video:
                    formats_info["video_with_audio"].append(format_info)
                elif has_audio and not has_video:
                    if not formats_info["audio"]:  # Include only the first audio format
                        formats_info["audio"].append(format_info)
                elif has_video and resolution in major_resolutions:
                    formats_info["video"].append(format_info)

        # Create the final data structure
        video_info = {
            "video_id": video_id,
            "video_title": video_title,
            "thumbnail": thumbnail_url,
            "duration": {
                "seconds": duration_seconds,
                "human_readable": duration_readable,
            },
            "formats": formats_info,
        }

        # Write the video info to a JSON file
        return video_info
