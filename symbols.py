import validate


def parse(txt):
    symbols = txt.replace('\n', ' ').casefold().strip()
    report = []
    results = []
    if symbols:
        for symbol in symbols.split(' '):
            isReal = validate.isValid(symbol)
            emoji = "✅" if isReal else "🆘"
            report.append("{} {}".format(emoji, symbol))
            if isReal:
                results.append(symbol)
    return results, report
