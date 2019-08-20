import bottle
from currency_converter import CurrencyConverter

c = CurrencyConverter(fallback_on_wrong_date=True)

@bottle.get('/')
def hello():
    return bottle.template("index.html")

@bottle.get('')
def hello():
    return bottle.template("index.html")

@bottle.post('/converter/')
def converter():
    print(bottle.request)
    value = float(bottle.request.forms['value'])
    from_currency = bottle.request.forms['from_currency']
    to_currency = bottle.request.forms['to_currency']
    try:
        tecaj = get_tecaj(from_currency, to_currency)
        final_value = c.convert(value, from_currency, to_currency)
        return bottle.template('result.html', final_value=final_value, value=value,
                               from_currency=from_currency, to_currency=to_currency, tecaj=tecaj)
    except ValueError:
        return bottle.template("index.html")


@bottle.post('/past_converter/')
def converter():
    print(bottle.request)
    value = float(bottle.request.forms['value'])
    from_currency = bottle.request.forms['from_currency']
    to_currency = bottle.request.forms['to_currency']
    try:
        tecaj = get_tecaj(from_currency, to_currency)
        final_value = c.convert(value, from_currency, to_currency)
        return bottle.template('result.html', final_value=final_value, value=value,
                               from_currency=from_currency, to_currency=to_currency, tecaj=tecaj)
    except ValueError:
        return bottle.template("index.html")

def get_tecaj(from_currency, to_currency):
    tecaj = c.convert(1, from_currency, to_currency)
    return tecaj


bottle.run(reloader=True, debug=True)
