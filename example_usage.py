from client import StreamingDelimiterChunker

chunker = StreamingDelimiterChunker(mode="clause")
print("Emitted 1:", chunker.push("Hello there,"))
print("Emitted 2:", chunker.push(" how are you today?"))
print("Flushed remaining:", chunker.flush())
