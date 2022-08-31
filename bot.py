# import asyncio
import datetime
# import math
import os
# import queue
import time
# from json import loads

import discord
import requests
# import youtube_dl
from bs4 import BeautifulSoup
# from youtubesearchpython import SearchVideos

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# import json
import cv2
import numpy as np

import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# client_id = os.environ['CLIENT_ID']
# autho = os.environ['AUTHO']
# twitch_id = os.environ['TWITCH_ID']
kakao_key = os.environ['KAKAO_KEY']
chrome_bin = os.environ["CHROME_BIN"]
chrome_driver = os.environ['CHROME_DRIVER']
chrome_key_id = os.environ['CHROME_KEY_ID']
chrome_client_id = os.environ['CHROME_CLIENT_ID']

# Suppress noise about console usage from errors
# youtube_dl.utils.bug_reports_message = lambda: ''

# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
# }

# ffmpeg_options = {
#     'options': '-vn'
# }

# ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=1.0):
#         super().__init__(source, volume)

#         self.data = data

#         self.title = data.get('title')
#         self.url = data.get('url')

#     @classmethod
#     async def from_url(cls, url, *, loop=None, stream=False):
#         loop = loop or asyncio.get_event_loop()
#         data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

#         if 'entries' in data:
#             # take first item from a playlist
#             data = data['entries'][0]

