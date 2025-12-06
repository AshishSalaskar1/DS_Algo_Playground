# Facade (Structural)

Ref: https://refactoring.guru/design-patterns/facade

Overview
- Provides a simplified interface to a complex subsystem.
- Hides complexity behind a single entry-point.

When to use
- You need a simple API for a complex set of classes.
- You want to decouple client code from subsystem details.

How to identify
- A class that aggregates calls to multiple subsystem classes and exposes a tiny API.

Pros
- Simplifies usage; reduces coupling.
- Makes code easier to read and maintain.

Cons
- Can become a god-object if it grows too much.
- Risk of hiding useful functionality.

Common confusions
- vs Adapter: Facade provides a new simplified interface; Adapter converts an existing one.

Python example (video conversion)
```python
class VideoFile: ...
class Codec: ...
class MPEG4Codec(Codec): ...
class OggCodec(Codec): ...

class CodecFactory:
    @staticmethod
    def extract(file: VideoFile) -> Codec: ...

class BitrateReader:
    @staticmethod
    def read(filename: str, codec: Codec) -> bytes: ...

    @staticmethod
    def convert(buffer: bytes, codec: Codec) -> bytes: ...

class AudioMixer:
    @staticmethod
    def fix(buffer: bytes) -> bytes: ...

class VideoConverterFacade:
    def convert(self, filename: str, to: str) -> bytes:
        file = VideoFile()
        source_codec = CodecFactory.extract(file)
        if to == "mp4":
            dest_codec = MPEG4Codec()
        else:
            dest_codec = OggCodec()
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, dest_codec)
        result = AudioMixer.fix(result)
        return result

if __name__ == "__main__":
    api = VideoConverterFacade()
    data = api.convert("movie.ogg", "mp4")
    print("Converted!", bool(data))
```

Quick glance
- One simple API over many classes.
- Doesn’t forbid direct subsystem access.
