# LLM File Assistant

An AI-powered file assistant that uses LLM tool calling to read, search, list, and write resume files.

The project uses OpenRouter with an OpenAI-compatible API and provides custom Python tools for file-system operations.

## Features

- Read TXT, PDF, and DOCX files
- List files in a directory
- Filter files by extension
- Search for keywords inside resumes
- Return matching text with surrounding context
- Create and write resume summaries
- LLM-powered tool selection
- Multi-step tool calling
- Graceful error handling

## Architecture

```text
User
 |
 v
LLM File Assistant
 |
 v
OpenRouter LLM
 |
 |---- read_file()
 |---- list_files()
 |---- search_in_file()
 |---- write_file()
 |
 v
File System
 |
 v
Final Response
