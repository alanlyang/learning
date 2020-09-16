## 简介
Eigen是C++的一个开源模板库，支持线性袋鼠计算，矩阵和矢量计算，数值分析及其相关的算法  
Eigen是tensorflow高维计算层的主要技术栈 
tensorflow中大多数的kernel都是基于Eigen::Tensor来实现的  

Eigen只包含头文件，因此不需要进行编译（只需要使用#include即可） 
Eigen的默认安装位置为 /usr/include/eigen3  

## Eigen库的模块及头文件
Eigen库被分为多个功能模块，每个模块都有自己相对应的头文件。 
Dense模块整合了绝大部分的模块  

Core: Matrix和Array类， 基础的线性代数运算和数组操作 
Geometry: 旋转、平移、缩放、2D、3D的各种变换
LU : 求逆，行列式， LU分解
Cholesky: LLT和LDLTCholesky分解
Householder: 豪斯霍尔德变换，用于线性代数计算
SVD: SVD分解
QR： QR分解
Eigenvalues: 特征值，特征向量分解
Sparse: 稀疏矩阵的存储和一些基本的线性运算
Dense: 包含了Core/Geometry/LU/Cholesky/SVD/QR/Eigenvalues模块
Eigen: 包括Dense和Sparse（整个Eigen库）