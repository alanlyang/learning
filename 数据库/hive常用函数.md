## hive中的分组与组内排序
    语法：  
        - row_number() over (partition by 字段a  order by 计算项B desc) rank 
        - rank 为排序的别名
        - partition by: 类似hive的建表、分区的意思
        - order by ： 排序，默认是升序，加desc为降序
        - 这里是按a分区，对计算项b进行降序排列
        - row_number是针对每个partition后的分组进行排序打标记

    例子：取top10品牌下，各自的top10渠道
        select a.* from (select "品牌"，"渠道"，sum/count() as num , row_number() over (partition by "品牌" order by num desc) rank from "表名" where 条件 group by "品牌"，"渠道") a having a.rank <= 10

## where 和 hiving 的区别
    相同点: 
        - 都是限定返回的数据集合
        - 在一个sql语句中可以有where子句和having子句
    不同点：
        - where
          - 在where 子句中不能使用聚组函数
          - where 子句的作用时在对查询结果进行分组前，将不符合条件的行丢掉
          - where 语句在Group By之前，Hql会在分组之前计算where语句
        - having
          - having语句可以使用聚组函数
          - 查询语句 select、group by 、having子句时聚组函数唯一出现的地方
          - Having语句在Group by 语句之后，分组之后计算having
          - 当在group by 中使用having子句时，查询结果中只返回满足having条件的组
          - 

    
## concat 、concat_ws
    concat:
        - 字符串拼接函数
        - 主要用于将输出的字段与其他字段拼接在一起
        - 输入类型必须为字符串类型
    concat_ws:
        - 应用与输出字段用相同字符分割的场景
        - concat_ws("|", s1, s2, s3)
        - 输入类型必须为字符串类型

## collect_list 、 colect_set
    - 都是将分组中的某列转为一个数组返回
    - collect_list不去重而collect_set去重
    - 和group by 结合使用

## if 语句
    if(boolen 条件， value True, value False or NUll)
    如果条件为真，则返回True对应的字段, 否则返回Flase对应的字段

## Union ALL 
    将筛选出的结果进行合并，不会进行去重
    union会进行去重

    效率上 union all 会快很多