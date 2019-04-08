# /usr/bin/env bash
dmypy restart --log-file dmypy.log -- --follow-imports=skip --config-file=mypy_self_check.ini
dmypy check -- mypy/suggestions.py > /dev/null
dmypy suggest --callsites "mypy/suggestions.py 173 44"