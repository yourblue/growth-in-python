import re
import urllib.request
import urllib.error
import urllib.parse
import json


def get_all_hot_songs():
    """获取所有的热门歌曲"""
    url = 'http://music.163.com/discover/toplist?id=3779629'
    html = urllib.request.urlopen(url).read().decode('utf8')
    html = str(html)
    pat1 = r''
    result = re.compile(pat1).findall(html)
    result = result[0]

    pat2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'
    pat3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'
    hot_songs_name = re.compile(pat2).findall(result)
    hot_songs_id = re.compile(pat3).findall(result)

    return hot_songs_name, hot_songs_id


def get_hot_comments(hot_songs_name, hot_songs_id):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_songs_id + '?csrf_token='
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
    data = {
        "params": "VpOqhdfuS4gtSPH1ViZORhaXQuNRQe37GpUG4mPVHbYYt1g/K1eak6VBTA5dLqVWG5ahb475QjJzUqy9TmYHi2sGUVevSslkwHrV9iApB0iOOC/kOaMoY7urxTVH4Lf/WfItnONkogLXl8mEcdjDWKGuyMmf5DSPjb6zI62Yv3J+eziPzjjqVjK2woqvncXv",
        "encSecKey": "06b00562f94190674ff7e46cfae57c2440d353dce0d174879155ffcd0a8954bafe8486c6e09084004c2c036caaf4290cdb0c6ae41844f73e608ac9a6b19c07b2d919a4024d4883dad803bb2697077f4164c20b4ecf5e6df1e03742bec2bc09ff8e219cb4ac1592a7b636686a8a20ffb74950de2647d1f9506670157ed19c2f6e"}
    postdata = urllib.parse.urlencode(data).encode('utf8')
    request = urllib.request.Request(url, headers=header, data=postdata)
    response = urllib.request.urlopen(request).read().decode('utf8')
    json_dict = json.loads(response)
    hot_commit = json_dict['hotComments']

    num = 0
    fhandle = open('./song_comments.txt', 'a', encoding='utf8')
    fhandle.write(hot_songs_name + ':' + '\n')

    for item in hot_commit:
        num += 1
        fhandle.write(str(num) + '.' + item['content'] + '\n')
    fhandle.write('\n**************************************\n\n')
    fhandle.close()


if __name__ == '__main__':

    hot_songs_name, hot_songs_id = get_all_hot_songs()
    num = 0
    while num < len(hot_songs_name):
        print("正在抓取第%d首歌曲热评..." % (num + 1))
        get_hot_comments(hot_songs_name[num], hot_songs_id[num])
        print("第%d首歌曲热评抓取成功" % (num + 1))
        num += 1
