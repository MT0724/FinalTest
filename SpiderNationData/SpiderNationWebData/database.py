import sqlite3
#从spydata模块中导入爬虫函数
from spydata import getfinance_data, getpopula_data, getexchange_rate

#创建数据库中population数据表并将人口数据写入数据表
def insert_populationdata():
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    # ------------------------------------------------------------------------------------------------------------
    # 创建数据表population,此表共有4列，年份year、总人口total_number、男性人口数male_number、女性人口数female_number
    # ------------------------------------------------------------------------------------------------------------
    try:
        c.execute('create table population (year int primary key,total_number int,male_number int,female_number int)')
    #如果数据表已被创建
    except sqlite3.OperationalError:
        pass
    # 调用爬虫函数spyder_getdata获取数据
    data1 = getpopula_data()
    data_one = data1['returndata']['datanodes']
    #---------------------------------------
    #按2018—2009时间顺序将各项数据写入数据库
    #---------------------------------------
    #写入总人口数据
    for i in range(0, 10):
        year_num1 = 2018 - i
        number_num1 = data_one[i]['data']['data']
        try:
            c.execute('insert into population (year, total_number) values (%d,%d)' % (year_num1,number_num1))
        #若表中已有总人口数据
        except sqlite3.IntegrityError:
            c.execute('update population set total_number = %d where year = %d' % (number_num1, year_num1))
    #写入男性人口数
    for i in range(20, 30):
        year_num2 = 2038 - i
        number_num2 = data_one[i]['data']['data']
        try:
            c.execute('insert into population (year, male_number) values (%d,%d)' % (year_num2, number_num2))
        #若表中已有男性人口数据
        except sqlite3.IntegrityError:
            c.execute('update population set male_number = %d where year = %d' % (number_num2, year_num2))
    #写入女性人口数
    for i in range(40, 50):
        year_num3 = 2058 - i
        number_num3 = data_one[i]['data']['data']
        try:
            c.execute('insert into population (year, female_number) values (%d,%d)' % (year_num3, number_num3))
        #若表中已有女性人口数据
        except sqlite3.IntegrityError:
            c.execute('update population set female_number = %d where year = %d' % (number_num3,year_num3))
    c.close()
    conn.commit()
    conn.close()

#插入人民币汇率数据
def insert_exchangerate():
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    # ------------------------------------------------------------------------------------------------------------
    # 创建数据表exchangedata,此表共有5列，年份year、对美汇率m_rate、对日汇率r_rate、对港汇率g_rate、对欧汇率o_rate
    # ------------------------------------------------------------------------------------------------------------
    try:
        c.execute('create table exchangedata (year int primary key,m_rate int,r_rate int,g_rate int,o_rate int)')
    #如果数据表已被创建
    except sqlite3.OperationalError:
        pass
    # 调用爬虫函数spyder_getdata获取数据
    # data1 = getexchange_rate()
    # rate_data = data1['returndata']['datanodes']
    ratedata1, ratedata2, ratedata3, ratedata4 = getexchange_rate()
    rate_data = ratedata1['returndata']['datanodes'] + ratedata2['returndata']['datanodes'] + \
                ratedata3['returndata']['datanodes'] + ratedata4['returndata']['datanodes']

    print("rate_data",rate_data)
    #---------------------------------------
    #按2018—2009时间顺序将各项数据写入数据库
    #---------------------------------------
    #写入对美汇率数据
    for i in range(0, 10):
        year_num1 = 2018 - i
        number_num1 = rate_data[i]['data']['data']
        try:
            c.execute('insert into exchangedata (year, m_rate) values (%d,%d)' % (year_num1,number_num1))
        #若表中已有对美汇率数据
        except sqlite3.IntegrityError:
            c.execute('update exchangedata set m_rate = %d where year = %d' % (number_num1, year_num1))
    #写入对日汇率数据
    for i in range(20, 30):
        year_num2 = 2038 - i
        number_num2 = rate_data[i]['data']['data']
        try:
            c.execute('insert into exchangedata (year, r_rate) values (%d,%d)' % (year_num2, number_num2))
        #若表中已有对日汇率数据
        except sqlite3.IntegrityError:
            c.execute('update exchangedata set r_rate = %d where year = %d' % (number_num2, year_num2))
    #写入对港汇率数据
    for i in range(40, 50):
        year_num3 = 2058 - i
        number_num3 = rate_data[i]['data']['data']
        try:
            c.execute('insert into exchangedata (year, g_rate) values (%d,%d)' % (year_num3, number_num3))
        #若表中已有对港汇率数据
        except sqlite3.IntegrityError:
            c.execute('update exchangedata set g_rate = %d where year = %d' % (number_num3,year_num3))
    # 写入对欧汇率数据
    for i in range(60, 70):
         year_num4 = 2078 - i
         number_num4 = rate_data[i]['data']['data']
         try:
             c.execute('insert into exchangedata (year, o_rate) values (%d,%d)' % (year_num4, number_num4))
         # 若表中已有对欧汇率数据
         except sqlite3.IntegrityError:
             c.execute('update exchangedata set o_rate = %d where year = %d' % (number_num4, year_num4))
    c.close()
    conn.commit()
    conn.close()

