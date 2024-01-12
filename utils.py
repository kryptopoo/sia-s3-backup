import locale


def human_size(bytes, units=[' bytes', ' KB', ' MB', ' GB', ' TB']):
    return str(bytes) + units[0] if bytes < 1024 else human_size(
        bytes >> 10, units[1:])


def format_integer(integer):
    return locale.format_string('%d', integer, grouping=True)


def human_time(value, units=['seconds', 'minutes', 'hours']):
    return ('%.1f ' % value) + units[0] if value < 60 else human_time(
        value / 60.0, units[1:])
