# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import  filedialog
import os
import shutil
import pyodbc
import time
from datetime import datetime,timedelta


root=tk.Tk()
select_path=tk.StringVar()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    filepath = "D:\\gdjc_data\\project_num.txt"
    filepath1 = "D:\\gdjc_data\\road_num.txt"
    f = open(filepath, 'r')
    file_content = f.read()
    project_num = file_content
    f = open(filepath1, 'r')
    file_content = f.read()
    road_num=file_content
    print(project_num)
    print(road_num)
    filepath3="D:\\gdjc_data\\video"
    if os.path.exists(filepath3):
        filepath4 = os.path.join(filepath3, project_num+"+"+road_num)
        if os.path.exists(filepath4):
            a=1
        else:
            os.mkdir(filepath4)
    else:
        os.mkdir(filepath3)
        filepath4 = os.path.join(filepath3, project_num +"+"+ road_num)
        os.mkdir(filepath4)

    file_path5 = filedialog.askopenfilenames()
    select_path.set('\n'.join(file_path5))
    print(file_path5)
    #root.mainloop()

    for i in range(0,len(file_path5)):
        source_file=file_path5[i]
        target_folder=filepath4
        shutil.copy(source_file,target_folder)
    path = "D:\gdjc_data\Database3.accdb"
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path)
    cursor1 = conn.cursor()
    cursor1.execute("select max(ID) from VideoInformation")
    data1 = cursor1.fetchall()
    max_value = data1[0]
    maxvalue=max_value[0]+1
    cursor1.close()
    files=[os.path.join(filepath4,file) for file in os.listdir(filepath4)]
    for file in file_path5:
        maxvalue=maxvalue+1
        file_base_name=os.path.basename(file)
        file_time=time.gmtime(os.path.getmtime(file))
        file_time_str=time.strftime("%Y-%m-%d",file_time)

        #保存记录
        cursor2=conn.cursor()
        #str="'"+maxvalue+"'"
        str1="'"+str(maxvalue)+"'"
        str1=str1+",""'"+file_base_name+"'"
        str1=str1+","+"'"+file_time_str+"'"
        str1=str1+","+"'"+filepath4+"\\"+file_base_name+"'"
        print(str1)
        str1=str1+","+"'"+road_num+"'"
        cursor2.execute("insert into VideoInformation(VideoNum,VideoName,VideoDate,VideoPath,RoadNum) VALUES ("+str1+")")
        cursor2.commit()
        cursor2.close()


    #cursor1.execute("select * from ProLnfSheet where ProNum=" + "'" + golbal_var.project_num + "'")
    #data1 = cursor1.fetchall()
    #if len(data1) > 0:
        #for row1 in data1:
           # project_name = row1.ProName
    #else:
        #print("该项目不存在")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