#创建数据库中finance数据表并将数据写入数据表
def insert_financedata():
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    #-----------------------------------------------------------------------------------------------------------------
    #创建数据表finance,此表共有5列，年份year、收入income、支出outcome、收入增长速度incomespeed、支出增长速度outcomespeed
    #-----------------------------------------------------------------------------------------------------------------
    try:
        c.execute('create table finance (year int primary key,income int,outcome int,incomespeed int, outcomespeed int)')
    #如果数据表已被创建
    except sqlite3.OperationalError:
        pass
    # 调用爬虫函数getfinance_data获取数据
    financedata1, financedata2, financedata3, financedata4 = getfinance_data()
    # financedata1,financedata2,financedata3,financedata4 = data1['returndata']['datanodes']
    financedata = financedata1['returndata']['datanodes'] + financedata2['returndata']['datanodes'] + \
                  financedata3['returndata']['datanodes'] + financedata4['returndata']['datanodes']

    #---------------------------------------
    #按2018—2009时间顺序将各项数据写入数据库
    #---------------------------------------
    #写入财政收入数据
    for i in range(0, 10):
        year_num1 = 2018 - i
        number_num1 = financedata[i]['data']['data']
        try:
            c.execute('insert into finance (year, income) values (%d,%d)' % (year_num1,number_num1))
        #若表中已有财政收入数据
        except sqlite3.IntegrityError:
            c.execute('update finance set income = %d where year = %d' % (number_num1, year_num1))
    #写入财政支出数据
    for i in range(20, 30):
        year_num2 = 2038 - i
        number_num2 = financedata[i]['data']['data']
        try:
            c.execute('insert into finance (year, outcome) values (%d,%d)' % (year_num2, number_num2))
        #若表中已有财政支出数据
        except sqlite3.IntegrityError:
            c.execute('update finance set outcome = %d where year = %d' % (number_num2, year_num2))
    #写入财政收入增长速度数据
    for i in range(40, 50):
        year_num3 = 2058 - i
        number_num3 = financedata[i]['data']['data']
        try:
            c.execute('insert into finance (year, incomespeed) values (%d,%d)' % (year_num3, number_num3))
        #若表中已有财政收入增长速度数据
        except sqlite3.IntegrityError:
            c.execute('update finance set incomespeed = %d where year = %d' % (number_num3,year_num3))
    #写入财政支出增长速度数据
    for i in range(60,70):
        year_num4 = 2078 - i
        number_num4 = financedata[i]['data']['data']
        try:
            c.execute('insert into finance (year, outcomespeed) values (%d,%d)' % (year_num4, number_num4))
        # 若表中已有财政支出增长速度数据
        except sqlite3.IntegrityError:
            c.execute('update finance set outcomespeed = %d where year = %d' % (number_num4, year_num4))
    c.close()
    conn.commit()
    conn.close()

#读取population数据表中数据
#6个参数依次为年份，年末总人口，男性人口数，女性人口数，男性人口占比，女性人口占比
def select_population(year, total_amount, male_amount, female_amount, ma_scale, fema_scale):
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    # ------------------------
    # 从population表中选择数据
    # ------------------------
    for i in range(0, 10):
        c.execute('select * from population where year=?', (2018 - i,))
        values = c.fetchall()
        print(values[0])
        year.append(values[0][0])#年份
        total_amount.append(values[0][1])#年末总人口
        male_amount.append(values[0][2])#年末男性人口数
        female_amount.append(values[0][3])#年末女性人口数
        ma_scale.append(float(100 * values[0][2]) / float(values[0][1]))#男性人口占总人口比例
        fema_scale.append(float(100 * values[0][3]) / float(values[0][1]))#女性人口占总人口比例
    c.close()
    conn.close()
    # --------------------------------------------------------------
    # 所获得的6个列表均为2018年-1999年，做一次转置，变为1999年-2018年
    # --------------------------------------------------------------
    year.reverse()
    total_amount.reverse()
    male_amount.reverse()
    female_amount.reverse()
    ma_scale.reverse()
    fema_scale.reverse()

#读取exchangedata表中数据
#5个参数依次为年份，对美汇率，对日汇率，对港汇率，对欧汇率
def select_rate(year, m_rate, r_rate, g_rate, o_rate):
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    #---------------------
    #从exchangedata表中选择数据
    #---------------------
    for i in range(0, 10):
        c.execute('select * from exchangedata where year=?', (2018 - i,))
        values = c.fetchall()
        print(values[0])
        year.append(values[0][0])         #年份
        m_rate.append(values[0][1])       #对美汇率
        r_rate.append(values[0][2])       #对日汇率
        g_rate.append(values[0][3])       #对港汇率
        o_rate.append(values[0][4])       #对欧汇率
    c.close()
    conn.close()
    # --------------------------------------------------------------
    # 所获得的5个列表均为2018年-1999年，做一次转置，变为1999年-2018年
    # --------------------------------------------------------------
    year.reverse()
    m_rate.reverse()
    r_rate.reverse()
    g_rate.reverse()
    o_rate.reverse()

#读取finance数据便中数据
#5个参数依次为年份，财政收入，财政支出，财政收入增长速度，财政支出增长速度
def select_finance(year, income_amount, outcome_amount, inspeed, outspeed):
    conn = sqlite3.connect('E:/mydemo/database.db')
    c = conn.cursor()
    #---------------------
    #从finance表中选择数据
    #---------------------
    for i in range(0, 10):
        c.execute('select * from finance where year=?', (2018 - i,))
        values = c.fetchall()
        print(values[0])
        year.append(values[0][0])          #年份
        income_amount.append(values[0][1]) #财政收入
        outcome_amount.append(values[0][2])#财政支出
        inspeed.append(values[0][3])       #财政收入增长速度
        outspeed.append(values[0][4])      #财政支出增长速度
    c.close()
    conn.close()
    # --------------------------------------------------------------
    # 所获得的5个列表均为2018年-1999年，做一次转置，变为1999年-2018年
    # --------------------------------------------------------------
    year.reverse()
    income_amount.reverse()
    outcome_amount.reverse()
    inspeed.reverse()
    outspeed.reverse()
