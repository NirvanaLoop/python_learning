# Python 课程资源库

这个仓库是一个面向教学与自学的 Python 课程资料集合，内容覆盖：

- Python 基础语法与面向对象
- Jupyter Notebook 课堂讲义
- 游戏化项目实践
- 命令行与 Web 小项目
- 大模型、智能体、微调与部署专题资料

仓库里既有可以直接运行的项目，也有适合课堂讲解的 Notebook、Markdown 教案、PDF / DOCX 资料和外部网页入口。

## 仓库结构

```text
python-course/
├── README.md
├── 教学主题快速参考.md
├── python/
├── 五子棋/
├── 贪吃蛇/
├── 个人记账系统/
├── 大模型/
└── pic/
```

## 主要内容

### 1. `python/` 基础课程与讲义

这一部分是 Python 入门到进阶的主课程区，当前包含：

- `Lesson1.ipynb`
  - 程序与 Python 基础
  - 变量、类型、输入输出、注释
- `Lesson2.ipynb`
  - 条件语句
  - 循环、`break` / `continue`
  - 成绩管理等练习示例
- `Lesson3.ipynb`
  - 列表、元组、集合、字典
  - 数据结构对比与示例
- `Lesson4.ipynb`
  - 函数定义、参数、返回值
  - 综合函数练习
- `Lesson5.ipynb`
  - 文件读写
  - 异常处理
- `Lesson6.ipynb`
  - 进阶课程 Notebook（仓库中存在，可作为后续课程入口）
- `面向对象基础教程（一）.ipynb`
  - 面向对象概念
  - 类、对象、类属性、实例属性
  - 封装、继承、多态示例
- `面向对象基础教程（二）.ipynb`
  - 初始化函数、析构函数
  - 继承、方法重写、多态、访问控制
- `hello_world.py`
  - 一个带字符逐个输出效果的入门示例
- `test.py`
  - 四则运算函数综合练习
- `github教程.md`
  - 一个外部网页入口
- `Python课程目录.docx`

#### `python/Python/Python-master/Python-master/`

这是随仓库一起保存的一套较完整的 Markdown 教程库，适合补充阅读。内容包括：

- Python 入门基础
- 代码规范
- 函数、迭代器、生成器
- 面向对象
- 模块与包
- 魔术方法、枚举、元类
- 线程与进程
- 正则表达式
- Django 入门
- Linux 与一些补充资料

如果希望按文章系统阅读，可以从这里开始：

- `python/Python/Python-master/Python-master/README.md`
- `python/Python/Python-master/Python-master/SUMMARY.md`

### 2. `五子棋/` Notebook 项目

这一部分是五子棋教学资源，适合讲解图形界面、事件处理和游戏逻辑。

- `五子棋教学.ipynb`
  - 从绘制棋盘开始
  - 玩家落子
  - 胜负判断
  - 简单 AI 对手
  - 项目优化建议
- `五子棋弹窗版.ipynb`
  - 弹窗式图形交互版本
- `五子棋ipycanvas版.ipynb`
  - 基于 `ipycanvas` 的交互版本

### 3. `贪吃蛇/` Pygame 项目

这是仓库里最完整的代码型项目之一，适合做课堂项目实战。

当前代码结构：

- `snake_game.py`
  - 程序入口
  - 启动时可选择 `player` 或 `ai` 模式
  - 可设置胜利分数
- `game.py`
  - 游戏主循环
  - 绘制、事件处理、计分、胜负判断
- `snake.py`
  - 蛇的移动、转向、增长、碰撞检测
- `food.py`
  - 食物刷新逻辑
- `snake_ai.py`
  - `SimpleSnakeAI`
  - `SafeSnakeAI`，包含 BFS 安全寻路思路
- `config.py`
  - 窗口大小、网格、颜色、默认胜利分数
- `贪吃蛇教学.md`
  - 配套教学讲义

适合讲解的知识点：

- 模块化拆分
- 游戏循环
- 坐标与网格系统
- 状态更新与碰撞检测
- 简单 AI 与 BFS 路径搜索

### 4. `个人记账系统/` 命令行 + Flask 小项目

这是一个更偏业务场景的小项目，适合初学者从“课堂知识”过渡到“完整应用”。

当前包含：

- `main.py`
  - 命令行菜单程序
  - 支持收入 / 支出录入、分类查询、摘要统计
