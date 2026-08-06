tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a PDF, DOCX, or TXT file and return its content along with metadata.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path to the file."
                    }
                },
                "required": ["filepath"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List all files in a directory. Optionally filter by file extension.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory to search."
                    },
                    "extension": {
                        "type": "string",
                        "description": "Optional extension like .pdf or .txt"
                    }
                },
                "required": ["directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write text content to a file. Creates directories if needed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Destination file path."
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write."
                    }
                },
                "required": [
                    "filepath",
                    "content"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_in_file",
            "description": "Search for a keyword in a file and return matching text with surrounding context.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path to the file."
                    },
                    "keyword": {
                        "type": "string",
                        "description": "Keyword to search."
                    }
                },
                "required": [
                    "filepath",
                    "keyword"
                ]
            }
        }
    }
]