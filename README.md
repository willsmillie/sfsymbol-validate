# SFValidate - SFSymbol Validation Script

Python script to format &amp; validate a list of SFSymbols against sfsymbols.com

# About

When I received a email containing a list of SFSymbols needing to be placed in an app, I needed to validate they were all correct. I could see some had incorrect casings, and I didn't want to do it manually... So what did I do? Turned a five minute task into a thirty minute task!

Anyway, hope you get some use out of this!

# Usage

`python ./sfvalidate.py symbols.txt -o results.txt`

## example output

```
✅ alarm
✅ gamecontroller.fill
✅ paintpalette
🆘 cup.and.saucer
🆘 fork.knife
✅ figure.walk
✅ ear
```

# TODO

- [] read input of typed / pasted txt if no file is provided
- [] wrap-in-quotes arg: prepares the list to be copied and pasted into an app

# Contributions

Contributions welcome! Feel free to open an issue or PR!
