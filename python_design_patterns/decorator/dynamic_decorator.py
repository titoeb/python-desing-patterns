# The decorator design pattern.
# In `classic_decorator.py` we saw the classical decorator design pattern,
# where a decorator-class stores the original object and then adds funtionality.
# Downside is that we cannot access the function of the internal object(s).
import tempfile

# Let's look at the dynamic decorator for that purpose!
class FileWithLogging:
    def __init__(self, file: str) -> None:
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"I wrote {len(strings)} files")

    def __iter__(self):
        self.file.iter()

    def __next__(self):
        self.file.next()

    def __getattr__(self, item):
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["file"], key)

    def __delattr__(self, item):
        delattr(self.__dict__["file"], item)


if __name__ == "__main__":
    tmp_dir = tempfile.gettempdir()
    this_file = FileWithLogging(open(f"{tmp_dir}/test.txt", "w"))
    this_file.writelines(["hello", "world"])
    this_file.write("test")
    this_file.close()
