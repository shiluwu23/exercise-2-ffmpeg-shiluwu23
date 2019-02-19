import asyncio
import queue
import os


async def video720(que):
    video = que.get()
    os.system("./ffmpeg -i ./video_in/" + video + " -b: 2M -r 30 -s 1280x720 -f mp4 -loglevel quiet " + video + "_720p.mp4")
    print('Convert ' + video + ' to 720p' + ' successfully!')
    return'720 done'


async def video480(que):
    video = que.get()
    os.system("./ffmpeg -i ./video_in/" + video + " -b: 2M -r 30 -s 640x480 -f mp4 -loglevel quiet " + video + "_480p.mp4")
    print('Convert ' + video + ' to 480p' + ' successfully!')
    return'480 done'



if __name__ == '__main__':
    path = "/Users/shiluwu/Documents/Spring2019/EC500/Exercise2/video_in"  # 文件夹目录
    files = os.listdir(path)
    que = queue.Queue()
    que2 = queue.Queue()
    for file in files:
        que.put(file)
        que2.put(file)
        print(file)
    que.get()
    que2.get()

    coroutine720 = video720(que2)
    coroutine480 = video480(que)

    tasks = [asyncio.ensure_future(coroutine480), asyncio.ensure_future(coroutine720)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print('Task: ', task.result())
