#!/usr/bin/python3
from settings import *
with IMAP4_SSL(host=url, ssl_context=context) as M:
    M.LOGIN(user, password)
    M.SELECT('Inbox')
    while True:
        result, numbers = M.UID('search', None, 'ALL')
        uids = numbers[0].split()
        for i in uids:
            if i in pushed_email:
                continue
            data = M.UID('fetch', i, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
            header_data = data[1][0][1]
            parser = HeaderParser()
            msg = parser.parsestr(header_data.decode('utf-8'))
            sender = msg.__getitem__('From')
            subject = msg.__getitem__('Subject')
            print(f"UTF-8 {sender} sent you an email: {subject}")
            requests.post(
                gotifyurl,
                headers=headers,
                data={
                    'title': "Email",
                    'message': f"{sender} send you an email:\n {subject}",
                    'priority': 10})
            pushed_email.append(i)
        time.sleep(60)
    M.CLOSE()
    M.LOGOUT()
