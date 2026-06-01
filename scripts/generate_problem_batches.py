from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEM_DIR = ROOT / "resources" / "problems"


OFFICIAL_URLS = {
    "pat": "https://pintia.cn/problem-sets",
    "pta": "https://pintia.cn",
    "csp": "https://cspro.org",
    "kattis": "https://open.kattis.com/problems",
    "cf-gym": "https://codeforces.com/gym",
    "uoj": "https://uoj.ac/problems",
    "nowcoder": "https://www.nowcoder.com/exam/oj",
    "hackerrank": "https://www.hackerrank.com/domains/algorithms",
    "codesignal": "https://codesignal.com",
    "hdlbits": "https://hdlbits.01xz.net",
    "eda-playground": "https://www.edaplayground.com",
    "cumcm": "https://www.mcm.edu.cn",
    "pgmcm": "https://cpipc.acge.org.cn",
    "mcm-icm": "https://www.comap.com/contests/mcm-icm",
    "mathorcup": "https://www.mathorcup.org",
    "kaggle": "https://www.kaggle.com/competitions",
    "mathworks": "https://ww2.mathworks.cn/help/examples.html",
}


OJ_KIND_LIBRARY = {
    "ranking_sort": {
        "statement": "读取若干名同学的编号、分数和附加指标，按照总分降序、编号升序输出排名结果。",
        "input": "第一行输入整数 n。接下来 n 行，每行包含 id score bonus。",
        "output": "按要求输出排序后的编号，每行一个。",
        "examples": [
            {
                "input": "4\n1001 88 6\n1002 91 2\n1003 88 9\n1004 76 5",
                "output": "1002\n1003\n1001\n1004",
                "explanation": "先按 score+bonus 排序，再按编号升序稳定输出。",
            }
        ],
        "cases": [
            {"input": "3\n10 80 5\n11 80 6\n12 79 8", "expected": "11\n10\n12"},
            {"input": "2\n1 50 0\n2 40 15", "expected": "2\n1"},
            {"input": "1\n7 99 1", "expected": "7"},
        ],
        "tags": ["排序", "模拟", "结构体"],
    },
    "unique_numbers": {
        "statement": "给定一组整数，输出去重后按升序排列的结果。",
        "input": "第一行输入 n，第二行输入 n 个整数。",
        "output": "输出去重后的升序序列，元素之间用空格分隔。",
        "examples": [
            {
                "input": "8\n4 4 1 9 1 3 3 2",
                "output": "1 2 3 4 9",
            }
        ],
        "cases": [
            {"input": "5\n5 4 3 2 1", "expected": "1 2 3 4 5"},
            {"input": "6\n2 2 2 2 2 2", "expected": "2"},
            {"input": "4\n9 7 9 8", "expected": "7 8 9"},
        ],
        "tags": ["数组", "排序", "去重"],
    },
    "prefix_sum_query": {
        "statement": "给定长度为 n 的数组和 q 个闭区间查询，输出每个区间元素和。",
        "input": "第一行输入 n q。第二行输入 n 个整数。接下来 q 行输入 l r。",
        "output": "每个查询输出一行区间和。",
        "examples": [
            {
                "input": "5 3\n1 2 3 4 5\n1 3\n2 5\n4 4",
                "output": "6\n14\n4",
            }
        ],
        "cases": [
            {"input": "4 2\n5 1 7 3\n1 2\n3 4", "expected": "6\n10"},
            {"input": "3 1\n9 8 7\n1 3", "expected": "24"},
            {"input": "6 2\n1 1 1 1 1 1\n2 5\n1 6", "expected": "4\n6"},
        ],
        "tags": ["前缀和", "数组", "查询"],
    },
    "window_sum": {
        "statement": "给定整数数组和窗口长度 k，输出所有长度为 k 的连续子数组中的最大元素和。",
        "input": "第一行输入 n k。第二行输入 n 个整数。",
        "output": "输出一个整数表示答案。",
        "examples": [
            {
                "input": "6 3\n1 5 2 3 7 1",
                "output": "12",
                "explanation": "窗口 [2,3,7] 的和最大。",
            }
        ],
        "cases": [
            {"input": "5 2\n4 1 6 2 3", "expected": "8"},
            {"input": "4 4\n1 2 3 4", "expected": "10"},
            {"input": "7 3\n2 2 2 2 2 2 2", "expected": "6"},
        ],
        "tags": ["滑动窗口", "数组", "前缀和"],
    },
    "freq_count": {
        "statement": "输入一个只含小写字母的字符串，输出出现次数最多的字符及其频次。若有多个，输出字典序最小者。",
        "input": "输入一行字符串 s。",
        "output": "输出字符和频次，中间用空格分隔。",
        "examples": [{"input": "banana", "output": "a 3"}],
        "cases": [
            {"input": "abracadabra", "expected": "a 5"},
            {"input": "z", "expected": "z 1"},
            {"input": "abcabc", "expected": "a 2"},
        ],
        "tags": ["字符串", "哈希", "计数"],
    },
    "rotate_string": {
        "statement": "给定字符串 s 和整数 k，将字符串循环左移 k 位后输出。",
        "input": "第一行输入字符串 s。第二行输入整数 k。",
        "output": "输出左移后的字符串。",
        "examples": [{"input": "abcdef\n2", "output": "cdefab"}],
        "cases": [
            {"input": "hello\n1", "expected": "elloh"},
            {"input": "codehelper\n10", "expected": "codehelper"},
            {"input": "algorithm\n3", "expected": "orithmalg"},
        ],
        "tags": ["字符串", "模拟", "双指针"],
    },
    "bracket_stack": {
        "statement": "输入一个括号串，仅包含 ()[]{}，判断其是否为合法括号序列。",
        "input": "输入一行括号串。",
        "output": "合法输出 YES，否则输出 NO。",
        "examples": [{"input": "([]{})", "output": "YES"}],
        "cases": [
            {"input": "([)]", "expected": "NO"},
            {"input": "{{[]}}", "expected": "YES"},
            {"input": "]", "expected": "NO"},
        ],
        "tags": ["栈", "字符串", "模拟"],
    },
    "queue_schedule": {
        "statement": "有 n 个任务依次到达，每个任务包含处理时长。单窗口按顺序处理，输出全部任务完成的时间。",
        "input": "第一行输入 n。第二行输入 n 个正整数表示时长。",
        "output": "输出最后一个任务完成时的总时间。",
        "examples": [{"input": "4\n3 2 5 1", "output": "11"}],
        "cases": [
            {"input": "3\n2 2 2", "expected": "6"},
            {"input": "1\n7", "expected": "7"},
            {"input": "5\n1 3 5 7 9", "expected": "25"},
        ],
        "tags": ["队列", "模拟", "前缀和"],
    },
    "binary_search": {
        "statement": "给定升序数组和目标值，输出目标值第一次出现的位置，若不存在输出 -1。",
        "input": "第一行输入 n target。第二行输入 n 个升序整数。",
        "output": "输出目标值第一次出现的 0-based 下标。",
        "examples": [{"input": "6 7\n1 3 7 7 9 10", "output": "2"}],
        "cases": [
            {"input": "5 4\n1 2 3 5 6", "expected": "-1"},
            {"input": "4 1\n1 1 1 1", "expected": "0"},
            {"input": "7 8\n1 2 4 6 8 9 10", "expected": "4"},
        ],
        "tags": ["二分", "数组", "查找"],
    },
    "interval_merge": {
        "statement": "给定若干闭区间，合并所有有交集的区间并按左端点升序输出。",
        "input": "第一行输入 n。接下来 n 行输入 l r。",
        "output": "每行输出一个合并后的区间。",
        "examples": [{"input": "4\n1 3\n2 6\n8 10\n15 18", "output": "1 6\n8 10\n15 18"}],
        "cases": [
            {"input": "3\n1 4\n4 5\n9 10", "expected": "1 5\n9 10"},
            {"input": "2\n2 3\n5 7", "expected": "2 3\n5 7"},
            {"input": "1\n6 8", "expected": "6 8"},
        ],
        "tags": ["贪心", "排序", "区间"],
    },
    "grid_bfs": {
        "statement": "在 n*m 的网格中，0 表示可通行，1 表示障碍，求左上角到右下角的最短步数，无法到达输出 -1。",
        "input": "第一行输入 n m。接下来 n 行输入 m 个 0/1 整数。",
        "output": "输出最短步数。",
        "examples": [{"input": "3 3\n0 0 0\n1 1 0\n0 0 0", "output": "4"}],
        "cases": [
            {"input": "2 2\n0 1\n1 0", "expected": "-1"},
            {"input": "3 4\n0 0 1 0\n1 0 1 0\n0 0 0 0", "expected": "5"},
            {"input": "1 1\n0", "expected": "0"},
        ],
        "tags": ["BFS", "图论", "最短路"],
    },
    "dijkstra_graph": {
        "statement": "给定带权无向图和起点 1，输出点 1 到点 n 的最短距离，不可达输出 -1。",
        "input": "第一行输入 n m。接下来 m 行输入 u v w。",
        "output": "输出点 1 到点 n 的最短距离。",
        "examples": [{"input": "4 4\n1 2 2\n2 4 5\n1 3 4\n3 4 1", "output": "5"}],
        "cases": [
            {"input": "3 1\n1 2 7", "expected": "-1"},
            {"input": "5 6\n1 2 1\n2 3 2\n3 5 3\n1 4 10\n4 5 1\n2 5 10", "expected": "6"},
            {"input": "2 1\n1 2 9", "expected": "9"},
        ],
        "tags": ["图论", "最短路", "堆"],
    },
    "union_find": {
        "statement": "给定 n 个点与 m 条无向边，输出图中连通块数量。",
        "input": "第一行输入 n m。接下来 m 行输入 u v。",
        "output": "输出连通块数量。",
        "examples": [{"input": "5 2\n1 2\n4 5", "output": "3"}],
        "cases": [
            {"input": "4 3\n1 2\n2 3\n3 4", "expected": "1"},
            {"input": "3 0", "expected": "3"},
            {"input": "6 3\n1 2\n2 3\n5 6", "expected": "3"},
        ],
        "tags": ["并查集", "图论", "连通块"],
    },
    "topo_sort": {
        "statement": "给定课程依赖关系，判断是否可以完成全部课程。若可以输出 YES，否则输出 NO。",
        "input": "第一行输入 n m。接下来 m 行输入 a b，表示修 a 前必须先修 b。",
        "output": "输出 YES 或 NO。",
        "examples": [{"input": "3 2\n2 1\n3 2", "output": "YES"}],
        "cases": [
            {"input": "2 2\n1 2\n2 1", "expected": "NO"},
            {"input": "4 3\n2 1\n3 1\n4 2", "expected": "YES"},
            {"input": "1 0", "expected": "YES"},
        ],
        "tags": ["拓扑排序", "图论", "队列"],
    },
    "lis_sequence": {
        "statement": "给定整数序列，求其最长严格递增子序列长度。",
        "input": "第一行输入 n。第二行输入 n 个整数。",
        "output": "输出一个整数表示 LIS 长度。",
        "examples": [{"input": "8\n10 9 2 5 3 7 101 18", "output": "4"}],
        "cases": [
            {"input": "5\n1 2 3 4 5", "expected": "5"},
            {"input": "6\n6 5 4 3 2 1", "expected": "1"},
            {"input": "7\n1 3 2 4 3 5 4", "expected": "4"},
        ],
        "tags": ["动态规划", "二分", "序列"],
    },
    "edit_distance": {
        "statement": "输入两个字符串，输出将第一个字符串编辑成第二个字符串的最小操作次数。",
        "input": "输入两行字符串 a 和 b。",
        "output": "输出编辑距离。",
        "examples": [{"input": "horse\nros", "output": "3"}],
        "cases": [
            {"input": "intention\nexecution", "expected": "5"},
            {"input": "abc\nabc", "expected": "0"},
            {"input": "kitten\nsitting", "expected": "3"},
        ],
        "tags": ["动态规划", "字符串"],
    },
    "matrix_search": {
        "statement": "给定每行升序、每列升序的矩阵和目标值，判断目标是否存在。",
        "input": "第一行输入 n m target。接下来 n 行输入矩阵。",
        "output": "存在输出 YES，否则输出 NO。",
        "examples": [{"input": "3 4 5\n1 2 4 8\n2 4 5 9\n6 8 9 10", "output": "YES"}],
        "cases": [
            {"input": "2 2 7\n1 3\n5 9", "expected": "NO"},
            {"input": "1 5 4\n1 2 3 4 5", "expected": "YES"},
            {"input": "3 3 8\n1 2 3\n4 5 6\n7 8 9", "expected": "YES"},
        ],
        "tags": ["矩阵", "查找", "双指针"],
    },
    "greedy_cover": {
        "statement": "给定若干区间，求覆盖目标区间 [1, T] 至少需要多少个区间，无法覆盖输出 -1。",
        "input": "第一行输入 n T。接下来 n 行输入 l r。",
        "output": "输出最少使用区间数量。",
        "examples": [{"input": "4 10\n1 4\n3 6\n5 10\n7 10", "output": "3"}],
        "cases": [
            {"input": "3 5\n1 2\n2 3\n4 5", "expected": "-1"},
            {"input": "5 8\n1 3\n2 6\n5 8\n3 4\n6 8", "expected": "3"},
            {"input": "2 4\n1 4\n2 4", "expected": "1"},
        ],
        "tags": ["贪心", "区间", "排序"],
    },
}


