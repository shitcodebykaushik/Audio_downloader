import yt_dlp

def download_youtube_audio_no_ffmpeg():
    print("Welcome to YouTube Audio Downloader!")
    print("Paste the YouTube video URL below to download the audio:\n")

    url = input("Enter the YouTube video URL: ")
    try:
        # Configure yt-dlp options to download audio only
        ydl_opts = {
            'format': 'bestaudio/best',  # Select the best audio format available
            'outtmpl': '%(title)s.%(ext)s',  # Save the audio file with the video title
        }

        # Initialize yt-dlp with the options and download the audio
        print("\nDownloading audio, please wait...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nAudio download completed! Check your folder for the file.")
    except Exception as e:
        print(f"An error occurred: {e}\nPlease check the URL and try again.")

if __name__ == "__main__":
    download_youtube_audio_no_ffmpeg()
