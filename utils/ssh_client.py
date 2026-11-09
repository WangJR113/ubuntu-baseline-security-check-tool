import paramiko
from utils.logger import logger

class SSHClient:
    def __init__(self, ip, user, pwd, port=22):
        self.ip = ip
        self.user = user
        self.pwd = pwd
        self.port = port
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(hostname=self.ip, username=self.user, password=self.pwd, port=self.port, timeout=8)
            logger.info(f"成功连接服务器：{self.ip}")
            return True
        except Exception as e:
            logger.error(f"连接 {self.ip} 失败：{str(e)}")
            return False

    def exec_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        out = stdout.read().decode("utf-8", errors="ignore").strip()
        err = stderr.read().decode("utf-8", errors="ignore").strip()
        return out, err

    def close(self):
        self.client.close()
        logger.info(f"断开连接 {self.ip}")
