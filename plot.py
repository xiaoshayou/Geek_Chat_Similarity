import matplotlib.pyplot as plt
import numpy as np

## 这两句话太他妈重要了，用来解决matplotlib画图中文乱码的问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

zpc={}
zpc[100000]='技术'
zpc[110000]='产品'
zpc[120000]='设计'
zpc[130000]='运营'
zpc[140000]='市场'
zpc[150000]='职能&高级管理'
zpc[160000]='销售'
zpc[170000]='传媒'
zpc[180000]='金融'
zpc[190000]='教育培训'
zpc[200000]='其他'
zpc[210000]='医疗健康'
zpc[220000]='房地产&建筑'
zpc[230000]='汽车'
zpc[240000]='供应链&物流'
zpc[250000]='采购&贸易'
zpc[260000]='咨询&翻译&法律'
zpc[270000]='实习生&管培生'
zpc[280000]='旅游'
zpc[290000]='酒店&餐饮&零售'
zpc[300000]='生产制造'

city={}
city[0]='一'
city[1]='二'
city[2]='三'
city[3]='四'

#存放从txt读取的数据
data_raw = np.array([]) 

f = open("E:\Projects\lmy_chat_similarity_res.txt",encoding='utf-8')

line = f.readline()
while line:
    data_raw = np.append(data_raw,line.split())
    line = f.readline()
f.close()

data = np.reshape(data_raw,(-1,7)).astype(int)

# 对一级类进行循环
for l1_code in ([100000,110000,120000,130000,140000,150000,160000,170000,180000,190000,200000,210000,220000,230000,240000,250000,260000,270000,280000,290000,300000]):  
    
    # 每个一级类生成一个大图
    fig = plt.figure(figsize=(40,10))
    
    # 对城市等级进行循环
    for city_level in range(4): 
        
        # 某个一级类下某个城市等级下的A、B、C、D数据
        data_img_raw=np.array([]);
        data_img=np.array([]);
        for i in range(np.shape(data)[0]):
            if(data[i][0]==(city_level+1) and data[i][1]==l1_code):
                data_img_raw = np.append(data_img_raw,data[i][2:7])
        data_img = data_img_raw.astype(int).reshape(-1,5)
        
        # 每个一级类的大图下对应四个小图，各个小图对应一个城市等级的数据
        sub_fig = fig.add_subplot(1,4,city_level+1)
        
        l1 = sub_fig.scatter(data_img[:,0],data_img[:,1])
        l2 = sub_fig.scatter(data_img[:,0],data_img[:,2])
        l3 = sub_fig.scatter(data_img[:,0],data_img[:,3])
        l4 = sub_fig.scatter(data_img[:,0],data_img[:,4])
        
        sub_fig.set_title(city[city_level] +'线城市',fontsize = 30) # 子图标题
        sub_fig.set_xlim(0,50) # x坐标轴范围
        sub_fig.set_ylim(0,2200) # y坐标轴范围
        sub_fig.tick_params(labelsize = 20) # 坐标轴刻度的字体
        sub_fig.legend(handles = [l1, l2, l3, l4], labels = ['A', 'B', 'C', 'D'], loc = 'best', fontsize = 20) # 图例
        sub_fig.grid(True, linestyle = "-.", color = "black", linewidth = "0.5") #网格
    
    fig.suptitle(zpc[l1_code],fontsize = 50) #大图标题
    plt.savefig("E:\\Projects\\"+zpc[l1_code]+".jpg") #保存图片
