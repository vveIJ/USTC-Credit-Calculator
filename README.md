# USTC Credit Calculator

## 简介

中科大学分计算小工具 ( 基于Python ) , 支持本科生 ( 研究生尚未测试 )

## 运行

1. `pip install requests lxml easyocr` ;
2. 修改 `config.py` 中的相关设置 ;
3. 在终端命令行工具 ( 如 `Powershell` ) 中运行 `main.py` .

示例输出 :

```plaintext
Captcha recognized: 0000
学号: PB00000000
已选择课程:
0.0 - course A
0.0 - course B
0.0 - course C
总学分: 0.0
```

## 致谢

由 [@yusanshi](https://github.com/yusanshi "https://github.com/yusanshi") 制作的 [中科大教务系统刷课 Python 小脚本](https://github.com/yusanshi/USTC-choose-course "https://github.com/yusanshi/USTC-choose-course") 为本项目建立了完整的框架, 并完成了大部分代码实现.
