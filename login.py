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

