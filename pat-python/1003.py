"""
1003. Emergency
输入：
    第一行  N : 城市量  M : 道路条数 C1: 当前所在节点 C2: 目标节点
    第二行 每个城市的救援队数量
    接下来的M行 是城市间的道路图的邻接矩阵，每行三个数字分别表示 c1, c2, L(道路长度) （两个城市之间至少有一个道路）
输出：
    一行两个值： c1,c2之间最短的路径的数量， 最多能聚集的救援队， 空格分割
"""

"""
题目解析：深度遍历优先，Dfs
"""

if __name__ == "__main__":
    # 初始信息
    N,M,C1,C2 = map(int, input().split(" "))
    # 救援队数量
    rescue_num = map(int, input().split(" "))
    # 道路图信息
    road_map = [[]] * M
    for i in range(M):
        start, end, length = map(int, input().split(" "))
        road_map[start].append((end, length))
        road_map[end].append((start, length))
    # 构建二维矩阵
    





