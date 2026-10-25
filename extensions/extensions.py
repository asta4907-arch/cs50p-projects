"""Print a MIME type based on a file's extension."""

MIME_TYPES = {
    ".gif": "image/gif", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".png": "image/png", ".pdf": "application/pdf", ".txt": "text/plain",
    ".zip": "application/zip",
}


def get_mime_type(filename):
    parts = filename.strip().lower().rsplit(".", maxsplit=1)
    if len(parts) == 2:
        return MIME_TYPES.get(f".{parts[1]}", "application/octet-stream")
    return "application/octet-stream"


def main():
    print(get_mime_type(input("File name: ")))


if __name__ == "__main__":
    main()
