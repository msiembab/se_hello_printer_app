from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

MOJE_IMIE = "Natalia"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN

    name = request.args.get('name')
    if not name:
        name = MOJE_IMIE

    return get_formatted(msg, name,
                         output.lower())
