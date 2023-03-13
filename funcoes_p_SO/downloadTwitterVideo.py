

from twitter.src.twitter_video_dl.twitter_video_dl import download_video
from os import chdir, getlogin


class Twitter:
    def __init__(self, where):
        self.where = where
        self.user = getlogin()
        self.prefix = f'C:/Users/'
        self.path = self.prefix + self.user + '/' + self.where
        chdir(self.path)
        self.input_for_link = input('Cole o link do vídeo twitter -> ')
        self.title = input('Nome do título do vídeo -> ')
        self.format = input('Formato do vídeo -> ')
        download_video(video_url=self.input_for_link, file_name=self.title + self.format)
        print('\nSTATUS: Download concluído\n')


midia = Twitter(where='Downloads')
