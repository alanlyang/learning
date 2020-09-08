## HBase简介
    - 全称: Hadoop Database
    - 建立于Hadoop 文件系统之上
    - 分布式面向列的数据库， noSql
    - HDFS为Hbase提供可靠的底层数据存储服务，MapReduce为Hbase提供高性能计算能力，ZooKeeper为Hbase提供稳定服务和Failover机制
    - Hbase是一个通过大量廉价机器解决海量数据的告诉存储和读取的分布式数据库解决方案
    - Hbase可与HDFS互通
  
## Hbase和HDFS
    HDFS适用于存储大容量文件的分布式文件系统，不支持快速单独记录查找
    Hbase建立在HDFS之上，提供较大表的快速查找，Hbase内部使用Hash表和提供随机接入，并且存储其索引，可对HDFS文件进行快速查找

### Hbase存储机制
    Hbase是一个面向列的数据库，在表中由行排序
    表模式定义只能时键值对,一个表可以有多个列族，每一个列族都可以有任意数量的列。后续列的值连续的存在磁盘上.
    表中的每个单元格都具有时间戳
    
    总之，在HBase中
        - 表是行的集合
        - 行时列族的集合
        - 列族时列的集合
        - 列时键值对的集合

### Hbase相关的概念
    rowkey的概念和mysql的主键完全一样，Hbase使用rowKey来唯一的区分某一行的数据

    HBase只支持三中形式的查询
        - 1、基于rowkey的单行查询
        - 2、基于rowkey的范围扫描
        - 3、全表扫描

    rowkey的设计对HBase的性能影响非常大，设计时需要兼顾基于rowkey的单行查询，也要兼顾基于rowkey的范围查询

    rowkey可以时任意的字符串（最大长度64kb, 实际应用中一般为10-100bytes, 最好是16. 在Hbase内部,rowkey保存为字节数组，Hbase会对表中的数据按照rowkey排序）

    列族： 
        - Hbase通过列族划分数据的存储，列族可以包含任意多的列，实现灵活的数据存取，
        - 列族由一个一个的列组成
        - Hbase表创建的时必须指定列族
        - HBase列族不是越多约好，推荐最好小于或者等于3，通常使用一个即可


    TimeStamp
        - TimeStamo时Hbase实现多版本的关键，在Hbase中使用不同的timeStamp标识相同rowkey行对应的timestamp
        - 如果用户没有指定对应的timestamp,Hbase会自动的添加一个timeStamp,timeStamp和服务器时间保持一致
  
    单元格(cell)
        - 由{rowkey, column, version}确定的唯一单元
        - cell中数据没有类型，全部时字节码形式存储
        - 在cell中，不同版本的数据按照时间倒序排序，即最新的数据排在最前面
        - 为避免数据存在过多版本造成的管理负担，Hbase提供了两种数据版本回收方式
          - 1、保存数据的最后n个版本
          - 2、保存数据最近一段时间内的版本，设置数据的生命周期TTL

    Region
        - region类似于关系型数据库的分区
        - Hbase会将一个大表的数据，基于rowkey的不同范围分配到不同的Region中，每个region负责一定范围的数据访问和存储


### Hbase特点
    1、海量存储，支持PB级别的存储，能够在百毫秒内返回数据
    2、列族存储
    3、易于拓展
    4、并发性强
    5、使用场景
        - 适用于海量数据存储和准实时查询，Hbase能够在百毫秒内实现上百亿数据的查询
        - Hbase只有在还海量数据的时候才能发挥良好性能，如果只是在百万或者千万数据，mysql实现完全可以
        - 适用于查询简单，不涉及复杂关联的环境

### Hbase结构
    在Hbase中，Region被列族垂直分为stores， Stores被存储在HDFS上
    - 依赖于HDFS做底层存储
    - 依赖于MapReduce做数据计算
    - 依赖于zookeeper做服务协调

    Hbase主要由三个部分组成
      - 1、主服务器
          - 分配给区域服务器，并在zookeeper的协助下完成任务
            - 处理跨区域的服务器的负载均衡
            - 通过判断负载均衡维护集群状态
            - 负责模式变化和其他元数据操作
      - 2、区域服务器
            - 与客户端进行通信并处理数据相关操作
            - 句柄读写所有地区的请求
            - 决定区域的大小
      - 3、客户端库
