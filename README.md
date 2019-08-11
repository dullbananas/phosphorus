# Phosphorus
Phosphorus is a simple WSGI framework that uses regular expressions for URL endpoints. Here is an example of a simple application implemented in Phosphorus:

```python3
import phosphorus

app = phosphorus.App()

@app.add_endpoint('/(.)')
def single_char(match, environ):
    content = f'<html><head></head><body>Character: {match.group(1)}<br/>Environ: {environ}</body></html>'
    return phosphorus.Response(content)
```
