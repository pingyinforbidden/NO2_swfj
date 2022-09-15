# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:23:32 2021

@author: Administrator
"""


import os
import pandas as pd

def MeanCa(np_arr):
    exist = (np.array(np_arr) != 999999)
    t1=temp_iloc.replace(999999,0)
    num = np.array(t1).sum(axis=1)
    den = exist.sum(axis=1)
    ave=np.divide(num, den, out=np.zeros_like(num), where=den!=999999)
    return ave

re_df0=pd.DataFrame()
for i in range(len(name)):
    a=num_df[num_df.point==name[i]]
    a=a.fillna(999999)
    test_df=a.drop(a[a.iloc[:,6]>=1000].index)
    predict_df=a.drop(a[a.iloc[:,6]<1000].index)
    if len(test_df)==0:
        a1=pd.concat([test_df,predict_df])
        # re_df0=pd.concat([re_df0,a1])
        o=0
        n_list=[]
        for i1 in range(len(name)):
            if a['city'].iloc[0] in name[i1]:
                o=o+1
                n_list.append(i1)
        temp_iloc=pd.DataFrame()
        for i1 in n_list:
            a2=num_df[num_df.point==name[i1]]
            a2.reset_index(drop=True, inplace=True)
            temp_iloc[str(a.iloc[:,6].name)+str(i1)]=a2[a2.iloc[:,6].name]
            ave=MeanCa(temp_iloc)
            ave=pd.DataFrame(ave,columns=['ave'])
            ave=ave.fillna(999999)
            a2[a2.iloc[:,6].name]=ave['ave']
        test_df=a2.drop(a2[a2.iloc[:,6]>=1000].index)
        predict_df=a2.drop(a2[a2.iloc[:,6]<1000].index)
        test_arr=np.array(test_df[['year', 'doy', 'hour', 'point', a.iloc[:,6].name ]])
        features, labels=test_arr[:,:3],test_arr[:,4]
        train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
        regr=RandomForestRegressor()
        regr.fit(train_x,train_y)
        pre_arr=np.array(predict_df[['year', 'doy', 'hour', 'point',  a.iloc[:,6].name ]])
        pre=regr.predict(pre_arr[:,:3])
        predict_df[ a2.iloc[:,6].name ]=pre
        a3=pd.concat([test_df,predict_df])
        re_df0=pd.concat([re_df0,a3])
            
        print('jump ',i)
        
    else:
        test_arr=np.array(test_df[['year', 'doy', 'hour', 'point', a.iloc[:,6].name ]])
        features, labels=test_arr[:,:3],test_arr[:,4]
        train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
        regr=RandomForestRegressor()
        regr.fit(train_x,train_y)
        pre_arr=np.array(predict_df[['year', 'doy', 'hour', 'point',  a.iloc[:,6].name ]])
        pre=regr.predict(pre_arr[:,:3])
        predict_df[ a.iloc[:,6].name ]=pre
        a1=pd.concat([test_df,predict_df])
        re_df0=pd.concat([re_df0,a1])
        print(i)
re_df0.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/"+str(a.iloc[:,6].name)+".csv")


a1_p=r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore"
file=os.listdir(a1_p)
te_f=pd.read_csv(os.path.join(a1_p,file[0]),index_col=0)
te_f=te_f.drop(['pm2', 'pm10', 'so2', 'o3', 'no2','pr',
       'tem', 'hum', 'ws'],axis=1)
te_f=te_f.sort_values(['year', 'doy', 'hour','city','pot', 'point'], ascending=[True,True,True,False,False,True])
te_f=te_f.reset_index(drop=True)
for i in range(1,len(file)):
    de_f=pd.read_csv(os.path.join(a1_p,file[i]),index_col=0)
    de_f=de_f[['year', 'doy', 'hour','city','pot', 'point',os.path.splitext(file[i])[0]]]
    de_f=de_f.sort_values(['year', 'doy', 'hour','city','pot', 'point'], ascending=[True,True,True,False,False,True])
    de_f=de_f.reset_index(drop=True)
    te_f[os.path.splitext(file[i])[0]]=de_f[os.path.splitext(file[i])[0]]
    # pd.merge(te_f,de_f[['year','doy','hour','point',os.path.splitext(file[i])[0]]],how='left',on=['year','doy','hour','point'])
te_f.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/restor_total.csv")

import pandas as pd
loaction={'闽侯县大湖':[119.101839,26.3681], '闽侯县闽侯县环保局':[119.127177,26.134931], '闽侯县闽侯县教育局':[119.140118,26.158436], '连江县花坞村':[119.575057,26.201935], 
 '连江县小湾村':[119.526543,26.206646], '连江县连江县医院':[119.546839,26.195885], '罗源县滨海新城':[119.596993,26.478955], '罗源县罗源县环保局':[119.566174,26.491169],
 '罗源县罗源一中':[119.558225,26.49835], '厦门市洪文':[118.173808,24.482889], '厦门市鼓浪屿':[118.063233,24.450886], '厦门市溪东':[118.165492,24.82337],
 '厦门市湖里中学':[118.104738,24.509227], '泉港区泉港区环保局':[118.933254,25.125787], '泉港区凤北村':[118.908282,25.15009], '泉港区泉港二中':[118.913725,25.139047],
 '惠安县惠安县体育馆':[118.788759,25.020945], '惠安县惠安县图书馆':[118.817867,25.054312], '安溪县安溪参山':[118.233336,25.080421], '安溪县安溪砖文':[118.20044,25.057964],
 '安溪县安溪上山':[118.180687,25.075196], '永春县港永幼儿园':[118.297311,25.322836], '永春县永春师范':[118.310833,25.331455], '永春县永春一中':[118.284465,25.33433],
 '德化县荐解村':[118.282141,25.660193], '德化县龙门滩大厦':[118.257511,25.496451], '德化县德化县环保局':[118.234292,25.48983], '石狮市宝盖山':[118.684612,24.724236],
 '石狮市金林村':[118.605426,24.746641], '石狮市前廊村':[118.628685,24.752318], '晋江市华表山':[118.535224,24.776608], '晋江市晋江一中':[118.589204,24.825454],
 '晋江市曾井小区':[118.563865,24.806451], '南安市柳城变电站':[118.436265,24.952738], '南安市南安一中':[118.448577,24.978413], '南安市南美子站':[118.389975,24.984775],
 '泉州市东海大街':[118.654866,24.881491], '泉州市清源山':[118.603493,24.947018], '泉州市涂山街':[118.589989,24.904096], '泉州市津头埔':[118.626746,24.905335],
 '泉州市万安':[118.6846,24.955646], '云霄县立人学校':[117.340757,23.967271], '云霄县县环保局':[117.338791,23.945478], '漳浦县漳浦县气象局':[117.612859,24.139996],
 '漳浦县漳浦一中':[117.626154,24.10253], '诏安县诏安县监测站':[117.146777,23.714328], '诏安县诏安县医院':[117.188066,23.716687], '长泰县长泰县环保局':[117.760608,24.63108],
 '长泰县长泰一中':[117.745903,24.627209], '东山县东山二中':[117.531669,23.740631], '东山县东山一中':[117.437639,23.708903], '南靖县南靖县监测站':[117.358781,24.740708],
 '南靖县县博物馆':[117.379327,24.520742], '平和县平和县气象局':[117.312379,24.381212], '平和县平和县金华小学分校':[117.342032,24.391725], '华安县华安县监测站':[117.548049,25.009608],
 '华安县实验二小':[117.541123,24.998823], '龙海市紫云公园':[117.824811,24.434428], '龙海市海澄中学':[117.861364,24.425511], '龙海市龙海中医院':[117.819576,24.459848],
 '漳州市田丰':[117.694308,24.514353], '漳州市县前直街':[117.645711,24.514336], '漳州市西洋坪路':[117.643926,24.544677], '漳州市九湖':[117.646733,24.479013],
 '漳州市蓝田镇':[117.72109,24.511696], '漳州市漳州三中':[117.675887,24.539442], '顺昌县顺昌实验小学':[117.816822,26.800312], '顺昌县林业技术推广中心':[117.827093,26.789095],
 '浦城县东风水库':[118.477427,27.94475], '浦城县浦城一中':[118.547148,27.925649], '浦城县县特殊学校':[118.547148,27.925649], '光泽县光泽县委':[117.3433,27.547183],
 '光泽县光泽县林业局':[117.353168,27.5562], '松溪县松溪二中':[118.793593,27.547998], '松溪县松溪县环保局':[118.791862,27.527396], '政和县新环保大楼':[118.860502,27.361968],
 '政和县政和二中':[118.877627,27.369352], '邵武市邵武市委党校':[117.480596,27.340321], '邵武市闽北地质队':[117.514301,27.334609], '邵武市邵武市环保局':[117.491304,27.356365],
 '武夷山市天游':[117.954501,27.653747], '武夷山市武夷山一中':[118.038465,27.75956], '武夷山市武夷学院':[118.002337,27.731066], '南平市南平七中':[118.186591,26.631063],
 '南平市南平铝业有限公司':[118.176274,26.614756], '南平市南平市监测站':[118.160821,26.66246], '南平市茫荡山':[118.12549,26.705237], '建瓯市林业推广中心':[118.335675,27.059484],
 '建瓯市建瓯市环保局':[118.327154,27.037248], '建瓯市水西林场':[118.30342,27.036992], '建阳市建阳农工校':[118.039447,27.361247], '建阳市建阳区环保局':[118.130284,27.317861],
 '闽清县黄楮林':[118.709734,26.284565], '闽清县档案馆':[118.867843,26.227311], '闽清县闽清高级中学':[118.882811,26.222494], '永泰县青云山':[119.015449,25.826616],
 '永泰县上马路':[118.944775,25.870286], '永泰县城南小学':[118.958395,25.863722], '福清市石竹湖景区':[119.298457,25.70768], '福清市福清市监测站':[119.370241,25.70557],
 '福清市石竹派出所':[119.335326,25.735825], '福清市江阴工业区':[119.297661,25.454175], '明溪县明溪县环保局':[117.204766,26.366342], '明溪县县宾馆':[117.208581,26.360837],
 '清流县清流县环保局':[116.814189,26.182004], '清流县清流一中':[116.827427,26.184329], '宁化县三明工贸学校':[116.671578,26.274679], '宁化县县第七中':[116.65243,26.264693],
 '大田县文昌':[117.855219,25.700126], '大田县玉田站':[117.845756,25.685627], '尤溪县尤溪实验小学':[118.196897,26.180906], '尤溪县县自来水厂':[118.178485,26.174784],
 '沙县沙县环保局':[117.798485,26.407455], '沙县沙县三中':[117.79228,26.38369], '将乐县将乐县科技局':[117.79228,26.38369], '将乐县县国有林场':[117.477138,26.723129],
 '泰宁县泰宁一中':[117.180954,26.905471], '泰宁县泰宁县总医院住院部':[117.180551,26.893889], '建宁县建宁原县政府':[116.85486,26.839003], '建宁县智华中学':[116.849788,26.826136],
 '三明市荆东':[117.568001,26.201424], '三明市陈大':[117.661641,26.318907], '三明市洋溪':[117.743739,26.313023], '三明市三钢':[117.628612,26.276616],
 '三明市三明二中':[117.633762,26.237522], '三明市三元区政府':[117.656399,26.272321], '永安市林木种苗繁育中心':[117.37178,25.916262], '永安市永安四中':[117.379318,25.98993],
 '永安市永安市监测站':[117.357955,25.976059], '永安市永安市教育局':[117.384779,25.973301], '福州市鼓山':[119.398153,26.064196], '福州市紫阳':[119.330304,26.082254],
 '福州市五四北路':[119.312984,26.116235], '福州市师大':[119.306948,26.030689], '福州市杨桥西路':[119.306948,26.030689], '福州市九龙':[119.31792,25.999624],
 '福州市金井湾':[119.717458,25.488075], '长乐市石燕村':[119.531278,25.989777], '长乐市长乐市政府':[119.529494,25.967454], '长乐市郑和花园':[119.517053,25.957455],
 '福州市省站超级站':[119.295414,26.108579], '莆田市东圳水库':[118.931089,25.489894], '莆田市荔城区仓后路':[119.026135,25.437788], '莆田市莆田市监测站':[119.011566,25.461892],
 '莆田市涵江区六中':[119.128561,25.457717], '莆田市秀屿区政府':[119.111797,25.297522], '仙游县仙游县监测站':[118.68975,25.375482], '仙游县鲤南镇政府':[118.691259,25.34479],
 '霞浦县霞浦县监测站':[120.033184,26.902303], '霞浦县县第三小学':[120.011889,26.88001], '古田县特殊教育学校':[118.771476,26.604368], '古田县玉田中学':[118.744886,26.586147],
 '屏南县闽东电力公司':[118.991909,26.914729], '屏南县屏南县职业中学':[118.973705,26.905656], '寿宁县寿宁县气象局':[119.513456,27.460155], '寿宁县县党校':[119.515259,27.471464],
 '周宁县周宁县环保局':[119.515259,27.471464], '周宁县人社局':[119.348426,27.112958], '柘荣县柘荣县环保局':[119.898538,27.236242], '柘荣县县气象局':[119.906332,27.23525],
 '福安市天湖山庄':[119.660928,27.082439], '福安市阳头办事处':[119.660928,27.082439], '福安市福安市建委':[119.652897,27.100092], '福鼎市太姥山':[120.202111,27.120131],
 '福鼎市监测监控分中心':[120.234919,27.305859], '福鼎市实验小学':[120.224245,27.331658], '平潭综合实验区县政府':[119.813753,25.560271], '平潭综合实验区36脚湖':[119.775413,25.482473],
 '宁德市蕉城南路':[119.537239,26.656775], '宁德市闽东中路':[119.547464,26.668758], '宁德市金涵水库':[119.500653,26.70091], '宁德市宁德市监测站':[119.582509,26.655362],
 '宁德市蕉城区农机局':[119.509334,26.664511], '长汀县长汀一中':[116.359902,25.841792], '长汀县长汀职专':[116.384991,25.851548], '永定县永定区环保局':[116.744912,24.728052],
 '永定县永定二中':[116.727761,24.724831], '上杭县上杭县环保局':[116.42119,25.067334], '上杭县县一中':[116.443101,25.049277], '武平县武平县政府':[116.110714,25.098731],
 '武平县武平一中':[116.097103,25.08679], '连城县连城县职业教育中心':[116.762635,25.732583], '连城县连城县实验小学西城校区':[116.776864,25.699445], '龙岩市龙岩师专':[117.027814,25.125709],
 '龙岩市龙岩市监测站':[117.070055,25.103144], '龙岩市龙岩学院':[117.070055,25.103144], '龙岩市闽西职业技术学院':[117.058022,25.068899], '漳平市漳平市委':[117.425867,25.296684],
 '漳平市漳平二中':[117.435445,25.274389]}



list_a=list(loaction)
list_a=list(loaction.keys())
list_b=list(loaction.values())
pd_a=pd.DataFrame(list_a,columns=['name'])
arr_a=np.array(list_b)
from xpinyin import Pinyin
p=Pinyin()
# p.get_pinyin(list_a[0])
py_la=[]
for i in range(len(list_a)):
    py_la.append(p.get_pinyin(list_a[i],splitter=''))

pd_a['long']=arr_a[:,0]
pd_a['lat']=arr_a[:,1]
pd_a['py_name']=py_la
pd_b=pd_a[['py_name','long','lat']]
pd_b.to_csv(r'G:\thesis\aerosol for no2\raw_data\air_p16_19\zuobiao\zb189.csv')


import pyproj

p1 = pyproj.Proj(init='epsg:32650')
corr=np.zeros((len(arr_a),2))
for i in range(len(arr_a)):
    corr[i,0],corr[i,1]= p1(arr_a[i,0],arr_a[i,1],inverse=False)
pd_a[['utmlon','utmlat']]=corr
pd_a=pd_a.rename(columns={'name':'point'})
te_f1=pd.merge(te_f,pd_a,how='left',on=['point'])
te_f1.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/restor_total1.csv")

"""tif_landscan"""
import gdal,ogr
import numpy as np
import struct

mxn_utm_co=pd_a.drop(pd_a[(pd_a['utmlon']>712375) | (pd_a['utmlat']>3009021)].index)

mxn_utm_co.to_csv(r'G:\thesis\aerosol for no2\raw_data\air_p16_19\zuobiao\zb126.csv')



def data_pro(data_link,point):
    l_data=[]
    src_ds=gdal.Open(data_link)
    gt=src_ds.GetGeoTransform()
    rb=src_ds.ReadAsArray()
    for i in range(len(point)):
        mx,my=point['utmlon'][i], point['utmlat'][i]
        px = int((mx - gt[0]) / gt[1]) #x pixel
        py = int((my - gt[3]) / gt[5]) #y pixel
        l_data.append(rb[py,px])

    return l_data
    

da2018=te_f1[te_f1['year']==2018]
da2018=da2018.drop(da2018[(da2018['utmlon']>712375) | (da2018['utmlat']>3009021)].index)
group=da2018.groupby([da2018['doy'],da2018['py_name']])
b=group.mean()

da2018_a=b.reset_index(level=0)
da2018_b=da2018_a.reset_index(level=0)
da2018_b=da2018_b.drop(['hour'],axis=1)
da2018_b.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/mxn_126_2018.csv")

dempath=r'G:\thesis\aerosol for no2\raw_data\dem\1kmdemutm.tif'#1km
day1=da2018_b[da2018_b['doy']==1]
dem_l=data_pro(dempath,day1)

day1['dem']=dem_l
day2=day1.drop(['doy', 'year', 'co', 'hum', 'no2', 'o3', 'pm10', 'pm2', 'pr',
       'so2', 'tem', 'ws', 'long', 'lat', 'utmlon', 'utmlat',],axis=1)

da2018_c=pd.merge(da2018_b,day2,how='left',on=['py_name'])
da2018_c.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/mxn_126_2018.csv")


def data_pro(data_link,point):
    l_data=[]
    src_ds=gdal.Open(data_link)
    gt=src_ds.GetGeoTransform()
    rb=src_ds.ReadAsArray()
    for i in range(len(point)):
        mx,my=point['utmlon'][i], point['utmlat'][i]
        px = int((mx - gt[0]) / gt[1]) #x pixel
        py = int((my - gt[3]) / gt[5]) #y pixel
        l_data.append(rb[py,px])

    return l_data


#AOD
path=r'G:\thesis\aerosol for no2\raw_data\AOD\re17'
aod=np.zeros(len(da2018_c))
aod_f=os.listdir(path)
for i in range(len(aod_f)):
    point=da2018_c[da2018_c['doy']==1]
    data_link=os.path.join(path,aod_f[i])
    a=data_pro(data_link,point)
    aod[len(a)*i:len(a)*(i+1)]=a
da2018_c['aod']=aod

#aod_conv
path=r'G:\thesis\aerosol for no2\raw_data\AOD\aod_conv'
aod=np.zeros(len(da2018_c))
aod_f=os.listdir(path)
for i in range(len(aod_f)):
    point=da2018_c[da2018_c['doy']==1]
    data_link=os.path.join(path,aod_f[i])
    a=data_pro(data_link,point)
    aod[len(a)*i:len(a)*(i+1)]=a
da2018_c['aod_conv']=aod


#OMI
path=r'G:\thesis\aerosol for no2\raw_data\omi\re1'
aod=np.zeros(len(da2018_c))
aod_f=os.listdir(path)
for i in range(len(aod_f)):
    point=da2018_c[da2018_c['doy']==1]
    data_link=os.path.join(path,aod_f[i])
    a=data_pro(data_link,point)
    aod[len(a)*i:len(a)*(i+1)]=a
da2018_c['omi']=aod/100000000

#omi_conv
path=r'G:\thesis\aerosol for no2\raw_data\omi\omi_conv'
aod=np.zeros(len(da2018_c))
aod_f=os.listdir(path)
for i in range(len(aod_f)):
    point=da2018_c[da2018_c['doy']==1]
    data_link=os.path.join(path,aod_f[i])
    a=data_pro(data_link,point)
    aod[len(a)*i:len(a)*(i+1)]=a
da2018_c['omi_conv']=aod/100000000

##LONG_LAT

format = "GTiff"
driver = gdal.GetDriverByName(format)
aa=np.linspace(1,cols*rows/100,cols*rows)
k1=aa.reshape(cols,rows)


outDataRaster = driver.Create('G:/thesis/aerosol for no2/raw_data/id/not_random.tif', rows, cols, 1, gdal.GDT_Float32)
outDataRaster.SetGeoTransform(dem.GetGeoTransform())
outDataRaster.SetProjection(dem.GetProjection())
outDataRaster.GetRasterBand(1).WriteArray(k1)
outDataRaster.FlushCache()
del outDataRaster

path=r'G:/thesis/aerosol for no2/raw_data/id/not_random.tif'
point=da2018_c[da2018_c['doy']==1]
a=data_pro(path,point)
a=np.tile(a,365)
da2018_c['nrmid']=a

def workofnotday2018(doy):
    
    dicday={1,6,7,13,14,20,21,27,28,34, 35, 41, 46, 47, 48, 49, 50, 51, 52, 56,
     62, 63, 69, 70, 76, 77, 83, 84, 90,91,  95,  96,  97, 104, 105, 111, 112, 119, 120,
     121, 125, 126, 132, 133, 139, 140, 146, 147,153, 154, 160, 161, 167, 168, 169, 174, 175, 181,
     182, 188, 189, 195, 196, 202, 203, 209, 210,216, 217, 223, 224, 230, 231, 237, 238,
     244, 245, 251, 252, 258, 259, 265, 266, 267,274, 275, 276, 277, 278, 279, 280, 286, 287, 293, 294, 300, 301,
     307, 308, 314, 315, 321, 322, 328, 329,335, 336, 342, 343, 349, 350, 356, 357, 364, 365}
    if doy in dicday:
        return 1
    else:
        return 0
wdn=np.zeros((len(da2018_c)))
for i in range(1,366):
    a=np.array(workofnotday2018(i))
    a=np.tile(a,len(da2018_c[da2018_c['doy']==1]))
    wdn[len(da2018_c[da2018_c['doy']==1])*(i-1):len(da2018_c[da2018_c['doy']==1])*i]=a
da2018_c['wdn']=wdn




da2018_c=da2018_c[['py_name','long', 'lat', 'utmlon', 'utmlat', 'doy', 'year', 'co',  'no2', 'o3', 'pm10', 'pm2','so2', 
       'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc', 'rmid', 'nrmid','slope','wdn',"aod_conv",
       'omi_conv']]

da2018_c.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/mxn_126_2018_alvb.csv")


import pandas as pd
import numpy as np
import os
import gdal
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import lightgbm as lgb
import joblib


no_data=da2018_c[['py_name','long', 'lat', 'utmlon', 'utmlat','nrmid', 'no2', 'doy', 
       'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc', 'rmid', 'slope','pop','wdn']]
features, labels=np.array(no_data.iloc[:,7:]),np.array(no_data.iloc[:,6])
train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
# regr=RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
#                       max_features='auto', max_leaf_nodes=None,
#                       min_impurity_decrease=0.0, min_impurity_split=None,
#                       min_samples_leaf=5, min_samples_split=6,
#                       min_weight_fraction_leaf=0.0, n_estimators=150,
#                       n_jobs=None, oob_score=False, random_state=None,
#                       verbose=0, warm_start=False)
regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=2000, 
                       subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                       min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                       colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                       silent=True, importance_type='split')

regr.fit(train_x,train_y)
regr.score(test_x,test_y)
joblib.dump(regr,'G:/thesis/aerosol for no2/model/rmid_pop_828.pkl')
# regr=joblib.load('G:/thesis/aerosol for no2/model/nrmid.pkl')


no_data1=da2018_c[['py_name','long', 'lat', 'utmlon', 'utmlat','nrmid', 'no2', 'doy', 
       'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc',  'slope','aod_conv','no']]
features, labels=np.array(no_data1.iloc[:,7:]),np.array(no_data1.iloc[:,6])
train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
# regr=RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
#                       max_features='auto', max_leaf_nodes=None,
#                       min_impurity_decrease=0.0, min_impurity_split=None,
#                       min_samples_leaf=5, min_samples_split=6,
#                       min_weight_fraction_leaf=0.0, n_estimators=150,
#                       n_jobs=None, oob_score=False, random_state=None,
#                       verbose=0, warm_start=False)

regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=2000, 
                       subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                       min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                       colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                       silent=True, importance_type='split')

regr.fit(train_x,train_y)
regr.score(test_x,test_y)
joblib.dump(regr,'G:/thesis/aerosol for no2/model/rmid8321.pkl')



no_data=da2018_c[['py_name','long', 'lat', 'utmlon', 'utmlat','nrmid', 'no2', 'doy', 
       'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc',  'slope']]
features, labels=np.array(no_data.iloc[:,7:]),np.array(no_data.iloc[:,6])
train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
regr=RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
                      max_features='auto', max_leaf_nodes=None,
                      min_impurity_decrease=0.0, min_impurity_split=None,
                      min_samples_leaf=5, min_samples_split=6,
                      min_weight_fraction_leaf=0.0, n_estimators=100,
                      n_jobs=None, oob_score=False, random_state=None,
                      verbose=0, warm_start=False)
# regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=2000, 
#                        subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
#                        min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
#                        colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
#                        silent=True, importance_type='split')

regr.fit(train_x,train_y)
regr.score(test_x,test_y)
joblib.dump(regr,'G:/thesis/aerosol for no2/model/noid_rf.pkl')







dempath=r'G:\thesis\aerosol for no2\raw_data\dem\1kmdemutm.tif'#1km
dem=gdal.Open(dempath)
demarr=dem.ReadAsArray()
[cols,rows]=demarr.shape
df_data_total=pd.DataFrame()

#AOD
path=r'G:\thesis\aerosol for no2\raw_data\AOD\re17'
aod_f=os.listdir(path)
aod=np.zeros(len(aod_f)*cols*rows)
for i in range(len(aod_f)):
    arr=gdal.Open(os.path.join(path,aod_f[i])).ReadAsArray()
    arr=arr.reshape((cols*rows))
    aod[len(arr)*i:len(arr)*(i+1)]=arr
df_data_total['aod']=aod
#aod_conv
path=r'G:\thesis\aerosol for no2\raw_data\AOD\aod_conv'
aod_f=os.listdir(path)
aod=np.zeros(len(aod_f)*cols*rows)
for i in range(len(aod_f)):
    arr=gdal.Open(os.path.join(path,aod_f[i])).ReadAsArray()
    arr=arr.reshape((cols*rows))
    aod[len(arr)*i:len(arr)*(i+1)]=arr
df_data_total['aod_conv']=aod
#

df_data_total.to_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/predict_data_total_pop.csv")

dempath=r'G:\thesis\aerosol for no2\raw_data\dem\1kmdemutm.tif'#1km
dem=gdal.Open(dempath)
demarr=dem.ReadAsArray()
[cols,rows]=demarr.shape
format = "GTiff"
driver = gdal.GetDriverByName(format)

# regr=joblib.load('G:/thesis/aerosol for no2/model/rmid8321.pkl')
# out_p=r'G:\thesis\aerosol for no2\raw_data\no\test\total_rmid'
for i in range(237,365):
    point=df_data_total[df_data_total['doy']==(i+1)]
    # point=point[[ 'doy','pr','hum','tem','ws','dem','aod','omi','ndvi','osm','lucc','rmid','slope','pop','wdn']]
    point=point[[ 'doy', 'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc', 'slope','pop','wdn']]
    pre=regr.predict(np.array(point))
    pre=pre.reshape((410,340))
    print(pre.min())
    if i <10:
        ik=str(0)+str(0)+str(i)
    elif i<100:
        ik=str(0)+str(i)
    else:
        ik=i
    outDataRaster = driver.Create('G:/thesis/aerosol for no2/raw_data/no/test/train_no_zero_rf/'+'2018'+str(ik)+'.tif', rows, cols, 1, gdal.GDT_Float32)
    outDataRaster.SetGeoTransform(dem.GetGeoTransform())
    outDataRaster.SetProjection(dem.GetProjection())
    outDataRaster.GetRasterBand(1).WriteArray(pre)
    outDataRaster.FlushCache()
    del outDataRaster


# 'doy', 'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc', 'slope','pop','wdn'


out_p=r'G:\thesis\aerosol for no2\raw_data\no\new_nrmid'

regr=joblib.load('G:/thesis/aerosol for no2/model/nrmid8361.pkl')
out_p=r'G:\thesis\aerosol for no2\raw_data\no\new_nrmid'
for i in range(365):
    point=df_data_total[df_data_total['doy']==(i+1)]
    point=point[[ 'doy', 'pr', 'hum','tem', 'ws',  'dem', 'aod', 'omi', 'ndvi', 'osm', 'lucc', 'nrmid', 'slope']]
    pre=regr.predict(np.array(point))
    pre=pre.reshape((410,340))
    if i <10:
        ik=str(0)+str(0)+str(i)
    elif i<100:
        ik=str(0)+str(i)
    else:
        ik=i
    outDataRaster = driver.Create('G:/thesis/aerosol for no2/raw_data/no/new_nrmid/'+'2018'+str(ik)+'.tif', rows, cols, 1, gdal.GDT_Float32)
    outDataRaster.SetGeoTransform(dem.GetGeoTransform())
    outDataRaster.SetProjection(dem.GetProjection())
    outDataRaster.GetRasterBand(1).WriteArray(pre)
    outDataRaster.FlushCache()
    del outDataRaster




#no_id

import pandas as pd
import numpy as np
a=pd.read_csv(r'G:\thesis\aerosol for no2\raw_data\air_p16_19\restore\mxn_126_2018_alvb.csv')

city=a.drop_duplicates(['py_name'], keep='last')
d1=pd.DataFrame()
d1['name']=city['py_name']
d2=[]
for i in range(len(city)):
    b=a[a['py_name']==city['py_name'].iloc[i]]
    c=b.corr()
    d2.append(c['no2']['aod'])
d1['corr']=np.array(d2)

##AAAS的意见
'''

tr_data=no[no['mon']==1]

ts_data=no[(no['mon']==2]) & (no['doy']==32)]

train_x, train_y=np.array(tr_data.iloc[:,1:]),np.array(tr_data.iloc[:,0])
test_x,test_y=np.array(ts_data.iloc[:,1:]),np.array(ts_data.iloc[:,0])

regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=10, max_depth=-1, learning_rate=0.1, n_estimators=4000, 
                       subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                       min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                       colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                       silent=True, importance_type='split')
regr.fit(train_x,train_y)
print(regr.score(test_x,test_y))


import time
t_a=time.time()

# regr=RandomForestRegressor(n_estimators=2000,n_jobs=-1)

regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=10, max_depth=-1, learning_rate=0.1, n_estimators=4000, 
                       subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                       min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                       colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                       silent=True, importance_type='split')

# regr=lgb.LGBMRegressor(boosting_type='dart', num_leaves=4000, max_depth=-1, learning_rate=0.1, n_estimators=2000, 
#                         subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
#                         min_child_weight=0.001, min_child_samples=100, subsample=1, subsample_freq=0, 
#                         colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
#                         importance_type='split')
regr.fit(train_x,train_y)
t_b=time.time()
print(t_b-t_a)
print(regr.score(test_x,test_y))

#boosting_type='gbdt', num_leaves=10, max_depth=-1, learning_rate=0.1, n_estimators=4000   R2=0.8569830726481612
#boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=2000   R2=0.8525020859982689
'''
import pandas as pd
import numpy as np
import os
import gdal
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import lightgbm as lgb
import math
da2018_c=pd.read_csv(r"G:/thesis/aerosol for no2/raw_data/air_p16_19/restore/mxn_126_2018_alvb_wjsp.csv",index_col=0)

no=da2018_c[['no2','mon','doy','hum','pr','tem','ws', 'dem', 'lucc', 'aod','omi', 'pop',
             'slope','ndvi', 'osm', 'rmid', 'wdn','aod_conv','omi_conv' ]]

def RMSE(a,b):
    error=[]
    for i in range(len(a)):
        error.append(a[i]-b[i])
    sqerror=[]
    for j in error:
        sqerror.append(j**2)
    RMSE=math.sqrt(sum(sqerror)/len(sqerror))
    return RMSE

features, labels=np.array(no.iloc[:,1:]),np.array(no.iloc[:,0])
train_x,  test_x, train_y,test_y = train_test_split(features, labels,test_size=0.1, random_state=39)
regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=10, max_depth=-1, learning_rate=0.1, n_estimators=4000, 
                       subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                       min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                       colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                       silent=True, importance_type='split')
regr.fit(train_x,train_y)
print(regr.score(test_x,test_y))

#AAAS1 上一月月份预测下一月1日

m_1=[1,2,3,4,5,6,7,8,9,10,11]
d_1=[32,60,91,121,152,182,213,244,274,305,335]

for i in range(11):
    tr_data=no[no['mon']==m_1[i]]
    
    ts_data=no[(no['doy']==d_1[i])]
    
    train_x, train_y=np.array(tr_data.iloc[:,1:]),np.array(tr_data.iloc[:,0])
    test_x,test_y=np.array(ts_data.iloc[:,1:]),np.array(ts_data.iloc[:,0])
    
    regr=lgb.LGBMRegressor(boosting_type='gbdt', num_leaves=10, max_depth=-1, learning_rate=0.1, n_estimators=4000, 
                           subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, 
                           min_child_weight=0.001, min_child_samples=20, subsample=1.0, subsample_freq=0, 
                           colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, random_state=None, n_jobs=-1, 
                           silent=True, importance_type='split')
    regr.fit(train_x,train_y)
    pre_y=regr.predict(test_x)
    print('R2: ',regr.score(test_x,test_y))
    print('RMSE: ', RMSE(pre_y,test_y))

