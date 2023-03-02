from pytube import YouTube


def download(url):
    youtubeObj = YouTube(url)
    youtubeObj = youtubeObj.streams.get_highest_resolution()

    try:
        youtubeObj.download()
    except:
        print('Erro ao fazer o download')

    print('Download concluido!!!')


url = "URL DO VIDEO"
download(url)
