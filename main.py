from time import sleep
from pytube import Playlist
import os
from pytube import YouTube


def download_video(video_url):
    video = YouTube(video_url)
    if not os.path.exists(f'/home/{os.environ.get("USER")}/Education/videos/{video.author}'):
        os.makedirs(f'/home/{os.environ.get("USER")}/Education/{video.author}')
    video.streams.get_highest_resolution().download(f'/home/{os.environ.get("USER")}/Education/{video.author}')


def download_playlist(playlist_url):
    p = Playlist(playlist_url)
    if not os.path.exists(f'/home/{os.environ.get("USER")}/Education/{p.owner}/{p.title}'):
        os.makedirs(f'/home/{os.environ.get("USER")}/Education/{p.owner}/{p.title}')

    for video in p.videos:
        try:
            print(f'Downloading: {video.title}')
            video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(
                f'/home/{os.environ.get("USER")}/Education/{p.owner}/{p.title}', skip_existing=True)
        except Exception:
            sleep(5)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'FAILED!')
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Continue downloading!')
            video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(
                f'/home/{os.environ.get("USER")}/Education/{p.owner}/{p.title}', skip_existing=True)
        print('FINISHED!')
        print('____________________________________________________________________________________________')


def main():
    url = input('Введите ссылку/Enter url: ')
    if url.__contains__('playlist'):
        download_playlist(url)
    else:
        download_video(url)


if __name__ == '__main__':
    main()
    print("DONE!")
