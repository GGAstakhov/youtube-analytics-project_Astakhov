from src.mixinapi import MixinAPI


class Video(MixinAPI):
    def __init__(self, video_id):
        self.__video_id = video_id
        self.video = self.get_service().channels().list(
            id=video_id, part='snippet,statistics'
        ).execute()
        self.id = self.video['items'][0]['id']
        self.title_video = self.video['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.__video_id}'
        self.video_count = int(self.video['items'][0]['statistics']['viewCount'])
        self.video_likes = int(self.video['items'][0]['statistics']['likeCount'])