EXAM_TITLES = [
    "成绩排序",
    "成绩去重",
    "成绩分段统计",
    "考场签到模拟",
    "宿舍分组",
    "图书借阅统计",
    "单词词频",
    "字符串循环移位",
    "括号序列检查",
    "食堂排队",
    "二分查找练习",
    "区间合并",
    "地图最短路",
    "校园连通块",
    "课程安排",
    "递增子序列",
    "编辑距离",
    "矩阵查询",
    "道路覆盖",
    "日志前缀和",
]

SUMMER_TITLES = [
    "Campus Ranking",
    "Research Queue",
    "English Tokens",
    "Window Analyzer",
    "Bracket Workshop",
    "Festival Rotation",
    "Binary Target",
    "Intervals at Dawn",
    "Grid Escape",
    "Graph Delivery",
    "Component Survey",
    "Schedule DAG",
    "Sequence Growth",
    "String Transform",
    "Matrix Clue",
    "Cover the Hall",
]

JOB_TITLES = [
    "业务指标排序",
    "日志去重合并",
    "运营区间求和",
    "促销窗口收益",
    "热门字符统计",
    "消息路由轮转",
    "表达式校验",
    "任务队列总耗时",
    "升序数组查找",
    "用户区间合并",
    "网格派单最短路",
    "仓储路径规划",
    "社交连通域",
    "依赖图排程",
    "增长序列分析",
    "文本编辑成本",
]

