# -*- coding: utf-8 -*-
"""
@author: Sirius5783
@license: None
@contact: markdan@foxmail.com
@file: GUI.py
@time: 2018/8/1 0001 3:10
@desc:Windows 10,Python3.6
"""
"""

"""
import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox
from settings import settings

class GraphicInterface:
    def  __init__(self):
        if os.path.exists('path.nga'):
            with open('path.nga', 'r', encoding='utf-8') as file:
                file = file.read().split('\n')[0]
                if file[-8:] == 'simc.exe':
                    self.simPath = file
                    settings.simc_path = self.simPath
                    self.stringInput()
                else:
                    os.remove('path.nga')
                    os.popen("AutoSimc-master-NGA特供版811.exe")
                    quit()
        else:
            self.root = tk.Tk()
            self.root.title('sim路径检查    AutoSimC-NGA')
            self.root.geometry('390x100+735+420')

            self.status = tk.Label(relief=RIDGE, anchor=W)
            self.status.config(text='状态:未选择或选择的非simc.exe程序!请重新选择', fg='red')
            self.status.place(x=60, y=50)

            self.simcButton = tk.Button(text='Simc路径选择', width=20, command=self.fileOpen)
            self.simcButton.place(x=120, y=10)

            self.root.mainloop()

    def fileOpen(self):
        '''
        打开文件路径选择器，选择sim路径
        '''
        self.fileName = askopenfilename()
        # print(repr(self.fileName))
        if self.fileName[-8:] == 'simc.exe':
            self.simPath = self.fileName
            with open('path.nga', 'w', encoding='utf-8') as file:
                file.write(self.simPath)
                self.status.config(text='状态:已选择:' + self.simPath, fg='blue')
                self.root.destroy()
                self.stringInput()
        else:
            self.status.config(text='状态:未选择或选择的非simc.exe程序!请重新选择', fg='red')

    def stringInput(self):
        '''
        接收用户输入角色字符串
        '''
        self.root = tk.Tk()
        self.root.title('AutoSimC-master-NGA 08/11')
        self.root.geometry('480x740+635+120')

        # canvas = Canvas(self.root, width=490, height=740)
        # canvas.place(x=0,y=0)
        # canvas.create_rectangle(5, 685, 485, 735)

        tk.Label(self.root, text='最少装备橙装数:', fg='blue').place(x=60, y=10)
        self.min_leg = tk.IntVar()
        self.min_leg.set(0)
        tk.Radiobutton(self.root, text='0', variable=self.min_leg, value=0, command=self.leg_spe).place(x=160, y=0)
        tk.Radiobutton(self.root, text='3', variable=self.min_leg, value=3, command=self.leg_spe).place(x=160, y=20)

        tk.Label(self.root, text='Boss类型选择:', fg='blue').place(x=245, y=5)
        self.boss_types = {"帕奇维克(木桩单体)": "Default_Patchwerk", "轻移动战": "Default_LightMovement", "奥特拉赛恩(周期性击晕)": "Default_Ultraxion",
                           "兽王(刷新2种小怪,移动战)": "Default_Beastlord", "2个重叠的帕奇维克": "Two Patchwerks, stacked",
                           "2个相隔27码的帕奇维克": "Two Patchwerks, 27 yards away from each other"}
        self.boss_type = tk.StringVar()
        self.boss_type.set('帕奇维克(木桩单体)')
        tk.OptionMenu(self.root, self.boss_type, *self.boss_types.keys(), command=self.options_spe).place(x=245, y=25)

        tk.Label(self.root, text='模拟程序运行优先级:', fg='blue').place(x=245, y=65)
        self.priorities = {'低(推荐)': 'low', '中下': 'below_normal', '中等': 'normal', '中上': 'above_normal', '最高(可能使你的系统失去响应)': 'highest'}
        self.priority = tk.StringVar()
        self.priority.set('低(推荐)')
        tk.OptionMenu(self.root, self.priority, *self.priorities, command=self.options_spe).place(x=245, y=85)

        tk.Label(self.root, text='最少装备T21套装数:', fg='blue').place(x=60, y=55)
        self.min_T21 = tk.IntVar()
        self.min_T21.set(0)
        tk.Radiobutton(self.root, text='0', variable=self.min_T21, value=0, command=self.T21_spe).place(x=180, y=45)
        tk.Radiobutton(self.root, text='4', variable=self.min_T21, value=4, command=self.T21_spe).place(x=180, y=65)

        tk.Label(self.root, text='模拟模式选择:', fg='blue').place(x=60, y=100)
        self.mode = tk.IntVar()
        self.mode.set(2)
        tk.Radiobutton(self.root, text='静态(耗时少)', variable=self.mode, value=1, command=self.sta_spe).place(x=142, y=90)
        tk.Radiobutton(self.root, text='动态(更精准)', variable=self.mode, value=2, command=self.sta_spe).place(x=142, y=110)

        self.entry = tk.Text(width=50, height=30)
        self.entry.insert(tk.INSERT, '请输入您通过/SimPermut插件获得的角色字符串\n然后粘贴并覆盖此文本框内容')
        self.entry.place(x=65, y=140)

        self.boom = tk.Button(text='DIE DIE DIE', width=20, command=self.inputCheck)
        self.boom.place(x=155, y=545)

        tk.Label(anchor=W,text='已选择simc路径:' + self.simPath,).place(x=65, y=585)
        tk.Label(anchor=W,text='若要重新选择simc路径，请删除path.nga文件').place(x=65, y=605)
        tk.Label(anchor=W, text='AutoSimC介绍:\n将您身上的装备宝石等自动输入Simulationcraft中进行组合\n'
        '然后批量模拟伤害能力最后输出DPS最高的配装以供参考\n开源https://github.com/Sirius5783/AutoSimC',fg='blue').place(x=65, y=635)

        self.root.mainloop()

    def inputCheck(self):
        strings = self.entry.get('1.0', END)
        if '[Profile]' in strings:
            with open('input.txt', 'w', encoding='utf-8') as inputFile:
                inputFile.write(strings)
            messagebox.showinfo(title='成功!', message='模拟即将开始,请耐心等待。')
            self.start_autosimc()
        else:
            messagebox.showerror(title='错误提示', message='您输入的不是合法的角色字符串,请重新输入~')

    def leg_spe(self,*args):
        settings.default_leg_min = int(self.min_leg.get())

    def T21_spe(self,*args):
        settings.default_equip_t21_min = int(self.min_T21.get())

    def options_spe(self,*args):
        settings.default_fightstyle = self.boss_types[self.boss_type.get()]
        settings.simc_priority = self.priorities[self.priority.get()]

    def sta_spe(self,*args):
        #print('mode=',self.mode.get())
        settings.auto_choose_static_or_dynamic = self.mode.get()

    def start_autosimc(self):
        self.root.destroy()
        import main
        main.runs()

        input('***********************************\n按回车或者右上角叉叉即可关闭程序啦.')

if __name__ == '__main__':
    print('请不要关闭这个黑色的窗口')
    try:
        user = GraphicInterface()
    except Exception as e:
        with open("GUIERROR.txt","w") as file:
            file.write(str(e))
