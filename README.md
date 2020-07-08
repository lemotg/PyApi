PyApi接口自动化测试框架

基于Request+unittest实现接口自动化



Python版本与依赖库：
- python3.5+ :https://www.python.org/
- Requests : https://github.com/kennethreitz/requests

目录介绍：
* 测试报告利用HTMLTestRunner生成，存放于report目录
* 测试用例单独编写为case_xxx.py文件,存放于case目录
* 运行入口 run_test.py
* common目录存放一些共用的方法
* config目录存放配置文件和读取方法
* logs和report目录分别存放生成的日志和报告

感谢：
* 感谢虫师大佬的书籍及博客帮助：https://github.com/defnngj
* 感谢TDanny大佬的帮助：https://github.com/DDDDanny
