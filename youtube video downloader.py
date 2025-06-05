import yt_dlp

def download_video(url, output_path='.'):
    ydl_opts = {
        'format': 'best',               # highest quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # save with video title
        'noplaylist': True              # avoid downloading playlist if URL is playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download completed!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    path = input("Enter folder path to save (default current folder): ").strip()
    if not path:
        path = '.'

    download_video(video_url, path)
