import subprocess
import logging
from db.mysql_db import init_table, save_check_result
from baseline.rules import BASELINE_RULES
from report.html_report import generate_html_report
import os
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/run.log", encoding="utf-8"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def run_local_cmd(cmd):
    """在本机WSL执行命令，返回输出"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return "", str(e)


def baseline_check():
    all_result = []
    logger.info("===== 开始Ubuntu本地安全基线巡检 =====")
    for rule in BASELINE_RULES:
        rule_name = rule["name"]
        check_cmd = rule["cmd"]
        expect = rule["expect"]

        out, err = run_local_cmd(check_cmd)
        status = "pass" if expect in out else "fail"

        item = {
            "rule_name": rule_name,
            "cmd": check_cmd,
            "output": out,
            "stderr": err,
            "expect": expect,
            "status": status,
            "check_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        all_result.append(item)
        logger.info(f"【{status}】{rule_name}")
        # 存入mysql（预留）
        save_check_result(item)
    return all_result


if __name__ == "__main__":
    # 初始化数据库（预留）
    init_table()
    try:
        res_list = baseline_check()
        # 生成HTML报告
        report_path = generate_html_report(res_list)
        logger.info(f"✅ 巡检完成！HTML报告已输出：{report_path}")
    except Exception as e:
        logger.error(f"巡检失败：{str(e)}")
