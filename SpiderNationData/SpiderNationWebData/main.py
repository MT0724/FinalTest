#从database模块导入写入数据函数
from database import insert_financedata, insert_populationdata, insert_exchangerate
#从graph模块中导入绘图函数
from plotview import population_draw, finance_draw, rate_draw

#------------------
#向数据库中写入数据
#------------------
insert_populationdata()  #写入人口数据
insert_financedata()     #写入财政数据
insert_exchangerate()    #写入汇率数据

#----
#绘图
#----
population_draw()   #绘制人口情况图
finance_draw()      #绘制财政情况图
rate_draw()         #绘制人民币对外汇率情况图

