## pd.get_dummies
    get_dummies是利用pandas实现one-hot encode的方式

## pd.Series
    pandas 主要有两种数据结构 Series 和 DataFrame
    Series 是一种类似于一维数组的对象，它由一组与之相关的数据标签组成（即索引）
    pd.Series(["A", "B"]) 返回的每行为 （index , value） 即索引在左，值在右
## pd.merge
    merge提供了一种类似与SQL的内存链接操作
    参数：
        left_on 类似与left join
        right_on
        left_index/right_index: 如果为True, 则以index作为对齐的key
        how: 数据融合的方式
        sort: 根据dataframe合并的keys按字典序排序。默认true, 如果置为false，则可以提供性能

## pd.loc
    loc通过index中的具体指来取行数据
    data.loc['a'] 即取索引为'a'的行
    data.loc["a", "b"] 取'a'行 'b'列的值

    loc允许对df进行类似坐标的操作，只不过坐标为行或者列的别名