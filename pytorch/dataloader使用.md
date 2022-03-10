# dataloader使用

batch_size:一次处理的文件数(batch_size=4)(batch_size=64)

shuffle:取数据的顺序（shuffle=True时顺序不同）（shuffle=False时顺序相同)

num_workers

drop_last：最后一次不够，true时舍弃，False时不舍弃（drop_last=True)(drop_last=False)