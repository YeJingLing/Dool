def func():
   result = type(input("请输入类型："))
   if result == "string":
       set name "zhangsan"
       del name
       set name "zhaosi"
       set name "waawa"
   elif result == "hash":
        hset person name "名字"
        hset person age "年龄"
        hdel person name
        hset person name "新值"
        hget person name
        hgetall person
    elif result == "list":
        lpush k 1 2 3  4
        lrange k 0 -1
        lrem k 0 1
        lset k 2 "A"
        linsert k before 1 "B"
        linsert k after 2 "W"
        ltrim k 0 3
    elif result == "set":
        sadd hello kitty
        sadd hi kitty
        srem hi kitty
        smembers hello hi
    elif result == "zset":
        zadd k 1 hello 2 hi 3 kitty 4 nihaio 5 v 6
        zrem k v
        zrange k 0 -1
        zscore k v
    else:
        print(result)
func()




class input_data(objet):
    result =  input("请输入数据")

    def __init__(self,num,string,set,zset,list,hash):
        self.num = num
        self.string = string
        self.set = set
        self.zset = zset
        self.list = list
        self.hash = hash

    def num()：
        print(result)
    def string():
        set name myname
        del name
        set name yourname
        get name
        append name "是我"
    def set():
        sadd ha hello
       sadd mi zi
        smembers ha
        srem ha zi
    def zset():
        zadd ht hhaaa k v
        zadd he 1 heh 2 hhhhh 4 hhhhhhsss 3
        zrem zrange k 0 -1
        zsocre k v 
    def list():
        lpush k 1 2 3 78 4 56 99 7
        lrange k 0 -1
        lset k 2 "a"
        linsert 4 before 56 "u"
        ltrim k 0 1
        lrem k 1 5 
    def hash():
        hset he name "小明"
        hset he age "年审"
        hset he name "喵喵"
        hgetall he
        hdel he age
        hget he name
        
if __name__ =="__main__":
   a= input("输入：")



input_data()

