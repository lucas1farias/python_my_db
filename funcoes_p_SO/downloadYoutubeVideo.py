

from pytube import YouTube
from os import chdir, getlogin


class YoutubeDownloader:

    def __init__(self, where):
        self.where = where
        self.user = getlogin()
        self.prefix = f'C:/Users/'
        self.path = self.prefix + self.user + '/' + self.where
        chdir(self.path)
        self.input_for_link = input('Cole o link do vídeo youtube -> ')
        self.link_obj = YouTube(self.input_for_link).streams.get_highest_resolution()
        self.do_download()

    def do_download(self):
        try:
            self.link_obj.download()
        except:
            print("An error has occurred")
        print("Download is completed successfully")


if __name__ == '__main__':
    link = YoutubeDownloader(where='Downloads')
