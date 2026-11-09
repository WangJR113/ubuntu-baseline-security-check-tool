import pymysql
from utils.logger import logger

MYSQL_CFG = {
    "user": "root",
    "password": "123456",
    "unix_socket": "/var/run/mysqld/mysqld.sock",
    "database": "baseline_check",
    "charset": "utf8mb4"
}

def init_table():
    """
    初始化数据表，预留MySQL入库能力
    当前环境适配问题，暂时跳过数据库连接
    """
    logger.info("【提示】数据库模块已预留，当前跳过数据库初始化，基线检查正常运行")
    return True

def save_check_result(data):
    """
    保存巡检结果到MySQL，预留接口
    """
    logger.info(f"【预留入库】待存入数据库的数据：{data}")
    return True