#         filename = data['url'] if stream else ytdl.prepare_filename(data)
#         return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
 
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        # self.data = {}
        # super().__init__(intents=intents, *args, loop=None, **options)
        super().__init__(*args, **kwargs, intents=intents)

        # create the background task and run it in the background
        # self.bg_task = self.loop.create_task(self.background_task())
        # self.play_task = self.loop.create_task(self.play_queue())
        # self.search_infos = []
        # self.search_list = []
        # self.search_list_idx = 0
        # self.search_queue = queue.Queue()
        # self.search_guild = None
        # self.stop_count = -1
        self.activity_msg = ''
        self.activity_type = -1
    
    # async def play_queue(self):
    #     print('play_queue()')
    #     await self.wait_until_ready()

    #     # try:
    #     #     if os.path.isfile('music_list.txt'):
    #     #         print('file_load - start')
    #     #         with open('music_list.txt', 'r') as f:              # file을 열고 알아서 닫아 줌
    #     #             lines = []
    #     #             for count, line in enumerate(f):
    #     #                 data = line.strip('\n').split('\t')
    #     #                 info = YoutubeSearch(data[0], max_results=1).to_dict()
    #     #                 self.search_list.append([data[1], info[0]])
    #     #         print('file_load - end')
    #     # except Exception as e:
    #     #     print('file_load : [%s]' % e)
    #     #     channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
    #     #     await channelbot.send('file_load : [' + str(e) + ']')

    #     channel = discord.utils.get(self.get_all_channels(), name='봇명령어채팅')
    #     while True:
    #         try:
    #             if self.search_guild != None and self.search_guild.voice_client != None:
    #                 if not self.search_guild.voice_client.is_playing():
    #                     if self.stop_count != -1:
    #                         self.stop_count -= 1
    #                         if self.stop_count <= 0:
    #                             self.stop_count = -1
    #                             await self.search_guild.voice_client.disconnect()
    #                             self.search_guild = None
    #                             await channel.send(embed=discord.Embed(description='정지예약으로 재생을 정지합니다.'))
    #                             continue
    #                     if len(self.search_list) - 1 == self.search_list_idx:
    #                         self.search_list_idx = 0
    #                     else:
    #                         self.search_list_idx += 1
    #                     info = self.search_list[self.search_list_idx]
    #                     name = info[0]
    #                     result = info[1]
    #                     url = str(result['link'])
    #                     embed=discord.Embed(title=str(result['title']), url=url)
    #                     embed.set_author(name=str(result['channel']))
    #                     try:
    #                         embed.set_thumbnail(url=str(result['thumbnails'][2]))
    #                     except Exception as e:
    #                         embed.set_thumbnail(url=str(result['thumbnails'][0]))
    #                     embed.add_field(name='Channel', value=self.search_guild.voice_client.channel.name, inline=False)
    #                     embed.add_field(name='Duration', value=str(result['duration']), inline=True)
    #                     embed.add_field(name='Requested By', value=name, inline=True)
    #                     await channel.send(embed=embed)
                    
    #                     if str(result['duration']).count(':') == 2:
    #                         player = await YTDLSource.from_url(url, loop=self.loop, stream=True)
    #                     else:
    #                         player = await YTDLSource.from_url(url, loop=self.loop, stream=False)
    #                     self.search_guild.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else print('Player ok'))
    #                 else:
    #                     count = 0
    #                     for member in self.search_guild.voice_client.channel.members:
    #                         if member.bot == False:
    #                             count += 1
    #                     if count == 0:
    #                         await self.search_guild.voice_client.disconnect()
    #                         self.search_guild = None
    #                         self.stop_count = -1
    #                         await channel.send(embed=discord.Embed(description='체널에 사람이없어 재생을 정지합니다.'))    
    #         except Exception as e:
    #             print('play_queue : [%s]' % e)
    #             channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
    #             await channelbot.send('!play_queue Exception : [' + str(e) + ']')
    #         await asyncio.sleep(0.5)

    # async def background_task(self):
    #     print('background_task()')
    #     await self.wait_until_ready()
    #     channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
    #     channelwork = discord.utils.get(self.get_all_channels(), name='봇작업')
    #     nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     await channelbot.send('background_task() : [' + str(self.__hash__()) + '][' + nowDatetime + ']')

    #     name = 'Now N New Clan'
    #     twurl = '트위치:https://www.twitch.tv/' + twitch_id
    #     yturl = '유튜브:https://www.youtube.com/channel/UCvJ_CyjXl1XnUTSeinqW4gw/live'
    #     noticeChannel = discord.utils.get(self.get_all_channels(), name='서버메세지알림')
    #     freeChannel = discord.utils.get(self.get_all_channels(), name='자유채팅')
        
    #     live = False
    #     while True:
    #         try:            
    #             # nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             # await channelwork.send('while : [' + str(self.__hash__()) + '][' + nowDatetime + ']')

    #             #####################################################################################################################
    #             # headers = {'Client-ID': client_id, 'Authorization': 'Bearer '+autho}
    #             # res = requests.get('https://api.twitch.tv/helix/streams?user_login=' + twitch_id, headers=headers)
    #             # if res.text.find('type') != -1 and loads(res.text)['data'][0]['type'] == 'live':
    #             #     if live == False:
    #             #         live = True
    #             #         async with freeChannel.typing():
    #             #             # livemsg = name + ' 방송이 시작되었습니다.\n' + twurl + '\n' + yturl
    #             #             livemsg = name + ' 방송이 시작되었습니다.\n' + twurl
    #             #             await noticeChannel.send(embed=discord.Embed(description=livemsg))
    #             #             await freeChannel.send(embed=discord.Embed(description=livemsg))
    #             #             await self.changeActivity('Now N New Clan', twurl, discord.ActivityType.streaming, '방송중', 'twitch')
    #             #             await asyncio.sleep(10)
                            
    #             # elif live == True:
    #             #     async with freeChannel.typing():
    #             #         live = False
    #             #         livemsg = name + ' 방송이 종료되었습니다.'
    #             #         await noticeChannel.send(embed=discord.Embed(description=livemsg))
    #             #         await freeChannel.send(embed=discord.Embed(description=livemsg))
    #             #         await asyncio.sleep(10)
    #             #####################################################################################################################

    #             if live == False:
    #                 civil = await self.checkActivity('CIVIL WAR', '사용자 설정', "N&N Clan 내전", "내전 챔피언 선택", "내전 대기")
    #                 if civil == False:
    #                     scrim = await self.checkActivity('SCRIM MAGE', '사용자 설정', "N&N 스크림", "스크림 챔피언 선택", "스크림 대기")
    #                     if scrim == False:
    #                         crush = await self.checkActivity('CRUSH', '사용자 설정', "N&N Clan 격전", "격전 챔피언 선택", "격전 대기")
    #                         if crush == False:
    #                             music = await self.checkMusic()

    #             if live == False and civil == False and scrim == False and crush == False and music == False:
    #                     await self.changeActivity('', '', discord.ActivityType.playing, '', '')

    #         except Exception as e:
    #             print('bk_whlie Exception : [%s]' % e)
    #             channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
    #             await channelbot.send('!bk_whlie Exception : [' + str(e) + ']')
    #         await asyncio.sleep(0.5)
    #         nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #         await channelbot.send('bkClose() : [' + str(self.__hash__()) + '][' + nowDatetime + ']')

    async def checkActivity(self, ctgr,keyWord,act1,act2,act3):
        result = False
        try:
            # scrim = False
            Kategorie = discord.utils.get(self.get_all_channels(), name=ctgr)
            if Kategorie is None:
                return result
            for channel in Kategorie.channels:
                for member in channel.members:
                    if member.activity is None:
                        continue
                    if member.activity.name != 'League of Legends':
                        continue
                    if str(member.activity.details).find(keyWord) > -1:
                        if member.activity.state == '게임 중':
                            result_msg = act1
                        elif member.activity.state == '챔피언 선택 중':
                            result_msg = act2
                        # elif member.activity.state == '로비에서 대기 중':
                        #     game = discord.Game(act3)
                        else:
                            result_msg = act3
                        await self.changeActivity(result_msg, '', discord.ActivityType.playing, '', '')
                        result = True
                        break
            return result
        except Exception as e:
            # channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
            # await channelbot.send('Kategorie')
            print('checkActivity Exception : [%s]' % e)
            channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
            await channelbot.send('!checkActivity Exception : [' + str(e) + ']')
        return False

    # async def checkMusic(self):
    #     result = False
    #     if len(self.voice_clients) > 0:
    #         for voice_client in self.voice_clients:
    #             if voice_client.is_playing():
    #                 result = True
    #                 await self.changeActivity('MUSIC', '', discord.ActivityType.listening, '음악', '음악')
    #     return result

    async def changeActivity(self, name, url, discord_type, state, details):
        if self.activity_type != discord_type or self.activity_msg != name:
            self.activity_msg = name
            self.activity_type = discord_type
            if discord.ActivityType.listening == discord_type:    
                at = discord.Activity(name=name, type=discord_type, state=state, details=details)
            elif discord.ActivityType.streaming == discord_type:
                at = discord.Activity(name=name, url=url, type=discord_type, state=state, details=details)
            else:
                at = discord.Game(name)
            await self.change_presence(status=discord.Status.online, activity=at)
            
    async def parseOPGG(self, Name):
        hdr = {'Accept-Language': 'ko-KR,en;q=0.8', 'User-Agent': (
                'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36')}
        url = 'https://www.op.gg/summoners/kr/' + Name
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        rankTypes = []
        tiers = []
        points = []
        winLose = []
        name = soup.find("div", {"class":"name"}).text.replace('\n', '')
        for rankType in soup.find_all("div", {"class":"type"}):
            rankTypes.append(rankType.text.replace('\n', '').replace('\t', ''))
            tier = rankType.findNext('div').findNext('div').text.replace('\n', '').replace('\t', '')
            tiers.append(tier)
            if tier != 'Unranked':
                points.append(rankType.findNext('div').findNext('div').findNext('div').text.replace('\n', '').replace('\t', ''))
                win_lose = rankType.findNext('div').findNext('div').findNext('div').findNext('div').text.replace('\n', '').replace('\t', '')
                # lose = rankType.findNext('span').findNext('span').text.replace('\n', '').replace('\t', '')
                # ratio = rankType.findNext('span').findNext('span').findNext('span').text.replace('\n', '').replace('\t', '')
                # winLose.append('[' + win + ' ' + lose + ' (' + ratio + ')]')
                winLose.append(win_lose)
            else:
                points.append('None')
                winLose.append('None')
