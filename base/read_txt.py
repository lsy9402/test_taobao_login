def read_txt(number = 0):
    # 打开txt文件流
    with open('../page/data.txt', 'r', encoding='utf-8') as f :
        # 通过文件流调用读取的方法读取数据
        datas = f.readlines()
        # 新建列表保存单行数据
        lines = []
        #遍历
        # print(f)
        for data in datas:
            # strip()去除字符串前后回车 split()使用指定符号分割字符串并以列表格式返回分割前后的数据
            lines.append(data.strip().split(','))
        # 返回数据  从下标number(默认为0)开始返回
        return lines[number:]