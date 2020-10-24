import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
email['From'] = 'Cathy'
email['To'] = 'abc@gmail.com'  # 輸入收件者mail
email['Subject'] = 'Greetings'
email['Cc'] = 'abc@yahoo.com.tw'  # 輸入CC對象mail
html = Template(Path('index.html').read_text())  # 將html檔製作成template
sub = {'name': 'Sharon', 'date': 'Oct-23'}

email.set_content(html.substitute(sub), 'html')
# 要加第二個參數，才會把它當作html解讀，否則index的所有程式碼都會被寄出
# 第一個參數是內容，第二個參數是檔案解讀形式

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # 使用ehlo指令向esmtp伺服器確認你的身份。
    smtp.starttls()  # 使smtp連線執行在TLS模式，所有的smtp指令都會被加密。
    smtp.login('AAA@gmail.com', 'password1234')  # 輸入信箱帳號密碼
    smtp.send_message(email)
    print("finally done!")
