高级动态规划：
动态规划解题的一般思路：
    1. 将原问题分解为子问题
    把原问题分解为若干个子问题，子问题和原问题形式相同或类似，只不过规模变小了。子问题都解决，原问题即解决(数字三角形例）。
    子问题的解一旦求出就会被保存，所以每个子问题只需求 解一次。
    2.确定状态
    在用动态规划解题时，我们往往将和子问题相关的各个变量的一组取值，称之为一个“状 态”。一个“状态”对应于一个或多个子问题， 所谓某个“状态”下的“值”，就是这个“状 态”所对应的子问题的解。
    所有“状态”的集合，构成问题的“状态空间”。“状态空间”的大小，与用动态规划解决问题的时间复杂度直接相关。 在数字三角形的例子里，一共有N×(N+1)/2个数字，所以这个问题的状态空间里一共就有N×(N+1)/2个状态。
    整个问题的时间复杂度是状态数目乘以计算每个状态所需时间。在数字三角形里每个“状态”只需要经过一次，且在每个状态上作计算所花的时间都是和N无关的常数。
    3.确定一些初始状态（边界状态）的值
    以“数字三角形”为例，初始状态就是底边数字，值就是底边数字值。
    4. 确定状态转移方程
     定义出什么是“状态”，以及在该“状态”下的“值”后，就要找出不同的状态之间如何迁移――即如何从一个或多个“值”已知的 “状态”，求出另一个“状态”的“值”(递推型)。状态的迁移可以用递推公式表示，此递推公式也可被称作“状态转移方程”。


字符串算法：
一、判断两个字符串是否包含相同的内容
1.巧用数组下标实现，把用字符的ASCII码值当作下标，记录出现的字符，然后对两字符串进行遍历
2.使用键值对TreeMap、HashMap或HashTable进行登记式记录，这个适用于文字等复杂的字符串

二、判断一个字符串是否为另个一字符串的子集
1.数组下标记录实现
2.键值对记录实现

三、去除字符串种出现k次的字符
1.普通实现
2.正则表达式替换实现
