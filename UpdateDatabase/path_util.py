from pathlib import PurePosixPath

def get_url_segment_from(url: str, segment: int) -> str:
    return PurePosixPath(url).parts[segment]