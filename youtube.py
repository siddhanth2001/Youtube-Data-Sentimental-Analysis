import requests
import os

def get_video_details(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={os.getenv('API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            video_data = data['items'][0]
            title = video_data['snippet']['title']
            channel = video_data['snippet']['channelTitle']
            views = video_data['statistics']['viewCount']
            published_at = video_data['snippet']['publishedAt']
            return {
                'title': title,
                'channel': channel,
                'views': views,
                'published_at': published_at
            }
    else:
        print(f"Failed to fetch video details: {response.status_code}, {response.text}")
        raise Exception(f"Failed to fetch video details: {response.status_code}, {response.text}")

def get_video_comments(video_id, max_results=10):
    video_details = get_video_details(video_id)
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={os.getenv('API_KEY')}&maxResults={max_results}"
    response = requests.get(url)
    comments = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            snippet = item['snippet']['topLevelComment']['snippet']
            comment = snippet['textOriginal']
            author = snippet['authorDisplayName']
            like_count = snippet['likeCount']
            published_at = snippet['publishedAt']
            comments.append({
                'comment': comment,
                'author': author,
                'like_count': like_count,
                'published_at': published_at
            })
    else:
        print(f"Failed to fetch comments: {response.status_code}, {response.text}")
        raise Exception(f"Failed to fetch comments: {response.status_code}, {response.text}")
    
    return video_details, comments