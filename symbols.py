import validate


def parse(txt):
    symbols = txt.replace('\n', ' ').casefold().strip()
    results = []
    if symbols:
        for symbol in symbols.split(' '):
            isReal = validate.isValid(symbol)
            emoji = "✅" if isReal else "🆘"
            results.append("{} {}".format(emoji, symbol))
    return results
