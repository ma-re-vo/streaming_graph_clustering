import json
import time

class PushshiftStream:
    def __init__(self, file_path, delay=0.001):
        self.file_path = file_path
        self.delay = delay

    def stream(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    yield data
                    time.sleep(self.delay)
                except:
                    continue
