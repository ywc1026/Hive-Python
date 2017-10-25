
import random
import datetime


def userinfo():

    area_list = ['Beijing', 'Shanghai', 'Hangzhou', 'Chengdu']
    fd = open("/home/ywc/PycharmProjects/userinfo.txt", "w+")
    for i in range(1000):
        userid = str(100+i)
        age = str(random.randrange(10, 40))
        area = random.choice(area_list)
        user_money = str(i)
        str_temp = userid+','+age+','+area+','+user_money+'\n'
        fd.write(str_temp)
    fd.close()


def gameinfo():

    game_list = ['dota', 'dota2', 'lol', 'wangzhe']
    fd = open("/home/ywc/PycharmProjects/gameinfo.txt", "w+")
    for i in range(4):
        gameid = str(i)
        gamename = str(game_list[i])
        str_temp = gameid+','+gamename+'\n'
        fd.write(str_temp)
    fd.close()


def gametime():

    game_list = [0, 1, 2, 3]
    time_list = [10, 15, 20, 30, 50, 80, 90]

    for j in range(10):
        date = (datetime.datetime.now()+datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        fd = open("/home/ywc/PycharmProjects/stat/gametime_{}.txt".format(date), "w+")
        for i in range(1000):
            fdate = str(date)
            userid = str(100+i)
            gameid = str(random.choice(game_list))
            gametime = str(random.choice(time_list))
            str_temp = fdate+','+userid+','+gameid+','+gametime+'\n'
            fd.write(str_temp)
    fd.close()


def userfee():

    game_list = [0, 1, 2, 3]
    time_list = [10, 15, 30, 40, 50, 55, 62]

    for j in range(10):
        date = (datetime.datetime.now()+datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        fd = open("/home/ywc/PycharmProjects/stat/userfee_{}.txt".format(date), "w+")
        for i in range(1000):
            fdate = str(date)
            userid = str(100+i)
            gameid = str(random.choice(game_list))
            gametime = str(random.choice(time_list))
            str_temp = fdate+','+userid+','+gameid+','+gametime+'\n'
            fd.write(str_temp)
    fd.close()

if __name__ == '__main__':

    userfee()
    gametime()
