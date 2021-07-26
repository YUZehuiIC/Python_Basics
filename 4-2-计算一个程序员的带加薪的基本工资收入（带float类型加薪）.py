# 追求上进程序员的优越生活
# 计算一个程序员的带加薪的基本工资收入（带float类型加薪）
salary = 25000
sa_total  = 0
sa_year   = 0
sa_rate   = 1.05
sa_ceil   = 50000
sa_current = 0.0
for i in range(40):
    sa_current = salary*(1.05**i)
    
    if(sa_current>50000): sa_current = 50000.0
    
    sa_year  = sa_current * 12
    sa_total = sa_total + sa_year
    print(str.format('第 {0:2} 年工资 {1:6.7} ,年收入 {2:6.10} 元',i,sa_current,sa_year))
    
print('-------------------------------')
print(str.format('一生工资总收入{0:6.10}元',sa_total))
print('收入数据类型（sa_total）：',type(sa_total))