# <div class="winratio">14승 6 패 70%</div>
        rank = ''
        if tiers[0] != 'Unranked':
            rank = '솔랭 : ' + tiers[0] + ' ' + points[0] + ' ' + winLose[0]
        else:
            rank = '솔랭 : Unranked'

        subRank = ''
        if tiers[1] != 'Unranked':
            subRank = '자랭 : ' + tiers[1] + ' ' + points[1] + ' ' + winLose[1]
        else:
            subRank = '자랭 : Unranked'

        most = []
        title = soup.find("div", {"class":"winratio"})
        if not title is None:
            win_lose = title.findNext('span').text.replace('\n', '').replace('\t', '')
            # lose = title.findNext('span').findNext('span').text.replace('\n', '').replace('\t', '')
            # WinRatio = title.findNext('span').findNext('span').findNext('b').text.replace('\n', '').replace('\t', '')
            # ws = win + '승 ' + lose + '패 ' + '(' + WinRatio + ')'

            kda = title.findNext('span').findNext('span').findNext('b').findNext('span')
            kill = kda.text
            death = kda.findNext('span').text
            assist = kda.findNext('span').findNext('span').text
            KDARatio = kda.findNext('span').findNext('span').findNext('span').text
            CKRate = kda.findNext('span').findNext('span').findNext('span').findNext('span').findNext('span').text
            KDA = KDARatio + ' 평점' + ' (' + CKRate + ') - ' + kill + ' / ' + death + ' / ' + assist
            
            for cpName in soup.find_all("div", {"class":"ChampionName"}):
                title = cpName.get('title')
                kda = cpName.findNext('span').text
                game = cpName.findNext('span').findNext('div').findNext('div').findNext('div').findNext('div').text.replace('\n', '').replace('\t', '')
                rate = cpName.findNext('span').findNext('div').findNext('div').findNext('div').text.replace('\n', '').replace('\t', '')
                most.append(title + ' (' + kda + ')' + ' - ' + game + ' (' + rate + ')')
        else:
            win_lose = 'None'
            KDA = 'None'

        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")

        # driver = webdriver.Chrome(options=options)
        # url = 'https://www.op.gg/summoner/userName=' + Name

        # driver.get(url)
        # Container = {}

        # driver.find_element_by_css_selector('.SpectateTabButton').click()
        # time.sleep(5)

        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')

        # ingameInfo = soup.find("div", {"class" : "tabItem Content SummonerLayoutContent summonerLayout-spectator"})

        # names = ingameInfo.find_all("td", {"class" : "SummonerName Cell"})
        # Container['Names'] = []

        # now = ''
        # if len(names) != 0:
        #     now = '(현재 게임중)'

        msg = '===================================\n'
        msg += name + '\n'
        msg += '===================================\n'
        msg += rank + '\n'
        msg += subRank + '\n'
        # msg += '----------------------------------------------------------\n'
        # msg += '[최근전적]\n'
        # msg += win_lose + '\n'
        # msg += KDA + '\n'
        # msg += '----------------------------------------------------------\n'
        # msg += '[모스트 픽]\n'
        # if len(most) > 0:
        #     for item in most:
        #         msg += item + '\n'
        # else:
        #     msg += 'None\n'
        msg += '----------------------------------------------------------\n'
        
        return msg

    async def kakao_gameStart(self, appkey: str, result_url: str):
        """
        OCR api request example
        :param image_path: 이미지파일 경로
        :param appkey: 카카오 앱 REST API 키
        """
        API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

        headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

        url = result_url
        image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
        orgimage = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        height, width, channel = orgimage.shape
        if width != 1280:
            orgimage = cv2.resize(orgimage, (1280, 720))

        # orgimage = cv2.imread(image_path)
        # cutimage = orgimage[40:65, 110:189].copy() # 게임 시작
        # cutimage = orgimage[28:28+22, 81:81+69].copy() # 게임 시작
        cutimage = orgimage[28:28+26, 77:77+91].copy() # 게임 시작
        # cv2.imwrite("C:\\test\\test_.png", cutimage)
        jpeg_image = cv2.imencode(".jpg", cutimage)[1]
        data = jpeg_image.tobytes()
        return requests.post(API_URL, headers=headers, files={"image": data}).json()

    async def kakao_ocr_area(self, appkey: str, result_url: str, x: int, y: int, w: int, h: int):
        """
        OCR api request example
        :param image_path: 이미지파일 경로
        :param appkey: 카카오 앱 REST API 키
        """
        API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

        headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

        url = result_url
        image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
        orgimage = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        height, width, channel = orgimage.shape
        if width != 1280:
            orgimage = cv2.resize(orgimage, (1280, 720))

        # orgimage = cv2.imread(image_path)
        cutimage = orgimage[y:y+h, x:x+w].copy()
        # cv2.imwrite("C:\\test\\test_.png", cutimage)
        jpeg_image = cv2.imencode(".jpg", cutimage)[1]
        
        data = jpeg_image.tobytes()

        ocr_data = requests.post(API_URL, headers=headers, files={"image": data}).json()
        ocr_text = ""
        name = ""
        kda = ""
        cnt= 0
        for item in ocr_data['result']:
            text = item['recognition_words'][0] + ' '
            if text.find('/') == -1:
                name += text
            else:
                cnt += text.count('/')
                kda += text.replace('/',',')
            # if name != "" and kda != "":
            if cnt == 2 and name != "":
                ocr_text += name + ',' + kda + '\r\n'
                name = kda = ""
                cnt = 0
        print(ocr_text)
                
        
        # for index in range(0,10,2):
        #     name = ocr_data['result'][index]['recognition_words'][0]
        #     if name.find('/') != -1:
        #         name = name.replace('/',',')
        #         kda = ocr_data['result'][index+1]['recognition_words'][0]
        #         ocr_text += kda + ',' + name + '\r\n'
        #     else:
        #         kda = ocr_data['result'][index+1]['recognition_words'][0]
        #         kda = kda.replace('/',',')
        #         ocr_text += name + ',' + kda + '\r\n'
            
        # for index in range(13,23,2):
        #     name = ocr_data['result'][index]['recognition_words'][0]
        #     if name.find('/') != -1:
        #         name = name.replace('/',',')
        #         kda = ocr_data['result'][index+1]['recognition_words'][0]
        #         ocr_text += kda + ',' + name + '\r\n'
        #     else:
        #         kda = ocr_data['result'][index+1]['recognition_words'][0]
        #         kda = kda.replace('/',',')
        #         ocr_text += name + ',' + kda + '\r\n'

        return ocr_text.strip()
    
    async def champion_area(self, file_list: list, hists: list, appkey: str, result_url: str, x: int, y: int, w: int, h: int):
        """
        OCR api request example
        :param image_path: 이미지파일 경로
        :param appkey: 카카오 앱 REST API 키
        """
        API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

        headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

        url = result_url
        image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
        orgimage = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        height, width, channel = orgimage.shape
        if width != 1280:
            orgimage = cv2.resize(orgimage, (1280, 720))

        # orgimage = cv2.imread(image_path)
        cutimage = orgimage[y:y+h, x:x+w].copy()
        # cv2.imwrite("C:\\test\\test_.png", cutimage)
        # target_image = cv2.imread("C:\\test\\test.png")
        hsv = cv2.cvtColor(cutimage, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        query = hist
        
#         'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 
# #            'INTERSECT':cv2.HISTCMP_INTERSECT,
# #            'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}

        ret = 0.0
        for i, hist in enumerate(hists):
            cur_ret = cv2.compareHist(query, hist, cv2.HISTCMP_CORREL)
            # print(file_list[i] + "({})".format(cur_ret))
            if ret < cur_ret :
                ret = cur_ret
                name, ext = os.path.splitext(file_list[i])
                
        return name.strip()
    
    async def civilWarList(self, num):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        options.binary_location = chrome_bin
        driver = webdriver.Chrome(chrome_driver, chrome_options=options)
        driver.get('https://cafe.naver.com/ca-fe/home/search/combinations?q=제%20'+ num + '회%20N%26N%20공식내전')
        time.sleep(3)
        soup = bs(driver.page_source ,'html.parser')
        soup = soup.find(class_ = 'detail_area')
        soup = soup.find('a')
        newurl= soup['href']

        driver.get(newurl)
        time.sleep(1)
        driver.switch_to.frame('cafe_main') #iframe으로 접근

        soup = bs(driver.page_source ,'html.parser')
        names = soup.find_all(class_ = 'comment_nickname')
        coms = soup.find_all(class_ = 'text_comment')

        variables_keys = await self.create_keyfile_dict()
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        # credentials = ServiceAccountCredentials.from_json_keyfile_name('nnnocr-e0186b20172c.json', scope)
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(variables_keys, scope)
        gc = gspread.authorize(credentials).open("N&N 기록")
        wks = gc.worksheet('공식내전댓글')
        cell = wks.range('B6:X52')
        wks.batch_clear(["B6:X26", "B29:J52"])
        
        top_index = 0
        jg_index = 4
        mid_index = 8
        ad_index = 12
        sup_index = 16
        all_index = 20
        err_index = 529
        order_index = 0
        for index in range(0, len(coms)):
            data = coms[index].text.split('/')
            order_index = order_index + 1
            if data[0].strip() == '탑':
                cell[top_index+0].value = order_index
                cell[top_index+1].value = names[index].text.strip()
                cell[top_index+2].value = data[1].strip()
                top_index+=23
            elif data[0].strip() == '정글':
                cell[jg_index+0].value = order_index
                cell[jg_index+1].value = names[index].text.strip()
                cell[jg_index+2].value = data[1].strip()
                jg_index+=23
            elif data[0].strip() == '미드':
                cell[mid_index+0].value = order_index
                cell[mid_index+1].value = names[index].text.strip()
                cell[mid_index+2].value = data[1].strip()
                mid_index+=23
            elif data[0].strip() == '원딜':
                cell[ad_index+0].value = order_index
                cell[ad_index+1].value = names[index].text.strip()
                cell[ad_index+2].value = data[1].strip()
                ad_index+=23
            elif data[0].strip() == '서폿':
                cell[sup_index+0].value = order_index
                cell[sup_index+1].value = names[index].text.strip()
                cell[sup_index+2].value = data[1].strip()
                sup_index+=23
            elif data[0].strip() == '올':
                cell[all_index+0].value = order_index
                cell[all_index+1].value = names[index].text.strip()
                cell[all_index+2].value = data[1].strip()
                all_index+=23
            else :
                order_index = order_index - 1
                cell[err_index+0].value = str(order_index) + "-err"
                cell[err_index+1].value = names[index].text.strip()
                cell[err_index+2].value = coms[index].text
                err_index+=23
        wks.update_cells(cell)

    async def create_keyfile_dict(self):
        variables_keys = {
            "type": "service_account",
            "project_id": "nnnocr",
            "private_key_id": chrome_key_id,
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCBgSsYBJohsNyv\nyidNDvJgp0j89UBstGzhV5TtBrXpYKZNwl0FfWRO7JnynthsJq9NbZ1tug4l/Vbr\nq1SgFoxXirVTuRH7xf/CvzZHTZ5ApZCiS5q9O3tM9Wda/gfdxfxvpfO5amrShg3e\njEicqITtLHkqarqjivZQWdsrgEGzcQWll8aFguR+WoBJxVgejXNktF5cJZKO0vwb\nqaIp5QmWbV6H9EdMy73OGz2KkX/XO4AWdPqqQwQiJSb72DlOqdqq1Mk7F9Lumsyn\nk3/6MxXvSkcO6HaNSESaNuv74EWdqmu/nSqvNuzvTMAaNwXftsXbT/96Ih4L7v9q\nPmpgvHE9AgMBAAECggEABGJbEx+/bWSPaWQZRdfmXLSibpiJlc8wixsWmkT1OPFi\nBT/kkPWtxP49jU5+BStKGVTx/2+iYFGIn8ctFj5X10mFhKVp9nFoNy+XUX1PM4u8\nrxc1ezKIT2f/bRUshFWE4O1n/YmcvtkgSb3LYiz8/bUuZOviuvv5Wr8FVx5Vxb1W\nyjXiRXSFwva4FjSDkkr0AJv3ExjCf3O1tfovoBsLG4ADsg0tjSuFEdFGmqab0xHe\nVLVvyTIeSnmZc73DY+zV8HnQ1NBrw3aZcqVufHzk2cYG1OyGHP8TdwLaLVfCfIxs\n12Pd2c9DPEndrWpzvhyUE8mGHrTgtX0jccAhzrMIAQKBgQC2PLSti3N5dg9tSUVf\nPkB7b/Bi0bnKJxbuMiAFidmmNrwirLPMXhecGmz0OrWCCWzZN+P0/H9YQFsVLbQK\nQ/kG47xytlVJlgyHEXI2XObZU67bJQPPucZOVxCgtO+XDCD0tw+K4wFMxA7qwYd2\n7QC26G8BXpB0gJxo9gSVrKuu8wKBgQC17FkKvtCV3GRCvdCwtMdRsuxTpiHoErXr\nkFGUqx8EdwY/7P9LlaguURo829+NTXVCaw4Kwne7C1cnpoohTvjrePgv6E7HDTTI\nNkJjPTcowveozdBNHMFLGTCeVN7a/pXrhCnxS+1Z6brWWjWUHSK6mU877WB/u5Is\nHuPhwuRLDwKBgEbt8dTqRhOsY+zBbALaE/b3ZrTPtGR+OmqTj+sX8GLFQwyr839D\n0CSuFGIqx6LJUFhrbIpaDKaoxcrEcyLbuf14fkyXszJk+JNJsw59skw8Sf55tbYQ\nNKMhOBOU2PwNeHZHGgGQwVzDopq0oKklLfYDGdGKoOb3d+lSeA5ZmqkJAoGBAJOd\nAC8I34UJ/ExvantHZIe1L688GT0OmZBXXOrN4vAjh+2s5wW0nG9gnXKOUhl8pU3M\nQeuXGcGqlQB2UJRwWOfwEyoETI+U9qQR6tJNZIltkbjlr0QyteCywtFmOiHl+03L\nwqCpJCEV1uWA8wKIlZplNXaByRA76YJlWjDgi48fAoGAGK4b6ebIiblVrD5OrG63\nnS3tVjAJvhEzsrZ5cS4qc1PqeVzs3qo6bb4mTxaVppE+ed/cSgxRbPv56PPHncaT\nKBi/hpB1BTlouthYP+38EvVuyig000G68iUaNfxdxCzqhtOPg8vqmLkLRIfn9HrU\neJnQ/aURhjfOaT2O2Ix5Vfo=\n-----END PRIVATE KEY-----\n",
            "client_email": "nnn-record@nnnocr.iam.gserviceaccount.com",
            "client_id": chrome_client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/nnn-record%40nnnocr.iam.gserviceaccount.com"
        }
        return variables_keys
    
    async def civilwar_result(self, result_url: str):
        variables_keys = await self.create_keyfile_dict()
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        # credentials = ServiceAccountCredentials.from_json_keyfile_name('nnnocr-e0186b20172c.json', scope)
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(variables_keys, scope)
        gc = gspread.authorize(credentials).open("N&N 기록")
        # wks = gc.get_worksheet(7)
        wks = gc.worksheet('member')
        # wks2 = gc.get_worksheet(4)
        # cell_data = wks.acell('B2').value
        sheetPlayerList = wks.range('B2:B200')
        
        # if len(sys.argv) != 3:
        #     print("Please run with args: $ python example.py /path/to/image appkey")
        # image_path, appkey = sys.argv[1], sys.argv[2]
        appkey = kakao_key

        # resize_impath = kakao_ocr_resize(image_path)
        # if resize_impath is not None:
        #     image_path = resize_impath
        #     print("원본 대신 리사이즈된 이미지를 사용합니다.")
######################################################################################################################################################        
        # gameStart = await self.kakao_gameStart(appkey, result_url)
        # # print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2)))
        # # print(output['result'][0]['recognition_words'][0])
        # if gameStart['result'] == []:
        #     screenName = ""
        # else:
        #     screenName = gameStart['result'][0]['recognition_words'][0]
        # game_text = screenName.find('게임')
        # party_text = screenName.find('파티')
        # if game_text != -1 or party_text != -1:
        #     playerFirstX = 141
        #     playerFirstY = 252
        #     playerWidth = 187
        #     playerHeight = 44
        #     playerGapY = 36
        #     playerSecondY = 469
            
        #     championFirstX = 112
        #     championFirstY = 131
        #     championWidth = 22
        #     championHeight = 22
        #     championGapY = 35
        #     championSecondY = 350
            
        #     # championFirstX = 108
        #     # championFirstY = 127
        #     # championWidth = 30
        #     # championHeight = 30
        #     # championGapY = 35
        #     # championSecondY = 346
            
        #     kdaFirstX = 497
        #     kdaFirstY = 241
        #     kdaWidth = 168
        #     kdaHeight = 61
        #     kdaGapY = 35
        #     kdaSecondY = 456
        # else:
        #     playerFirstX = 139
        #     playerFirstY = 120
        #     playerWidth = 187
        #     playerHeight = 44
        #     playerGapY = 34
        #     playerSecondY = 339
            
        #     championFirstX = 112
        #     championFirstY = 131
        #     championWidth = 22
        #     championHeight = 22
        #     championGapY = 35
        #     championSecondY = 350
            
        #     kdaFirstX = 523
        #     kdaFirstY = 110
        #     kdaWidth = 154
        #     kdaHeight = 61
        #     kdaGapY = 34
        #     kdaSecondY = 329
        
        # player = []
        # for item in range(0,5):
        #     data = await self.kakao_ocr_area(appkey, result_url, playerFirstX, playerFirstY, playerWidth, playerHeight)
        #     player.append(data)
        #     playerFirstY += playerGapY

        # for item in range(5,10):
        #     data = await self.kakao_ocr_area(appkey, result_url, playerFirstX, playerSecondY, playerWidth, playerHeight)
        #     player.append(data)
        #     playerSecondY += playerGapY


        # champion_images = []
        # file_list = os.listdir(".\\champion")
        # for file in file_list:
        #     image = cv2.imread(".\\champion\\" + file, cv2.IMREAD_COLOR)
        #     champion_images.append(image)
        
        # hists = []
        # for i, image in enumerate(champion_images) :
        #     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #     hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
        #     cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        #     hists.append(hist)

        # champion = []
        # for item in range(0,5):
        #     data = await self.champion_area(file_list, hists, appkey, result_url, championFirstX, championFirstY, championWidth, championHeight)
        #     champion.append(data)
        #     championFirstY += championGapY

        # for item in range(5,10):
        #     data = await self.champion_area(file_list, hists, appkey, result_url, championFirstX, championSecondY, championWidth, championHeight)
        #     champion.append(data)
        #     championSecondY += championGapY
            
        # kda = []
        # for item in range(0,5):
        #     data = await self.kakao_ocr_area(appkey, result_url, kdaFirstX, kdaFirstY, kdaWidth, kdaHeight)
        #     kda.append(data)
        #     kdaFirstY += kdaGapY
        
        # for item in range(5,10):
        #     data = await self.kakao_ocr_area(appkey, result_url, kdaFirstX, kdaSecondY, kdaWidth, kdaHeight)
        #     kda.append(data)
        #     kdaSecondY += kdaGapY

        # kills = []
        # deaths = []
        # assists = []
        # for item in kda:
        #     data = item
        #     if data.count('/') == 2:
        #         temp = data.split('/')
        #         kills.append(temp[0].replace(" ",""))
        #         deaths.append(temp[1].replace(" ",""))
        #         assists.append(temp[2].replace(" ",""))
        #     else:
        #         temp = data
        #         for item in range(1, len(temp)):
        #             if temp[item] == ' ' or data[item] == '/':
        #                 kills.append(temp[0:item].replace(" ",""))
        #                 temp = temp[item+2:]
        #                 break
        #         for item in range(1, len(temp)):
        #             if temp[item] == ' ' or data[item] == '/':
        #                 deaths.append(temp[0:item].replace(" ",""))
        #                 temp = temp[item+2:]
        #                 break
        #         assists.append(temp.replace(" ",""))


        # for item in range(0,10):
        #     match = False
        #     for name in sheetPlayerList:
        #         if name.value == player[item]:
        #             match = True
        #             break
        #     if match == False:
        #         playerNameList = list(player[item])
        #         maxMatch = 0
        #         newName = player[item]
        #         playerNameIdx = len(playerNameList) - 1
        #         nameIdx = len(name.value) - 1
        #         for name in sheetPlayerList:
        #             curMatch = 0
        #             for idx in range(0,min(len(playerNameList),len(name.value))):
        #                 if playerNameList[playerNameIdx - idx] == name.value[nameIdx - idx]:
        #                     curMatch += 1
        #             if curMatch > maxMatch:
        #                 if curMatch == 1:
        #                     if len(playerNameList) == len(name.value):
        #                         maxMatch = curMatch
        #                         newName = name.value
        #                 else:
        #                     maxMatch = curMatch
        #                     newName = name.value
        #         player[item] = newName
######################################################################################################################################################

        win_team = await self.kakao_ocr_area(appkey, result_url, 141, 247, 519, 197)
        lose_team = await self.kakao_ocr_area(appkey, result_url, 141, 463, 519, 213)
        result = win_team + '\r\n' + lose_team
        # result = ""
        # for item in range(0,10):
        #     result += player[item] + "," + kills[item] + "," + deaths[item] + "," + assists[item] + '\r\n'
        return result

    async def on_ready(self):
        print('on_ready()')
        channelbot = discord.utils.get(self.get_all_channels(), name='봇로그')
        nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        await channelbot.send('on_ready() : [' + str(self.__hash__()) + '][' + nowDatetime + ']')

    async def on_voice_state_update(self, member, before, after):
        if after != None:
            if after.channel != None:
                if after.channel.category != None:
                    if after.channel.category.name == 'NNN Clan Game' or after.channel.category.name == 'ACQUAINTANCE':
                        if after.channel.name == '음성채널 만들기' or after.channel.name == '지인채널 만들기':
                            chNewName = member.nick[5:] + '의 게임'
                            chName = after.channel.name[:4]
                            chNew = await after.channel.clone(name=chNewName, reason=None)
                            # chNew.rtc_region = discord.VoiceRegion.south_korea
                            # chNew.user_limit = 50
                            overwrite = discord.PermissionOverwrite()
                            overwrite.manage_channels = True
                            await chNew.set_permissions(member, overwrite=overwrite)
                            await chNew.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                            await member.move_to(chNew)
                            chFree = discord.utils.get(member.guild.text_channels, name='자유채팅')
                            await chFree.send(embed=discord.Embed(description=member.nick + '님께서 '+  chName + '을 생성하였습니다.'))
                    elif after.channel.category.name == 'CIVIL WAR':
                        if after.channel.name == '내전채널 만들기':
                            if len(after.channel.category.voice_channels) < 2:
                                ch_wait = await after.channel.clone(name='내전 대기방', reason=None)
                                await ch_wait.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch1 = await after.channel.clone(name='내전 1팀', reason=None)
                                await ch1.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch2 = await after.channel.clone(name='내전 2팀', reason=None)
                                await ch2.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch3 = await after.channel.clone(name='내전 3팀', reason=None)
                                await ch3.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch4 = await after.channel.clone(name='내전 4팀', reason=None)
                                await ch4.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch5 = await after.channel.clone(name='내전 5팀', reason=None)
                                await ch5.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                ch6 = await after.channel.clone(name='내전 6팀', reason=None)
                                await ch6.edit(reason=None, rtc_region=discord.VoiceRegion.south_korea)
                                await member.move_to(ch_wait)
                                chFree = discord.utils.get(member.guild.text_channels, name='자유채팅')
                                await chFree.send(embed=discord.Embed(description=member.nick + '님께서 내전채널을 생성하였습니다.'))
        if before != None:
            if before.channel != None:
                if before.channel.category != None:
                    if before.channel.category.name == 'NNN Clan Game' or before.channel.category.name == 'ACQUAINTANCE':
                        if len(before.channel.members) == 0:
                            if before.channel.name != '음성채널 만들기' and before.channel.name != '지인채널 만들기':
                                await before.channel.delete(reason=None)
                    elif before.channel.category.name == 'CIVIL WAR':
                        cnt = 0
                        for i in range(0, len(before.channel.category.voice_channels)):
                            cnt += len(before.channel.category.voice_channels[i].members)
                        if cnt == 0:
                            overwrite = discord.PermissionOverwrite()
                            overwrite.manage_channels = True
                            for j in reversed(range(len(before.channel.category.voice_channels))):
                                chDel = before.channel.category.voice_channels[j]
                                if chDel.name != '내전채널 만들기':
                                    await chDel.set_permissions(member, overwrite=overwrite)
                                    await chDel.delete(reason=None)

    async def on_message(self, message):
        if message.author == self.user:
            return
        # if len(self.search_infos) > 0:
        #     for idx, search_info in enumerate(self.search_infos):
        #         if message.author == search_info[0]:
        #             try:
        #                 sel = int(message.content)-1
        #                 result = search_info[1]['search_result']
        #                 if sel > -1 and sel < len(result):
        #                     await self.stream(message, result[sel])
        #                 else:
        #                     await message.channel.send(embed=discord.Embed(description='Prompt cancelled.'))    
        #             except:
        #                 await message.channel.send(embed=discord.Embed(description='Prompt cancelled.'))
        #             finally:
        #                 del self.search_infos[idx]
        #                 return

        if message.channel.type.value == 1:
            async with message.channel.typing():
                if message.content.startswith('!cw '):
                    num = message.content[4:]
                    # msg = await self.printSummonerInfo(await self.parseOPGG(name))
                    await self.civilWarList(num)
                    await message.channel.send(embed=discord.Embed(description="스프레드 시트를 확인해주세요."))
            return
        elif message.content.startswith('!lol '):
            async with message.channel.typing():
                name = message.content[5:]
                # msg = await self.printSummonerInfo(await self.parseOPGG(name))
                msg = await self.parseOPGG(name)
                await message.channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!clear_bot123'):
            async with message.channel.typing():
                self.clear()
                await message.channel.send('!clear_bot123')
        elif message.content.startswith('!intro '):
            async with message.channel.typing():
                msg = message.content[7:]
                channel = discord.utils.get(message.guild.text_channels, name='안내')
                await channel.send(msg)
        elif message.content.startswith('!emintro '):
            async with message.channel.typing():
                msg = message.content[9:]
                channel = discord.utils.get(message.guild.text_channels, name='안내')
                await channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!guide '):
            async with message.channel.typing():
                msg = message.content[7:]
                channel = discord.utils.get(message.guild.text_channels, name='가이드')
                await channel.send(msg)
        elif message.content.startswith('!emguide '):
            async with message.channel.typing():
                msg = message.content[9:]
                channel = discord.utils.get(message.guild.text_channels, name='가이드')
                await channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!free '):
            async with message.channel.typing():
                msg = message.content[6:]
                channel = discord.utils.get(message.guild.text_channels, name='자유채팅')
                await channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!link '):
            async with message.channel.typing():
                msg = message.content[6:]
                channel = discord.utils.get(message.guild.text_channels, name='클랜링크')
                await channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!msg '):
            async with message.channel.typing():
                msg = message.content[5:]
                await message.channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!notice '):
            async with message.channel.typing():
                msg = message.content[8:]
                channel = discord.utils.get(message.guild.text_channels, name='자유채팅')
                await channel.send(embed=discord.Embed(description=msg))
                channel = discord.utils.get(message.guild.text_channels, name='서버메세지알림')
                await channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!ping'):
            async with message.channel.typing():
                msg = '현재 핑은 ' + str(format(self.latency,".2")) + '입니다.'
                await message.channel.send(embed=discord.Embed(description=msg))
        elif message.content.startswith('!off'):
            await self.changeActivity('', '', discord.ActivityType.playing, '', '')
        elif message.content.startswith('!out_bot123'):
            async with message.channel.typing():
                channel = message.channel
                await channel.send('bye')
                await self.logout()
                await self.close()
        elif message.channel.name == '경기결과':
            if message.attachments != []:
                async with message.channel.typing():
                    result_url = message.attachments[0].proxy_url + "?width=1280&height=720"
                    try :
                        msg = await self.civilwar_result(result_url)
                        await message.reply(content=msg)
                    except :
                        await message.reply(content="인식오류\r\n업로드방법:https://cafe.naver.com/nownnew3333/2833")
        # elif message.content.startswith('!c '):
        #     # msg = message.content[2:]
        #     msg = '5'
        #     if int(msg) > 1:
        #         channel = message.channel
        #         await channel.send('(1/'+msg+')' + '...')

        #         def check(m):
        #             return m.channel == channel
        #         for i in range(2, int(msg)+1):
        #             try:
        #                 msg = await client.wait_for('message', timeout=1.0, check=check)
        #                 break
        #             except:
        #                 await channel.send('('+str(i)+'/'+msg+')' + '...')
        # elif message.content.startswith('!play'):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             msg = message.content[5:]
        #             async with message.channel.typing():
        #                 if len(msg) > 0:
        #                     await self.search(message, str(msg), True)
        #                 else:
        #                     await self.play(message)
        # elif message.content.startswith('!search '):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             msg = message.content[8:]
        #             await self.search(message, str(msg), False)

        # elif message.content.startswith('!stop'):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             if message.guild.voice_client is None:
        #                 await message.channel.send(embed=discord.Embed(description='현재 재생중이지 않습니다.'))
        #             else:
        #                 idx = message.content[5:]
        #                 if not idx.strip():
        #                     self.search_guild = None
        #                     self.stop_count = -1
        #                     await message.guild.voice_client.disconnect()
        #                     await message.channel.send(embed=discord.Embed(description='재생을 정지합니다.'))
        #                 else:
        #                     self.stop_count = int(idx)
        #                     await message.channel.send(embed=discord.Embed(description='1곡 재생 후 정지합니다.'))
        # elif message.content.startswith('!volume '):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             if message.channel == channel:
        #                 data = message.content.split(" ")
        #                 await self.volume(message, int(data[1]))
        # elif message.content.startswith('!queue'):
        #     async with message.channel.typing():
        #         try:
        #             if await self.check_music_msg(message) == True:
        #                 list_len = len(self.search_list)
        #                 max_page = math.ceil(list_len / 10)
        #                 page = message.content[6:]
        #                 if not page.strip():
        #                     sel_page = max_page
        #                 else:
        #                     sel_page = int(page)
        #                 if sel_page < 1:
        #                     sel_page = 1
        #                 elif sel_page > max_page:
        #                     sel_page = max_page
        #                 min_idx = (sel_page - 1) * 10
        #                 max_idx = sel_page * 10
        #                 msg = 'Queue page ' + str(sel_page) + '/' + str(max_page) + '\n\n'
        #                 for idx, search_list in enumerate(self.search_list):
        #                     if min_idx <= idx and max_idx > idx:
        #                         if self.search_list_idx == idx:
        #                             msg += '->'
        #                         msg += str(idx+1) + ') ' + search_list[1]['title'] + ' - ' + search_list[0] + '\n'
        #                 await message.channel.send(embed=discord.Embed(description=msg))
        #         except Exception as e:
        #             channelbot = discord.utils.get(self.get_all_channels(), guild__name=message.guild.name, name='봇로그')
        #             await channelbot.send('!queue : [' + str(e) + ']')
        # elif message.content.startswith('!skip'):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             message.guild.voice_client.stop()
        #             await message.channel.send(embed=discord.Embed(description='skipping...'))
        # elif message.content.startswith('!back'):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             idx = self.search_list_idx - 2
        #             if idx < -1:
        #                 self.search_list_idx = len(self.search_list) - 2
        #             else:
        #                 self.search_list_idx = idx
        #             message.guild.voice_client.stop()
        #             await message.channel.send(embed=discord.Embed(description='back...'))
        # elif message.content.startswith('!jump '):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             msg = message.content[6:]
        #             if len(self.search_list) + 1 > int(msg):
        #                 self.search_list_idx = int(msg) - 2
        #                 message.guild.voice_client.stop()
        #                 await message.channel.send(embed=discord.Embed(description='jumping...'))
        #             else:
        #                 await message.channel.send(embed=discord.Embed(description='잘못 입력하셨습니다.'))
        # elif message.content.startswith('!delete '):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             await self.list_del(message)
        # elif message.content.startswith('!clear'):
        #     async with message.channel.typing():
        #         if await self.check_music_msg(message) == True:
        #             await self.list_clear(message)
 
    # async def check_music_msg(self, message):
    #     channel = discord.utils.get(message.guild.text_channels, name='봇명령어채팅')
    #     if message.channel == channel:
    #         return True
    #     else:
    #         await message.channel.send(embed=discord.Embed(description='Music관련 명령어는 \'봇명령어채팅\'채널을 이용해주세요.'))
    #         return False
        
    # async def search(self, message, terms, dirt):

    #     search = SearchVideos(terms, offset = 1, mode = "json", max_results = 5)
    #     json_data = loads(search.result())

    #     if dirt == False:
    #         lst = ''
    #         for idx, author in enumerate(json_data['search_result']):
    #             lst += str(int(author['index'])+1) + ' : ' + str(author['title']) + '\n' # + ' (' + str(result['duration']) + ')\n'
    #         # for idx, info in enumerate(infos):
    #         #     lst += str(idx+1) + ' : ' + str(info['title']) + '\n' # + ' (' + str(result['duration']) + ')\n'
    #         lst += '\nSay the number of the track you wish to play (e.g \'1\') or say \'cancel\' to cancel.'
    #         await message.channel.send(embed=discord.Embed(description=lst))
    #         def check(m):
    #             return m.author == message.author and m.channel == message.channel
    #         try:
    #             self.search_infos.append([message.author, json_data])
    #             msg = await client.wait_for('message', timeout=30.0, check=check)
    #         except:
    #             await message.channel.send(embed=discord.Embed(description='30 초 동안 응답이 없습니다.'))
    #             for idx, search_info in enumerate(json_data):
    #                 if message.author == search_info[0]:
    #                     del self.search_infos[idx]
    #     else:
    #         await self.stream(message, json_data['search_result'][0])

    # async def stream(self, message, info):
    #     try:
    #         if message.guild.voice_client is None:
    #             if message.author.voice:
    #                 await message.author.voice.channel.connect()
    #             else:
    #                 await message.channel.send(embed=discord.Embed(description='먼저 음성체널에 접속해주세요.'))
    #                 # for idx, search_info in enumerate(self.search_infos):
    #                 #     if message.author == search_info[0]:
    #                 #         del self.search_infos[idx]
    #                 return
    #         # self.search_queue.put_nowait([message, result])
    #         await self.list_add(message.author.display_name, info)
            
    #         if message.guild.voice_client.is_playing():
    #             # await message.guild.voice_client.stop()
    #             # await message.guild.voice_client.disconnect()
    #             # await message.author.voice.channel.connect()
    #             # await message.guild.voice_client.move_to(message.author.voice.channel)
    #             # await message.channel.send(embed=discord.Embed(description='Please stop the music first, the music is playing. (ex. !stop)'))
    #             msg = str('"' + info['title']) + '" 플레이리스트에 추가되었습니다.'
    #             await message.channel.send(embed=discord.Embed(description=msg))
    #         else:
    #             self.search_list_idx = len(self.search_list) - 2
    #             if self.search_guild is None:
    #                 self.search_guild = message.guild
                
    #     except Exception as e:
    #         print('stream Exception: [%s]' % e)
    #         channelbot = discord.utils.get(self.get_all_channels(), guild__name=message.guild.name,name='봇로그')
    #         await channelbot.send('!stream Exception : [' + str(e) + ']')

    # async def list_add(self, name, info):
    #     self.search_list.append([name, info])
    #     with open("music_list.txt", "a", encoding='UTF-8') as f:
    #         f.write(info['title'] + '\t' + name + '\n')

    # async def list_del(self, message):
    #     msg = message.content[8:]
    #     idx = int(msg) - 1
    #     if self.search_list_idx == idx and message.guild.voice_client.is_playing():
    #         await message.channel.send(embed=discord.Embed(description='현재 곡은 삭제할 수 없습니다.'))
    #     elif len(self.search_list) > idx and 0 <= idx:
    #         del self.search_list[idx]
    #         with open('music_list.txt', 'r+', encoding='UTF-8') as f:              # file을 열고 알아서 닫아 줌
    #             lines = []
    #             for count, line in enumerate(f):
    #                 if(count == idx):      # 'old_term:'으로 시작하는 line을 찾음
    #                     pass
    #                 else:
    #                     lines = lines + [line]
    #             f.seek(0)                                      # file pointer 위치를 처음으로 돌림
    #             f.writelines(lines)                            # 수정한 lines를 파일에 다시 씀
    #             f.truncate()                                   # 현재 file pointer 위치까지만 남기고 나머지는 정리 
    #         if self.search_list_idx > idx:
    #             self.search_list_idx -= 1
    #         await message.channel.send(embed=discord.Embed(description='delete...'))
    #     else:
    #         await message.channel.send(embed=discord.Embed(description='잘못 입력하셨습니다.'))

    # async def list_clear(self, message):
    #     if not self.search_guild is None:
    #         if not self.search_guild.voice_client is None:
    #             if self.search_guild.voice_client.is_playing():
    #                 result = self.search_list[self.search_list_idx]
    #     self.search_list.clear()
    #     if os.path.isfile('music_list.txt'):
    #         os.remove('music_list.txt')
    #     if not self.search_guild is None:
    #         if not self.search_guild.voice_client is None:
    #             if self.search_guild.voice_client.is_playing():
    #                 await self.list_add(result[0], result[1])
    #     self.search_list_idx = 0
    #     await message.channel.send(embed=discord.Embed(description='clear...'))

    # async def play(self, message):
    #     try:
    #         if message.guild.voice_client is None:
    #             if message.author.voice:
    #                 self.search_list_idx -= 1
    #                 if self.search_list_idx < 0:
    #                     self.search_list_idx = len(self.search_list) - 1
    #                 self.search_guild = message.guild
    #                 await message.author.voice.channel.connect()
    #             else:
    #                 await message.channel.send(embed=discord.Embed(description='먼저 음성체널에 접속해주세요.'))
    #                 return
    #         else:
    #             if self.search_guild.voice_client.is_playing():
    #                 self.search_list_idx -= 1
    #                 if self.search_list_idx < 0:
    #                     self.search_list_idx = len(self.search_list) - 1
    #                 await message.guild.voice_client.stop()
    #     except:
    #         pass

    # async def volume(self, message, volume: int):
    #     if not message.guild.voice_client is None:
    #         message.guild.voice_client.source.volume = volume / 100

    # @play.before_invoke
    # @yt.before_invoke
    # @stream.before_invoke
    # async def ensure_voice(self, message, url):
    #     if message.guild.voice_client is None:
    #         if message.author.voice:
    #             await message.author.voice.channel.connect()
    #         else:
    #             await message.channel.send("You are not connected to a voice channel.")
    #             raise commands.CommandError("Author not connected to a voice channel.")
    #     elif message.guild.voice_client.is_playing():
    #         message.guild.voice_client.stop()

    async def on_member_join(self, member):
        channel = discord.utils.get(self.get_all_channels(), guild__name=member.guild.name, name='서버접속알림')
        msg = member.mention + '님 서버에 들어왔습니다.'
        await channel.send(msg)

    async def on_member_remove(self, member):
        nick = member.nick
        name = member.name
        if nick is None:
            nick = 'None'
        if name is None:
            name = 'None'
        channel = discord.utils.get(self.get_all_channels(), guild__name=member.guild.name, name='서버접속알림')
        msg = nick + '(' + name + ')' + ' 님이 나갔습니다.'
        await channel.send(msg)

access_token = os.environ['BOT_TOKEN']
client = MyClient()
client.run(access_token)