- `account.py`
  - 账户管理类
  - JSON 持久化
  - 汇总统计
- `transaction.py`
  - 单条交易记录对象
- `web_app.py`
  - Flask Web 版本入口
- `templates/index.html`
  - Web 页面模板
- `static/style.css`
  - 简单样式
- `data/transactions.json`
  - 示例数据文件
- `requirements.txt`
  - 当前依赖主要是 `Flask`
- `README.md`
  - 子项目说明
- `使用示例.md`
  - 使用流程示例

适合讲解的知识点：

- 面向对象建模
- JSON 文件读写
- 列表 / 字典统计
- 命令行交互
- Flask 基础 Web 开发

### 5. `大模型/` AI 专题资料

这一部分更偏课程资料和专题阅读，主要不是代码项目，而是教学讲义与参考资料。

当前文件包括：

- `大模型微调技术课程大纲.md`
  - 从理论到实践的大纲式课程资料
  - 覆盖全参数微调、LoRA、Adapter、Prompt-based 方法、数据工程、评估与部署
- `大模型部署实践.md`
  - Hugging Face、ModelScope、vLLM、OpenAI API、Docker、K8s、云平台等部署主题
- `《零代码玩转 AI 应用：小白也能轻松上手的开发工具指南》.md`
  - 面向非技术或低代码场景的 AI 工具选型资料
- `教案网页合集.md`
  - 多个外部网页入口
- `DeepSeek实践.docx`
- `AI智能体：从理解到实操.pdf`
- `大模型与计算平台.pdf`
- `大模型微调技术的理论和实践.pdf`

适合用作：

- AI 方向专题课
- 教师备课资料
- 工具选型与案例讨论

### 6. 顶层辅助资料

- `教学主题快速参考.md`
  - 对课程主题、难度、课时和教学方向的快速梳理
- `pic/`
  - 当前目录存在，但没有发现实际文件

## 快速开始

这个仓库不是单一 Python 包，而是一个课程资料集合。通常按“项目”或“子目录”单独使用。

### 运行贪吃蛇

```bash
cd 贪吃蛇
pip install pygame
python snake_game.py
```

### 运行个人记账系统命令行版

```bash
cd 个人记账系统
python main.py
```

### 运行个人记账系统 Web 版

```bash
cd 个人记账系统
pip install -r requirements.txt
python web_app.py
```

默认访问：

```text
http://127.0.0.1:5000/
```

### 打开 Notebook 课程

```bash
pip install notebook jupyter
jupyter notebook
```

然后在浏览器中打开：

- `python/` 下的各个 `Lesson*.ipynb`
- `python/面向对象基础教程（一）.ipynb`
- `python/面向对象基础教程（二）.ipynb`
- `五子棋/` 下的各个 Notebook

## 建议学习路径

### 路线 A：零基础入门

1. 学 `python/Lesson1` 到 `Lesson5`
2. 跑通 `python/hello_world.py` 和 `python/test.py`
3. 学 `面向对象基础教程（一）`、`（二）`
4. 实战 `个人记账系统/`
5. 进阶到 `贪吃蛇/`

### 路线 B：项目驱动教学

1. 用 `个人记账系统/` 讲输入输出、函数、类、JSON
2. 用 `贪吃蛇/` 讲模块化、循环、事件、状态机、算法
3. 用 `五子棋/` 讲交互式 Notebook 与游戏规则设计

### 路线 C：AI 专题延伸

1. 阅读 `大模型微调技术课程大纲.md`
2. 配合 `大模型部署实践.md` 讲平台与部署
3. 用 `《零代码玩转 AI 应用：小白也能轻松上手的开发工具指南》.md` 做工具选型讨论

## 适合谁使用

- Python 初学者
- 需要做课堂教学的老师
- 想找 Notebook 讲义和练手项目的学习者
- 想把 Python 课程扩展到 AI 专题的授课者

## 使用建议

- 先把这个仓库当作“课程资源目录”，不要按单一工程理解
- 运行代码时进入对应子目录再执行
- 讲课时优先结合 `Notebook + 小项目 + 说明文档`
- 如果要整理正式教学大纲，可以优先参考 `教学主题快速参考.md` 和 `大模型/` 下的专题资料

## 说明

- 当前顶层 README 已按仓库内实际可见文件重新整理
- 部分资料是文档型内容，适合阅读，不一定可直接运行
- 部分子项目包含自己的 README，可进入子目录查看更细的说明
