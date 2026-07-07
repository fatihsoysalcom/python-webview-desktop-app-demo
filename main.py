import webview
import threading
import time

# This example demonstrates the core concept discussed in the article:
# building lightweight desktop applications by leveraging the operating system's
# native WebView engine, rather than bundling a full browser like Electron.
# Verve, Tauri, and Wails all follow this principle for efficiency.

def update_content(window):
    """
    A simple function to simulate dynamic content updates,
    which can be done via JavaScript in the WebView.
    """
    count = 0
    while True:
        time.sleep(2) # Update every 2 seconds
        count += 1
        # Update the content of an element in the WebView via JavaScript.
        # This simulates how a backend (like Verve's Zig backend) might
        # communicate with the frontend (HTML/JS in the WebView).
        window.evaluate_js(f"document.getElementById('dynamic-content').innerText = 'Backend update count: {count}';")
        print(f"Updated content in WebView: {count}")

def main():
    # The HTML content to be displayed in the native WebView.
    # This is the "frontend" part of our desktop application.
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Verve Concept Demo</title>
        <style>
            body { font-family: sans-serif; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f0f0; color: #333; }
            h1 { color: #0056b3; }
            p { font-size: 1.1em; text-align: center; }
            #dynamic-content { font-weight: bold; color: #d9534f; margin-top: 15px; font-size: 1.2em; }
        </style>
    </head>
    <body>
        <h1>Verve Concept: Native WebView Demo</h1>
        <p>This application uses your operating system's native WebView.</p>
        <p>It's a lightweight approach, similar to Verve, Tauri, and Wails.</p>
        <div id="dynamic-content">Waiting for backend updates...</div>
        <p>Unlike Electron, it doesn't bundle a full browser, saving resources.</p>
    </body>
    </html>
    """

    # Create a new window that uses the native WebView.
    # This is the core mechanism that Verve, Tauri, and Wails utilize
    # to achieve smaller file sizes and lower resource consumption.
    window = webview.create_window(
        'Verve Concept Demo (Python + WebView)',
        html=html_content,
        width=800,
        height=600,
        resizable=True,
        # debug=True # Uncomment for debugging JavaScript in the WebView
    )

    # Start a background thread to simulate backend logic updating the frontend.
    # In a real Verve application, this would be the Zig backend communicating
    # with the JavaScript frontend running in the WebView.
    threading.Thread(target=update_content, args=(window,), daemon=True).start()

    # Run the WebView application. This blocks until the window is closed.
    webview.start()

if __name__ == '__main__':
    main()
