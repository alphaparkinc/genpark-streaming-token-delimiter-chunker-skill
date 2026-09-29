"""Streaming Token Delimiter Chunker.
100% Python Standard Library.
"""

import re

class StreamingDelimiterChunker:
    """Groups streaming token deltas into natural sentence and clause boundaries."""
    def __init__(self, mode="clause", max_buffer_chars=120):
        self.mode = mode
        self.max_buffer_chars = max_buffer_chars
        self.buffer = ""

    def push(self, delta: str) -> list:
        self.buffer += delta
        emitted = []

        if self.mode == "sentence":
            pattern = r'^(.*?[.!?])(?:\s+|$)(.*)$'
        elif self.mode == "clause":
            pattern = r'^(.*?[.!?,;:\n])(?:\s+|$)(.*)$'
        else:
            pattern = r'^(.*?\s)(.*)$'

        while True:
            m = re.match(pattern, self.buffer, re.DOTALL)
            if m:
                chunk, remaining = m.group(1), m.group(2)
                emitted.append(chunk.strip())
                self.buffer = remaining
            elif len(self.buffer) >= self.max_buffer_chars:
                emitted.append(self.buffer.strip())
                self.buffer = ""
                break
            else:
                break

        return [e for e in emitted if e]

    def flush(self) -> str:
        res = self.buffer.strip()
        self.buffer = ""
        return res
