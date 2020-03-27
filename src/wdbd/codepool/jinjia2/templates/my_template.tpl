<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <p>普通文本 Name is {{ name }}</p>
        <p>年龄 = {{ age }}</p>

        <p>
        <table border="1" cellspacing="0" cellpadding="0">
            <tr>
            {% for col in employee_table_header %}
                <th style="font-size: 15px; padding: 3px;">{{col}}</th>
            {% endfor %}
            </tr>

            
            {% for record in employee_table_data %}
            <tr>
                <td>{{ record.id }}</td>
                <td>{{ record.name }}</td>
                <td>{{ record.age }}</td>
            </tr>
            {% endfor %}
            
        </table>
        </p>
    </body>
</html>