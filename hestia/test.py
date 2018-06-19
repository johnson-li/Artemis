# 人为设定：每一次活动持续一个滴答

import threading
import time


def start():
    global status
    try:
        with open("status.txt") as f:
            lines = f.readlines()
        hours = int(lines[0].replace('hours:', ''))
        state = lines[1].replace('state:', '')
        happiness = int(lines[2].replace('happiness:', ''))
        hungry = int(lines[3].replace('hungry:', ''))
        health = int(lines[4].replace('health:', ''))
        status = {'hours': hours, 'state': state, 'happiness': happiness, 'hungry': hungry, 'health': health}
    except FileNotFoundError:
        status = {'hours': 7, 'state': '我在睡觉', 'happiness': 100, 'hungry': 50, 'health': 100}
    statusPrint()


def fun_timer():
    global timer, status
    status['hours'] += 1
    if status['hours'] > 23:
        status['hours'] = 0

    if status['hungry'] > 80 or status['hungry'] < 20:
        status['healthy'] -= 2
    if status['happy'] < 20:
        status['healthy'] -= 1

    timer = threading.Timer(5.0, fun_timer)  # 5s执行一次fun_timer
    timer.start()


def doNothing():
    global status, timerDoNothing
    if status['hours'] >= 8:
        status['hungry'] += 2
        status['happy'] -= 1
        status['state'] = '我醒着但很无聊'
    else:
        status['hungry'] += 1
        status['state'] = '我在睡觉'

    timerDoNothing = threading.Timer(5.0, doNothing)
    timerDoNothing.start()


def statusPrint():
    global status
    print('当前时间：{}点'.format(status['hours']))
    print('我当前的状态：' + status['state'])
    print('Happiness:    Sad ' + '*' * (status['happiness'] // 2) + '-' * (50 - status['happiness'] // 2) + ' Happy({})'.format(status['happiness']))
    print('Hungry:      Full ' + '*' * (status['hungry'] // 2) + '-' * (50 - status['hungry'] // 2) + ' Hungry({})'.format(status['hungry']))
    print('Health:      Sick ' + '*' * (status['health'] // 2) + '-' * (50 - status['health'] // 2) + ' Healthy({})'.format(status['healthy']))


def walk():
    global status, timerActivities
    timerDoNothing.cancel()
    status['hungry'] += 3
    status['healthy'] += 1
    status['state'] = '我在散步'
    print('我在散步.....')

    timerActivities = threading.Timer(5.0, commands)
    timerActivities.start()


def play():
    global status, timerActivities, timerDoNothing
    timerDoNothing.cancel()
    status['hungry'] += 3
    status['happy'] += 1
    status['state'] = '我在玩耍'

    print('我在玩耍.....')

    timerActivities.start()


def feed():
    global status, timerActivities, timerDoNothing
    timerDoNothing.cancel()
    status['hungry'] -= 3
    status['state'] = '我在吃饭'
    print('我在吃饭.....')

    timerActivities.start()


def seedoctor():
    global status, timerActivities, timerDoNothing
    timerDoNothing.cancel()
    status['healthy'] += 4
    status['state'] = '我在看医生'
    print('我在看医生.....')

    timerActivities.start()


def commands():
    global status, timer
    doNothing()
    while True:
        command = input("你想：")
        if status['hours'] >= 8:
            if command == 'walk':
                walk()
            elif command == 'play':
                play()
            elif command == 'feed':
                feed()
            elif command == 'seedoctor':
                seedoctor()
            elif command == 'letalone' or '':
                print('我醒着但很无聊.....')
            elif command == 'status':
                statusPrint()
            elif command == 'bye':
                timer.cancel()
                print("记得来找我！Bye.....")
                break
            else:
                print("我不懂你在说什么")
        else:
            if command == 'walk' or 'play' or 'feed' or 'seedoctor':
                ensure = input("你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）")
                if ensure == y:
                    status['happy'] = status['happy'] - 4
                    if command == 'walk':
                        walk()
                    elif command == 'play':
                        play()
                    elif command == 'feed':
                        feed()
                    elif command == 'seedoctor':
                        seedoctor()
                else:
                    continue
            elif command == 'letalone' or '':
                print('我在睡觉.....')
            elif command == 'status':
                statusPrint()
            elif command == 'bye':
                timer.cancel()
                print("记得来找我！Bye.....")
                break
            else:
                print('我不懂你在说什么')


def main():
    introduction = '我的名字叫Tommy,一直可爱的猫咪....\n你可以和我一起散步，玩耍，你也需要给我吃好吃的东西，带我去看病，也可以让我发呆......\n每次带我去活动，活动时间都为1个滴答...\nCommands:\n1.walk:散步\n2.play:玩耍\n3.feed:喂我\n4.seedoctor:看医生\n5.letalone:让我独自一人\n6.status:查看我的状态\n7.bye:不想看到我'
    print(introduction)
    start()
    fun_timer()
    commands()

    statusLines = []
    for key, value in status.items():
        statusLines.append('{}:{}\n'.format(key, value))
    with open("status.txt", 'w') as ff:
        ff.writelines(statusLines)


if __name__ == '__main__':
    main()