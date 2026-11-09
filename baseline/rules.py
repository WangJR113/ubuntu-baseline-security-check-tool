# baseline/rules.py
BASELINE_RULES = [
    {
        "name": "检查SSH是否禁止root登录",
        "cmd": "grep 'PermitRootLogin' /etc/ssh/sshd_config",
        "expect": "no"
    },
    {
        "name": "检查防火墙ufw是否开启",
        "cmd": "ufw status",
        "expect": "active"
    },
    {
        "name": "检查密码最大有效期",
        "cmd": "grep 'PASS_MAX_DAYS' /etc/login.defs",
        "expect": "PASS_MAX_DAYS"
    },
    {
        "name": "检查系统是否存在空密码账号",
        "cmd": "awk -F: '$2==\"\" {print $1}' /etc/shadow",
        "expect": ""
    },
    {
        "name": "检查系统历史命令记录开启",
        "cmd": "echo $HISTCONTROL",
        "expect": "ignoredups"
    }
]
