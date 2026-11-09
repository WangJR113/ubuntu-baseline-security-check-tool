def generate_html_report(check_result_list):
    html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>Ubuntu安全基线巡检报告</title>
<style>
table{border-collapse:collapse;width:90%;margin:20px auto;}
th,td{border:1px solid #ccc;padding:8px 12px;}
.pass{background:#d4edda;color:#155724}
.fail{background:#f8d7da;color:#721c24}
h2{text-align:center}
</style>
</head>
<body>
<h2>Ubuntu安全基线巡检报告</h2>
<table>
<tr><th>检查项</th><th>执行命令</th><th>预期结果</th><th>状态</th><th>输出</th></tr>
"""
    for item in check_result_list:
        status_class = "pass" if item["status"] == "pass" else "fail"
        html_template += f"""
<tr class="{status_class}">
<td>{item['rule_name']}</td>
<td>{item['cmd']}</td>
<td>{item['expect']}</td>
<td>{item['status']}</td>
<td>{item['output']}</td>
</tr>
"""
    html_template += "</table></body></html>"
    report_path = "report/baseline_report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    return report_path