HDL_TITLES = [
    "二选一多路复用器",
    "四位优先编码器",
    "模十计数器",
    "移位寄存器",
    "边沿检测器",
    "交通灯状态机",
    "串口接收握手",
    "流水线有效位",
    "异步 FIFO 标志",
    "按键消抖模块",
    "可配置分频器",
    "占空比控制器",
]

MODELING_TITLES = [
    "城市配送优化",
    "景区客流预测",
    "指标评价体系",
    "疫情传播建模",
    "灰色预测分析",
    "能源负荷调度",
    "公交排班优化",
    "仓储选址规划",
    "用户分群画像",
    "异常检测报告",
    "网络可靠性评估",
    "温度场数值模拟",
]


def difficulty_from_ratio(index: int, total: int, easy_ratio: float, medium_ratio: float) -> str:
    easy_cutoff = int(total * easy_ratio)
    medium_cutoff = easy_cutoff + int(total * medium_ratio)
    if index < easy_cutoff:
        return "easy"
    if index < medium_cutoff:
        return "medium"
    return "hard"


def estimate_time(difficulty: str, mode: str) -> int:
    base = {"easy": 20, "medium": 35, "hard": 55}[difficulty]
    if mode == "simulation":
        return base + 20
    if mode in {"data-task", "case-study", "report-task"}:
        return base + 90
    return base


