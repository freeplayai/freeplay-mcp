# Notes

To generate an API spec (as of today, eventually this will change).

Go to 'custom_quart_schema.py' and add this in `generate_rules` after the first unhide rule.

```python
            if getattr(
                self._app.view_functions[rule.endpoint], "is_api_endpoint", False
            ):
                is_unhidden = True
```

Go to localhost:8080/openapi.json and save the file.

Changes in the python-api directory (in anything but the pyproject.toml/uv.lock/etc.) will be overwritten.

```sh
brew install swagger-codegen
swagger-codegen generate -i openapi.json  -l python -o swagger/python-api
```
