RESPONSES = {
    "400": {
        "description": "parse error",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Malformed request.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "401": {
        "description": "not authenticated",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Authentication credentials were not provided.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "403": {
        "description": "permission denied",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "You do not have permission to perform this action.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "404": {
        "description": "not found",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Not found.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "405": {
        "description": "method not allowed",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Method not allowed.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "406": {
        "description": "not acceptable",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Could not satisfy the request Accept header.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "415": {
        "description": "unsupported media type",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Unsupported media type in request.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "429": {
        "description": "throttled",
        "schema": {
            "properties": {
                "detail": {
                    "description": "",
                    "example": "Request was throttled.",
                    "type": "string"
                }
            },
            "type": "object"
        }
    }
}


def get_none_pagination_response(item_schema=None, item_response=None) -> dict:
    """
    This method allows to get pagination response with item_schema or item_response for none pagination.
    
    :param item_schema: Is json schema 
    :param item_response: Is example of json object response
    :return:
    """
    _check_item(item_schema, item_response)
    return {
        "200": {
            "description": "",
            'schema': {
                "type": "object",
                "properties": {
                    "results": _get_results(item_schema, item_response)
                }
            }
        }
    }


def get_pagination_response(item_schema=None, item_response=None) -> dict:
    """
    This method allows to get pagination response with item_schema or item_response.

    :param item_schema: Is json schema 
    :param item_response: Is example of json object response
    :return:
    """
    _check_item(item_schema, item_response)
    return {
        "200": {
            "description": "",
            'schema': {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "number",
                        "example": 1
                    },
                    "next": {
                        "type": ["boolean", "null"],
                        "example": False
                    },
                    "previous": {
                        "type": ["boolean", "null"],
                        "example": False
                    },
                    "results": _get_results(item_schema, item_response)
                }
            }
        }
    }


def _check_item(item_schema, item_response):
    if item_schema is None:
        item_schema = {}
    if item_response is None:
        item_response = {}
    if not item_schema and not item_response:
        raise ValueError('you should specify item_schema or item_response')
    if not item_schema and not isinstance(item_schema, dict):
        raise ValueError('item_schema should be dict')
    if not item_response and not isinstance(item_response, dict):
        raise ValueError('item_schema should be dict')
    if item_response:
        for k, v in item_response.items():
            if v is None:
                raise ValueError('swagger does not support null. Use item_schema or remove None in {}'.format(k))


def _get_results(item_schema, item_response) -> dict:
    results = {
            "type": "array",
    }
    if item_response:
        results["example"] = [item_response]
    else:
        results["items"] = item_schema
    return results