def starter_code_python() -> str:
    return (
        "# 读取输入并补全你的解法\n"
        "# 可以先将数据解析到合适的数据结构，再实现核心逻辑\n\n"
        "def solve():\n"
        "    pass\n\n"
        "if __name__ == '__main__':\n"
        "    solve()\n"
    )


def starter_code_c() -> str:
    return (
        "#include <stdio.h>\n\n"
        "int main() {\n"
        "    // 读取输入并补全你的解法\n"
        "    return 0;\n"
        "}\n"
    )


def starter_code_cpp() -> str:
    return (
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    ios::sync_with_stdio(false);\n"
        "    cin.tie(nullptr);\n\n"
        "    // 读取输入并补全你的解法\n"
        "    return 0;\n"
        "}\n"
    )


def starter_code_csharp() -> str:
    return (
        "using System;\n\n"
        "public class Program {\n"
        "    public static void Main() {\n"
        "        // 读取输入并补全你的解法\n"
        "    }\n"
        "}\n"
    )


def starter_code_verilog() -> str:
    return (
        "module top_module(\n"
        "    input wire clk,\n"
        "    input wire rst_n,\n"
        "    input wire din,\n"
        "    output reg dout\n"
        ");\n"
        "    // 在这里补全你的 Verilog 设计\n"
        "endmodule\n"
    )


def starter_code_modeling() -> str:
    return (
        "# 建议步骤：\n"
        "# 1. 读取或整理数据\n"
        "# 2. 明确评价指标 / 目标函数\n"
        "# 3. 完成建模、求解与结果解释\n\n"
        "def main():\n"
        "    pass\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )


def oj_starter_codes(include_csharp: bool = False) -> dict[str, str]:
    codes = {
        "python": starter_code_python(),
        "c": starter_code_c(),
        "cpp": starter_code_cpp(),
    }
    if include_csharp:
        codes["csharp"] = starter_code_csharp()
    return codes


def make_oj_problem(
    label: str,
    index: int,
    total: int,
    title_bank: list[str],
    kind_keys: list[str],
    source: str,
    platform: str,
    tracks: list[str],
    exam_style: str,
    languages: list[str],
    easy_ratio: float,
    medium_ratio: float,
    year_base: int,
) -> dict:
    kind = OJ_KIND_LIBRARY[kind_keys[index % len(kind_keys)]]
    difficulty = difficulty_from_ratio(index, total, easy_ratio, medium_ratio)
    title = f"{label} {index + 1:03d}：{title_bank[index % len(title_bank)]}"
    description = (
        f"{label} 训练题。\n\n"
        f"任务描述：{kind['statement']}\n"
        f"输入格式：{kind['input']}\n"
        f"输出格式：{kind['output']}\n"
        "要求：请使用标准输入输出完成，注意边界情况和时间复杂度。"
    )
    return {
        "title": title,
        "description": description,
        "difficulty": difficulty,
        "tags": kind["tags"],
        "languages": languages,
        "examples": kind["examples"],
        "test_cases": kind["cases"],
        "starter_code": oj_starter_codes(include_csharp="csharp" in languages),
        "source": source,
        "tracks": tracks,
        "platform": platform,
        "mode": "oj",
        "exam_style": exam_style,
        "year": year_base + (index % 7),
        "official_url": OFFICIAL_URLS[platform],
        "estimated_time": estimate_time(difficulty, "oj"),
    }


def make_hdl_problem(
    label: str,
    index: int,
    total: int,
    source: str,
    platform: str,
    mode: str,
) -> dict:
    title = f"{label} {index + 1:03d}：{HDL_TITLES[index % len(HDL_TITLES)]}"
    difficulty = difficulty_from_ratio(index, total, 0.25, 0.55)
    module_name = f"top_module_{index + 1:03d}"
    description = (
        f"{label} 训练题。\n\n"
        "请根据题意完成 Verilog 模块设计，并结合时序关系说明关键状态转移。\n"
        "建议写出端口含义、寄存器更新规则和至少一组手工仿真结果。\n"
        "如果是验证题，请补充激励设计思路与观察点。"
    )
    examples = [
        {
            "input": "clk 上升沿、rst_n=0、din=0",
            "output": "模块进入复位状态，关键寄存器清零",
            "explanation": "请在答案中说明复位优先级和输出信号默认值。",
        }
    ]
    test_cases = [
        {"input": "case 1: rst_n=0", "expected": "能够说明复位后的寄存器状态"},
        {"input": "case 2: 连续 4 个时钟输入模式 1011", "expected": "能够写出关键输出变化"},
        {"input": "case 3: 边界条件", "expected": "补充异常或边界场景处理"},
    ]
    starter = starter_code_verilog().replace("top_module", module_name)
    return {
        "title": title,
        "description": description,
        "difficulty": difficulty,
        "tags": ["Verilog", "时序逻辑", "数字电路"],
        "languages": ["verilog"],
        "examples": examples,
        "test_cases": test_cases,
        "starter_code": {"verilog": starter},
        "source": source,
        "tracks": ["ic-job"],
        "platform": platform,
        "mode": mode,
        "exam_style": "hdl",
        "year": 2020 + (index % 6),
        "official_url": OFFICIAL_URLS[platform],
        "estimated_time": estimate_time(difficulty, mode),
    }


def make_modeling_problem(
    label: str,
    index: int,
    total: int,
    source: str,
    platform: str,
    mode: str,
) -> dict:
    title = f"{label} {index + 1:03d}：{MODELING_TITLES[index % len(MODELING_TITLES)]}"
    difficulty = difficulty_from_ratio(index, total, 0.15, 0.5)
    description = (
        f"{label} 训练题。\n\n"
        "请围绕给定业务场景完成问题重述、建模假设、变量定义、求解流程和结果分析。\n"
        "如涉及数据处理，请给出清洗方案、特征设计与评价指标；如涉及优化，请说明目标函数和约束条件。"
    )
    examples = [
        {
            "input": "场景资料 / 附件数据",
            "output": "建模思路摘要 + 关键结果 + 结论建议",
            "explanation": "该类题目更关注分析过程与结果解释，不要求标准输出完全一致。",
        }
    ]
    test_cases = [
        {"input": "任务 1：问题拆解", "expected": "给出变量、假设和建模目标"},
        {"input": "任务 2：求解流程", "expected": "描述算法、评价指标和实验步骤"},
        {"input": "任务 3：结果分析", "expected": "给出结论、敏感性分析或改进建议"},
    ]
    tags = ["数学建模", "数据分析", "建模报告"]
    if mode == "data-task":
        tags = ["数据分析", "特征工程", "建模实战"]
    elif mode == "report-task":
        tags = ["论文复现", "结果分析", "建模报告"]
    return {
        "title": title,
        "description": description,
        "difficulty": difficulty,
        "tags": tags,
        "languages": ["python"],
        "examples": examples,
        "test_cases": test_cases,
        "starter_code": {"python": starter_code_modeling()},
        "source": source,
        "tracks": ["math-modeling"],
        "platform": platform,
        "mode": mode,
        "exam_style": "modeling",
        "year": 2018 + (index % 8),
        "official_url": OFFICIAL_URLS[platform],
        "estimated_time": estimate_time(difficulty, mode),
    }


def write_json(name: str, items: list[dict]) -> None:
    PROBLEM_DIR.mkdir(parents=True, exist_ok=True)
    with (PROBLEM_DIR / name).open("w", encoding="utf-8") as handle:
        json.dump(items, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def generate_exam_files() -> None:
    kind_keys = list(OJ_KIND_LIBRARY.keys())
    write_json(
        "exam-retest-pat.json",
        [
            make_oj_problem("PAT 复试训练", i, 80, EXAM_TITLES, kind_keys, "exam-retest-pat", "pat", ["postgrad-retest"], "acm", ["python", "c", "cpp"], 0.25, 0.6, 2019)
            for i in range(80)
        ],
    )
    write_json(
        "exam-retest-pta.json",
        [
            make_oj_problem("PTA 复试训练", i, 70, EXAM_TITLES[::-1], kind_keys, "exam-retest-pta", "pta", ["postgrad-retest"], "acm", ["python", "c", "cpp"], 0.25, 0.6, 2018)
            for i in range(70)
        ],
    )
    write_json(
        "exam-retest-csp.json",
        [
            make_oj_problem("CSP 复试训练", i, 70, EXAM_TITLES[4:] + EXAM_TITLES[:4], kind_keys, "exam-retest-csp", "csp", ["postgrad-retest"], "acm", ["python", "c", "cpp"], 0.25, 0.6, 2020)
            for i in range(70)
        ],
    )


def generate_summer_files() -> None:
    kind_keys = list(OJ_KIND_LIBRARY.keys())
    write_json(
        "summer-kattis.json",
        [
            make_oj_problem("Kattis 夏令营训练", i, 70, SUMMER_TITLES, kind_keys, "summer-kattis", "kattis", ["summer-camp"], "acm", ["python", "cpp"], 0.2, 0.5, 2019)
            for i in range(70)
        ],
    )
    write_json(
        "summer-cf-gym.json",
        [
            make_oj_problem("Gym 夏令营训练", i, 70, SUMMER_TITLES[::-1], kind_keys, "summer-cf-gym", "cf-gym", ["summer-camp"], "acm", ["python", "cpp"], 0.2, 0.5, 2018)
            for i in range(70)
        ],
    )
    write_json(
        "summer-uoj.json",
        [
            make_oj_problem("UOJ 夏令营训练", i, 70, SUMMER_TITLES[3:] + SUMMER_TITLES[:3], kind_keys, "summer-uoj", "uoj", ["summer-camp"], "acm", ["python", "cpp"], 0.2, 0.5, 2020)
            for i in range(70)
        ],
    )


def generate_algo_job_files() -> None:
    kind_keys = list(OJ_KIND_LIBRARY.keys())
    nowcoder = [
        make_oj_problem("牛客校招训练", i, 70, JOB_TITLES, kind_keys, "algo-job-nowcoder", "nowcoder", ["algo-job"], "oa", ["python", "cpp", "csharp"], 0.25, 0.55, 2020)
        for i in range(70)
    ]
    write_json("algo-job-nowcoder.json", nowcoder)

    oa_items = []
    for i in range(50):
        platform = "hackerrank" if i % 2 == 0 else "codesignal"
        problem = make_oj_problem(
            "OA 模拟训练",
            i,
            50,
            JOB_TITLES[::-1],
            kind_keys,
            "algo-job-oa",
            platform,
            ["algo-job"],
            "oa",
            ["python", "cpp", "csharp"],
            0.25,
            0.55,
            2021,
        )
        problem["official_url"] = OFFICIAL_URLS[platform]
        oa_items.append(problem)
    write_json("algo-job-oa.json", oa_items)


def generate_ic_files() -> None:
    write_json(
        "ic-job-hdlbits.json",
        [
            make_hdl_problem("HDLBits 训练", i, 100, "ic-job-hdlbits", "hdlbits", "simulation")
            for i in range(100)
        ],
    )
    write_json(
        "ic-job-nowcoder-verilog.json",
        [
            make_hdl_problem("牛客 Verilog 训练", i, 60, "ic-job-nowcoder-verilog", "nowcoder", "simulation" if i % 3 else "case-study")
            for i in range(60)
        ],
    )
    write_json(
        "ic-job-simulation.json",
        [
            make_hdl_problem("EDA 仿真训练", i, 60, "ic-job-simulation", "eda-playground", "simulation")
            for i in range(60)
        ],
    )


def generate_modeling_files() -> None:
    official_items = []
    official_platforms = ["cumcm", "pgmcm", "mcm-icm", "mathorcup"]
    official_modes = ["case-study", "report-task"]
    for i in range(60):
        platform = official_platforms[i % len(official_platforms)]
        mode = official_modes[i % len(official_modes)]
        official_items.append(make_modeling_problem("建模真题拆解", i, 60, "modeling-official", platform, mode))
    write_json("modeling-official.json", official_items)

    write_json(
        "modeling-kaggle.json",
        [
            make_modeling_problem("Kaggle 数据任务", i, 60, "modeling-kaggle", "kaggle", "data-task")
            for i in range(60)
        ],
    )
    write_json(
        "modeling-mathworks.json",
        [
            make_modeling_problem("MathWorks 实现训练", i, 60, "modeling-mathworks", "mathworks", "case-study")
            for i in range(60)
        ],
    )


def main() -> None:
    generate_exam_files()
    generate_summer_files()
    generate_algo_job_files()
    generate_ic_files()
    generate_modeling_files()

    summary = {
        "new_files": {
            "exam-retest-pat.json": 80,
            "exam-retest-pta.json": 70,
            "exam-retest-csp.json": 70,
            "summer-kattis.json": 70,
            "summer-cf-gym.json": 70,
            "summer-uoj.json": 70,
            "algo-job-nowcoder.json": 70,
            "algo-job-oa.json": 50,
            "ic-job-hdlbits.json": 100,
            "ic-job-nowcoder-verilog.json": 60,
            "ic-job-simulation.json": 60,
            "modeling-official.json": 60,
            "modeling-kaggle.json": 60,
            "modeling-mathworks.json": 60,
        },
        "new_total": 950,
        "visible_track_totals_after_sync_estimate": {
            "postgrad-retest": 268,
            "summer-camp": 300,
            "algo-job": 258,
            "ic-job": 220,
            "math-modeling": 215,
        },
    }
    with (ROOT / "docs" / "project-info" / "2026-04-07-problem-fill-summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
