import pystray, time
from PIL import Image, ImageDraw
from threading import Thread, Event

class ExampleThread(Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = Event()

    def run(self):
        while not self._stop_event.is_set():
            print("Test")
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

def on_clicked(icon, query):
    if str(query) == "receiver":
        if len(threads) == 0:
            threads.append(ExampleThread())
            threads[0].start()
        elif len(threads) == 1:
            if threads[0].is_alive():
                pass
            else:
                threads.pop()
                threads.append(ExampleThread())
                threads[0].start()
        else:
            print('error')
    elif str(query) == "receiver stop":
        threads[0].stop()
        threads[0].join()
    elif str(query) == "Exit":
        icon.stop()

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)
    return image

# image = Image.open("icon.png")
image = create_image(64, 64, 'black', 'white')
 
icon = pystray.Icon("Jenova", image, "JENOVA", menu=pystray.Menu(
    pystray.MenuItem("receiver", on_clicked),
    pystray.MenuItem("receiver stop", on_clicked),
    pystray.MenuItem("Exit", on_clicked)))

threads = [] 
icon.run()