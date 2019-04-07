import random

quotes = []


def initialize_quotes(file_name):
    fd = open(file_name, 'r')
    quote = ""
    is_last_line_quote = False
    for line in fd:
        if line == '%':
            quotes.append(quote)
            quote = ""
            is_last_line_quote = False
        else:
            quote += line
            is_last_line_quote = True

    fd.close()

    if is_last_line_quote:
        quotes.append(quote)


def get_quote():
    index = random.randint(0, len(quotes))
    return quotes[index]


# ----------------------------------------------------


index = 1
db_instance = DatabasePlatform(db_config)


def initialize_quotes(file_name):
    fd = open(file_name, 'r')
    quote = ""
    is_last_line_quote = False
    for line in fd:
        if line == '%':
            db_instance.db_write(quote)
            index += 1
            quote = ""
            is_last_line_quote = False
        else:
            quote += line
            is_last_line_quote = True

    fd.close()

    if is_last_line_quote:
        db_instance.db_write(quote)
        index += 1


def get_quote():
    len = db_instance.db_size()
    index = random.randint(0, len)
    quote, error = db_instance.db_read(index)
    if error:
        return "No quote found"
    return quote


class DatabasePlatform:
    db_instance

    def __init__(self, db_config):
        if db_instance:
            return db_instance
        db_instance = db.connection(db_config.host, db_config.port, db_config.username, db_config.password)
        return db_instance

    def db_write(self, index, value):
        # query = "insert into quotes values(%s, %s)" + index + "," + quote
        db_instance.write(index, value)

    def db_read(self, index):
        value, error = db_instance.get(index)
        return value, error

    def db_size(self):
        return db_instance.count()

