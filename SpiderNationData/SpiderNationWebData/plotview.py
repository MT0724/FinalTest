import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
#从database文件中导入获取数据库中的数据函数
from database import select_population, select_finance, select_rate

#人口绘图模块
def population_draw():

    year = []          #年份
    total_amount = []  #总人口
    male_amount = []   #男性人口
    female_amount = [] #女性人口
    ma_scale = []      #男性人口占比
    fema_scale = []    #女性人口占比

    #调用select_population()函数获取以上6个列表值
    select_population(year, total_amount, male_amount, female_amount, ma_scale, fema_scale)

    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # -------------------------------------------------
    # 开启第一个视图，用来显示年末总人口随年份变化条形图
    # -------------------------------------------------
    fig1 = plt.figure('年末总人口条形图')
    #设置标题
    plt.title('(2009-2018年)年末总人口')
    #绘制年末总人口随年份变化条形图
    plt.bar(np.arange(10), total_amount, width=0.8, label=u'年末总人口', color='g')
    #设置y轴取值范围、标注
    plt.ylim(130000, 140000)
    plt.ylabel('年末总人口')
    #设置x轴标注、刻度、倾斜45°
    plt.xlabel('年份')
    plt.xticks(np.arange(10), year)
    plt.xticks(rotation=45)
    #设置图例
    plt.legend(loc='upper left')
    #添加网格
    plt.grid(b=True,axis='y',linestyle='--')
    fig1.savefig("1_total_population.png")
    #-------------------------------------------
    #开启第二个视图，用来显示男女性人口占比折线图
    #-------------------------------------------
    fig2 = plt.figure('男女占比情况折线图')
    #y轴显示百分数
    fmt = '%.2f%%'
    ytickscale = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(ytickscale)
    #设置折线图标题
    plt.title('(2009-2018年)男女性在总人口中的占比情况')
    #绘图
    p1, = plt.plot(np.arange(10), ma_scale, color = 'blue')#男性人口占比图
    p2, = plt.plot(np.arange(10), fema_scale, color = 'red')#女性人口占比图
    #设置x轴标注、刻度、倾斜45°
    plt.xlabel('年份')
    plt.xticks(np.arange(10), year)
    plt.xticks(rotation=45)
    #设置y轴标注
    plt.ylabel('占总人口的百分比')
    #添加图例
    plt.legend([p1, p2], ['男性人口占比', '女性人口占比'], loc='upper right')
    #添加网格
    plt.grid(b=True, linestyle='--')
    fig2.savefig("2_percentage.png")
    plt.show()

#财政绘图模块
def finance_draw():
    year = []           #年份
    income_amount = []  #财政收入
    outcome_amount = [] #财政支出
    inspeed = []        #财政收入增长速度
    outspeed = []       #财政支出增长速度

    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    select_finance(year,income_amount,outcome_amount,inspeed,outspeed)
    # ---------------------------------------------------
    # 开启第三个视图，用来显示财政收入财政支出随年份变化图
    # ---------------------------------------------------
    fig3 = plt.figure('收入支出变化条形图')
    #绘图
    plt.bar(np.arange(10), height=income_amount, width=0.25, alpha=0.8, color='r', label=u'财政收入')#财政收入随年份变化条形图
    plt.bar(np.arange(10)+0.25, height=outcome_amount, width=0.25, alpha=0.8, color='g', label=u'财政支出')#财政支出随年份变化条形图
    # ----------------------------------
    # 设置x轴参数(标注、刻度值并旋转45°)
    # ----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(10), year)
    plt.xticks(rotation=45)
    # 设置y轴标注
    plt.ylabel('财政收入支出/亿元')
    # 设置条形图标题
    plt.title('(2009-2018年)财政收入支出变化条形图')
    #显示网格
    plt.grid(b=True, axis='y', linestyle='--')
    #添加图例
    plt.legend()
    #保存图片
    fig3.savefig("3_financedata.png")
    #-----------------------------------------------
    #开启第四个视图，显示财政收入、支出增长速度折线图
    #-----------------------------------------------
    fig4 = plt.figure('收入支出增长速度折线图')
    #绘图
    p1, = plt.plot(np.arange(10), inspeed, color='red')  # 财政收入增长速度折线图
    p2, = plt.plot(np.arange(10), outspeed, color='green')  # 财政支出增长速度折线图
    #-----------------------------------
    #添加x轴标注,x轴刻度值,x轴字体旋转45°
    #-----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(10),year)
    plt.xticks(rotation=45)
    # -------------
    # 设置y轴参数
    # -------------
    #y轴显示小数点后一位百分数
    fmt = '%.1f%%'
    ytickscale = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(ytickscale)
    #添加y轴标注
    plt.ylabel('财政增长速度%')
    #添加折线图标题
    plt.title('(2009-2018年)财政收入支出增长速度折线图')
    #添加图例
    plt.legend([p1, p2], ['财政收入增长速度', '财政支出增长速度'], loc='upper right')
    #显示网格
    plt.grid(b=True, linestyle='--')
    fig4.savefig("4_growthrate.png")
    plt.show()

#汇率绘图模块
def rate_draw():
    year = []           #年份
    m_rate = []         #对美汇率
    r_rate = []         #对日汇率
    g_rate = []         #对港汇率
    o_rate = []         #对欧汇率

    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    select_rate(year,m_rate,r_rate,g_rate,o_rate)
    # ---------------------------------------------------
    # 开启第五个视图，用来显示人民币对美对欧汇率随年份变化图
    # ---------------------------------------------------
    fig5 = plt.figure('人民币对美对欧汇率变化条形图')
    #绘图
    plt.bar(np.arange(10), height=m_rate, width=0.35, alpha=0.8, color='r', label=u'对美汇率')#人民币对美汇率随年份变化条形图
    plt.bar(np.arange(10) + 0.35, height=o_rate, width=0.35, alpha=0.8, color='b', label=u'对欧汇率')#人民币对欧汇率随年份变化条形图
    # ----------------------------------
    # 设置x轴参数(标注、刻度值并旋转45°)
    # ----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(10), year)
    plt.xticks(rotation=45)
    # 设置y轴标注
    plt.ylabel('人民币对外汇率')
    # 设置条形图标题
    plt.title('(2009-2018年)人民币对外汇率变化条形图')
    #显示网格
    plt.grid(b=True, axis='y', linestyle='--')
    #添加图例
    plt.legend()
    #保存图片
    fig5.savefig("5_exchangerate_mo.png")
    plt.show()

    # ---------------------------------------------------
    # 开启第六个视图，用来显示人民币对日对港汇率随年份变化图
    # ---------------------------------------------------
    fig6 = plt.figure('人民币对日对港汇率变化条形图')
    # 绘图
    plt.bar(np.arange(10), height=r_rate, width=0.35, alpha=0.8, color='r', label=u'对日汇率')  # 人民币对日汇率随年份变化条形图
    plt.bar(np.arange(10) + 0.35, height=g_rate, width=0.35, alpha=0.8, color='b', label=u'对港汇率')  # 人民币对港汇率随年份变化条形图
    # ----------------------------------
    # 设置x轴参数(标注、刻度值并旋转45°)
    # ----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(10), year)
    plt.xticks(rotation=45)
    # 设置y轴标注
    plt.ylabel('人民币对外汇率')
    # 设置条形图标题
    plt.title('(2009-2018年)人民币对外汇率变化条形图')
    # 显示网格
    plt.grid(b=True, axis='y', linestyle='--')
    # 添加图例
    plt.legend()
    # 保存图片
    fig6.savefig("6_exchangerate_rg.png")
    plt.show()



