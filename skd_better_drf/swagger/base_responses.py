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


def get_none_pagination_response(item):
    if not isinstance(item, dict):
        raise ValueError('Should be dict')
    return {
        "200": {
            "description": "",
            'schema': {
                "type": "object",
                "properties": {
                    "results": {
                        "type": "array",
                        "items": item
                    }
                }
            }
        }
    }
