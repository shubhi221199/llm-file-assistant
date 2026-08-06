import os
from pathlib import Path
from datetime import datetime
from PyPDF2 import PdfReader
from docx import Document


def read_file(filepath: str) -> dict:
    try:
        path = Path(filepath)

        if not path.exists():
            return {
                "success": False,
                "error": "File not found."
            }

        extension = path.suffix.lower()

        if extension == ".txt":
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

        elif extension == ".pdf":
            reader = PdfReader(path)
            content = ""

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"

        elif extension == ".docx":
            document = Document(path)
            content = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        else:
            return {
                "success": False,
                "error": f"Unsupported file type: {extension}"
            }

        metadata = {
            "filename": path.name,
            "extension": extension,
            "size": path.stat().st_size,
            "modified": datetime.fromtimestamp(
                path.stat().st_mtime
            ).strftime("%Y-%m-%d %H:%M:%S")
        }

        return {
            "success": True,
            "content": content,
            "metadata": metadata
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
        
        
def list_files(directory: str, extension: str = None) -> list:
    try:
        path = Path(directory)

        if not path.exists():
            return []

        files = []

        for file in path.iterdir():
            if file.is_file():

                if extension and file.suffix.lower() != extension.lower():
                    continue

                files.append({
                    "name": file.name,
                    "path": str(file),
                    "size": file.stat().st_size,
                    "modified": datetime.fromtimestamp(
                        file.stat().st_mtime
                    ).strftime("%Y-%m-%d %H:%M:%S")
                })

        return files

    except Exception as e:
        return [{"error": str(e)}]       
    
    
def write_file(filepath: str, content: str) -> dict:
    try:
        path = Path(filepath)

        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        return {
            "success": True,
            "message": "File written successfully.",
            "filepath": str(path)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
        
        
        
def search_in_file(filepath: str, keyword: str) -> dict:
    try:
        # Read the file using the existing function
        result = read_file(filepath)

        if not result["success"]:
            return result

        content = result["content"]

        # Convert both to lowercase for case-insensitive search
        content_lower = content.lower()
        keyword_lower = keyword.lower()

        matches = []

        start = 0

        while True:
            index = content_lower.find(keyword_lower, start)

            if index == -1:
                break

            # Get surrounding text (30 chars before and after)
            context_start = max(0, index - 30)
            context_end = min(len(content), index + len(keyword) + 30)

            context = content[context_start:context_end]

            matches.append(context)

            start = index + len(keyword)

        return {
            "success": True,
            "keyword": keyword,
            "count": len(matches),
            "matches": matches
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }