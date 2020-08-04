import email


def parse_mail(text):
    return email.message_from_string(text)


if __name__ == '__main__':
    from pathlib import Path

    mail = Path("D:/simplon/maildir/ring-r/sent_items/42")

    with open(mail, 'r') as file:
        parsed = parse_mail(file.read())

    print(parsed.get_payload())  # contenu
    print(parsed.items())  # header
