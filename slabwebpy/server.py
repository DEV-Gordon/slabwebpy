
import http.server
import os
import socketserver
import threading
import webbrowser

from pathlib import Path

from slabwebpy.builder import build

# Dev server to serve the built HTML file
def serve(output: str = "index.html", port: int = 8000, open_browser: bool = True):
    
    """Builds the page and starts a local dev server.

    Args:
        output:       File path to build and serve.
        port:         Port number (default 8000).
        open_browser: Open the browser automatically if True.

    Example:
        slab.serve("dist/index.html", port=3000)
    """

    build(output)

    folder = str(Path(output).parent.resolve())
    os.chdir(folder)

    handler = http.server.SimpleHTTPRequestHandler

    # Silence default request logs
    class QuietHandler(handler):
        def log_message(self, format, *args):
            pass

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        httpd.allow_reuse_address = True

        print(f"\n SlabWeb Dev Server")
        print(f"  ->  Local:   http://localhost:{port}")
        print(f"  ->  File: {output}")
        print(f"\n  Press Ctrl+C to stop\n")

        if open_browser:
            threading.Timer(
                0.5, lambda: webbrowser.open(f"http://localhost:{port}")
            ).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped\n")

"""*Autor: DEV-Gordon (Carlos Zarate) — https://github.com/DEV-Gordon/slabwebpy*"""