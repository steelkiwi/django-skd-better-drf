## Simple library for DRF
1) Provide additional fields `TimestampField` and `PointField`,
2) Provide  swagger doc.
#### How to use:

##### Swagger docs
If you want to use swagger docs render scheme with JsonSchema, you can use our swagger docs view.

First of all, you should import swagger render view from our library and include url for it.

###### urls.py
```python
from skd_better_drf.swagger.views import get_swagger_view

urlpatterns = [
    url(r'^docs/$', get_swagger_view(title='Pastebin API')),
]
````


By default, our view uses default swagger schema generator. If you want to use JSONSchema for your documentations you need to include two parameters: response_docs for responses and parameters_docs for incoming parameters.

We include the mapping for HTTP methods (`get`, `post`, `put`, `patch`, `delete`) or ViewSet actions (`list`, `retrieve`, `create`, `update`, `partial_update`, `destroy`)
or map your own or standard `get`, `post`, `put`, `patch`, `delete`.**

Start from django rest framework version 3.7 you should use `BaseJsonSchema` as mixin for your view, `from drf_skd_tools.swagger.schema_views import BaseJsonSchema`.  


#### Response Example


```python
       responses_docs = {
        "retrieve": {
            "200": {
                "description": "Success! Instance successfully received",
                "schema": {
                    "title": "Person",
                    "type": "object",
                    "properties": {
                        "firstName": {
                            "type": "string",
                            "example": "My first name"
                        },
                        "lastName": {
                            "type": "string",
                            "example": "My last name"
                        },
                        "age": {
                            "description": "Age in years",
                            "type": "integer",
                            "minimum": 0,
                            "example": 16
                        }
                    },
                    "required": ["firstName", "lastName"]
                }
            },
        },
        "custom_list": {
            "200": {
                "type": "object",
                "description": "parse error",
                "schema": {
                    "properties": {
                        "filter_letter": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "description": "",
                                "example": "This field is required.",
                            }
                        }
                    }
                }
            }
        }
    }
```

#### Parameters example

```python
    parameters_docs = {
        'post': [{
            'in': 'body',
            'name': 'data',
            'description': 'Connect person',
            'schema': {
                "type": "object",
                "properties": {
                    "firstName": {
                        "type": "string",
                        "example": "My first name"
                    },
                    "lastName": {
                        "type": "string",
                        "example": "My last name"
                    },
                    "age": {
                        "description": "Age in years",
                        "type": "integer",
                        "minimum": 0,
                        "example": 16
                    }
                },
                "required": ["firstName", "lastName"]
            }
        }, {
            'in': 'path',
            'type': 'integer',
            'name': 'pk',
            'description': 'Object id',
            'required': True
        }],
        'list': [{
            'in': 'query',
            'type': 'integer',
            'name': 'pk',
            'description': 'Company id',
            'required': True
        }]
    }
```

`skd_better_drf.swagger.base_responses` contain base responses for default error codes like 403, 404, 401 and response for NonePagination.
