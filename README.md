# datasetFactory

自用简易数据集格式转换工具

需要安装的包 re（正则表达式）

```
pip install re
```

## 使用方法

将.csv文件放到同目录下，运行main.py，输入csv文件名(若名字为annotations.csv可直接回车不需要输入)，程序自动运行退出，生成labels文件夹，其中为转换完成的labels文件夹下的对应相应图片的标注数据。
其中，不同种类的血细胞被转换为0和1的label值，类似是否有mask的人脸。
