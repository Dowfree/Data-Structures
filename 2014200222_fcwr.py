# -*- coding: UTF-8 -*-
#在非诚勿扰节目现场有100盏灯，每盏灯都给了编号，分别为从1到100。每盏灯由一个美女嘉宾来控制。美女嘉宾按一下开关，灯就亮了，再按一下灯就灭了。美女嘉宾也给了编号，她们的编号与被控制的灯的编号相同。开始时，灯是全灭的。主持人孟非宣布将按照以下规则让美女嘉宾来决定他的命运。紧张时刻，马上开始。第一回合，所有美女嘉宾按一下开关，这时，所有的灯都亮了。男生大喜，俨然成了亮灯帝第二回合，所有编号为2的倍数的美女嘉宾按一下开关。男生心一沉，怎么一半的灯灭了。z第三回合，所有编号为3的倍数的美女嘉宾按一下开关。男生纳闷，怎么有的灯亮了，有的灯灭了。如此反复。第N回合，所有编号为N的倍数的美女嘉宾按一下开关。在第100回合后，还能虏获多少美女嘉宾的芳心？
def fcwr():
    a=[0]*100
    for i in range(100):
        for j in range(i,100):
            if (j+1)%(i+1)==0:
                a[j]=a[j]+1
    num=[]
    for i in range(len(a)):
        if a[i]%2!=0:
            num.append(i+1)
    return num