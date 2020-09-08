### redis数据类型(Remote Dictionary Server)
    redis支持五种数据类型：
        - String(字符串)
            - redis的基本类型，一个key对应一个value
            - string对二进制安全，可以包含任意类型数据，如图片或者序列化对象
            - 一个Key最大能存储512M
            - 使用get 和 set 来进行取或者赋值操作
        - hash(哈希类型)
            - 键名对集合
            - 是一个string类型的field和value的映射表
            - 尤其适合存储对象
            - 相当于Python的字典类型
            - 使用HMSET 和 HGETALL 系列来进行操作
            - 最多可以存储2的32次方个键值对
        - List(列表)
            - 简单字符串列表
            - 按照插入顺序排序
            - 最多可以存储2的32次方个元素
        - Set(集合)
            - string类型的无序集合
            - 内部通过hash表实现
            - 添加、删除、查找复杂度都是o(1)
            - 使用sadd添加数据，smembers可以查看数据
            - 最大成员数为2的31次方
        - zset(sorted set：有序集合)
            - 同set一样，是string的集合
            - 不允许同样的元素存在
            - 但是每个元素都会关联一个double类型的分数，redis根据这个分数来对集合中的元素从小到大排序
            - 使用zadd key score momber形式来添加元素
  
### 参考网址
        https://www.redis.com.cn/redis-transaction

### redis事务
    redis事务用于帮助用户在一个步骤中执行多个命令
    执行有两个属性
        - 事务中的所有命令都作为一个隔离操作顺序执行，无法在执行redis事务期间由另一个客户端发起请求
        - redis事务是原子的，要么所有的命令都执行，要么都不执行
    
    可以通过Multi命令启动呢事务，然后传递需要在事务中执行难的命令列表，之后整个事务由exec命令执行

### redis流水线 Piplining
    redis是一个支持请求/ 响应协议的tcp服务起，在redis中，请求分两万步炜岸城
    1、客户端通常以阻塞方式向服务器发送命令
    2、服务器处理该命令并将响应发送回客户端

    流水线操作有助于客户端向服务端发送多个请求，而无需等待，最后只需一部即可读取回复
    柳树先操作的主要优点式提高redis的性能，由于多个命令同时执行，它极大的提高了协议性能

### redis分区
    分区用于将redis数据拆分为多个redis实例，以便每个实例仅包含一部分密钥
    通常用于大型数据库

    分区类型
        1、范围分区
            - 通过将对象的范围映射到特定的redis实例来完成
        2、哈希分区
            - 在散列分区中，散列函数用于将密钥转为数字，然后将数据存储在不同的redis实例中

    分区的优缺点
        优点
            1、有助于使用多台计算机的集体内存
            2、利于将计算能力拓展到多个核心和多个计算机
        缺点
            1、分区不支持具有多个键的操作
            2、分区不支持具有多个密钥的事务
            3、使用分区时数据处理更加复杂
            4、添加和删除容量可能很复杂
  
### mac安装redis
    brew install redis 即可

### redis相关操作
    1、通过shutdown关闭redis-server
    2、redis-server用来获取服务器信息、统计信息和其他特征

### jedis关键参数设置建议
    maxTotal: 资源池中的最大连接数, 默认值是 8 
    maxIdle： 资源池允许的最大空闲连接数， 默认指 8
    minIdle: 资源池确保的最少空闲连接数， 默认 0

    maxTotal:
        需要考虑的因素较多如：
        - 1、业务希望的redis并发量
        - 2、客户端执行命令时间
        - 3、redis资源，例如nodes（应用个数）* maxTotal 不能超过redis的最大连接数
        - 4、资源开销，例如虽然希望控制空闲连接，但又不希望因为连接池中频繁的释放和创建链接造成不必要开销
  
    maxIdle
        - 实际上才是业务需要的最大连接数，maxTotal是为了给出余量，因此maxIdle不要设置的过小
        - 连接池最佳的性能是 maxTotal = maxIdle
  
### 连接redis/redis连接池
```scala

import redis.clients.jedis.{HostAndPort, JedisCluster, JedisPoolConfig}
import scala.collection.JavaConversions._
import redis.clients.JedisPool

// 配置连接池
val conf = new JedisPoolConfig
// 设置最大连接数等参数
conf.setMaxIdle(4)
conf.setMaxTotal(4)
// 连接redis
val pool = new JedisPool(conf, "localhost", 6379)
// 如果时redis集群需要使用JedisCluster

// 获取redis链接实例
val redis = pool.getResource()

// 然后就可以对redis进行相关的操作了

```



