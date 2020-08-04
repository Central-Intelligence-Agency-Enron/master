import email


class mail_parser():

    def __init__(self, mail_file):
        self.message = self._parse_mail(mail_file.read())
        self.header = self._get_header()
        self.content = self._get_content()

    def _parse_mail(self, text):
        return email.message_from_string(text)

    def _get_header(self):
        return self.message.items()

    def _get_content(self):
        return self.message.get_payload()


if __name__ == '__main__':
    from pathlib import Path

    mail = Path("D:/simplon/maildir/ring-r/sent_items/42")

    # with open(mail, 'r') as file:
    #     parsed = parse_mail(file.read())

    # print(parsed.get_payload())  # contenu
    # print(parsed.items())  # header
