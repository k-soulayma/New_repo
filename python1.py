from jinja2 import Template



ID_list=["001","002","003","004","005"]
Tests_list=["test_1", "test_2", "test_3","test_4","test_5"]
state=["OK","KO","KO","OK","OK"]

test_results = []
for i in range(len(ID_list)):
    test_results.append({
        'test_id': ID_list[i],
        'test': Tests_list[i],
        'status': state[i]
    })


html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Dynamic Test Report</title>
    <style>
        table { width: 60%; border-collapse: collapse; margin: 20px auto; font-family: Arial; }
        th, td { border: 1px solid black; padding: 10px; text-align: center; }
        th { background-color: #4CAF50; color: white; }
        .failed { background-color: #ffcccc; }
        .success { background-color: #ccffcc; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Test Execution Report</h2>
    <table>
        <tr>
            <th>Test ID</th>
            <th>Test</th>
            <th>Status</th>
        </tr>
        {% for result in test_results %}
        <tr class="{{ 'failed' if result.status == 'KO' else 'success' }}">
            <td>{{ result.test_id }}</td>
            <td>{{ result.test }}</td>
            <td>{{ result.status }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

template = Template(html_template)
html_output = template.render(test_results=test_results)

with open("test_report.html", "w") as f:
    f.write(html_output)
