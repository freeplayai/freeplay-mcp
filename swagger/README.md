# Notes

Go to localhost:8080/openapi.json and save the file.

Changes in the python-api directory (in anything but the pyproject.toml/uv.lock/etc.) will be overwritten.

```sh
brew install swagger-codegen
swagger-codegen generate -i openapi.json  -l python -o swagger/python-api
```
