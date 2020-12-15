Config = {
    'num_classes': 21,
    #-----------------------------------------------------------------#
    #   min_dim有两个选择。
    #   一个是300、一个是512。
    #   这里的SSD512不是原版的SSD512。
    #   原版的SSD512的比SSD300多一个预测层；
    #   修改起来比较麻烦，所以我只是修改了输入大小
    #   这样也可以用比较大的图片训练，对于小目标有好处
    #   当min_dim = 512时，'feature_maps': [64, 32, 16, 8, 6, 4]
    #   当min_dim = 300时，'feature_maps': [38, 19, 10, 5, 3, 1]
    #-----------------------------------------------------------------#
    'min_dim': 300,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    # 'min_dim': 512,
    # 'feature_maps': [64, 32, 16, 8, 6, 4],
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [30, 60, 111, 162, 213, 264],
    'max_sizes': [60, 111, 162, 213, 264, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}