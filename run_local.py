
import subprocess
import webbrowser
import time
import socket

def get_free_port():
    """Find a free port on localhost"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def is_port_in_use(port):
    """Check if port is in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def run_local():
    """Run Streamlit locally and open in browser"""
    # Use port 8501 (Streamlit default) or find a free one
    port = 8501 if not is_port_in_use(8501) else get_free_port()

    print(f"Starting Streamlit server on port {port}...")
    process = subprocess.Popen(["streamlit", "run", "app.py", "--server.port", str(port)])

    # Wait for server to start
    time.sleep(2)

    # Open in default browser
    url = f"http://localhost:{port}"
    print(f"Opening {url} in your browser...")
    webbrowser.open(url)

    print("Press Ctrl+C to stop the server when you're done.")

    try:
        # Keep script running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        process.terminate()
        print("Server stopped.")

if __name__ == "__main__":
    print("Fantasy Football AI Cheat Sheet - Local Server")
    print("-" * 50)
    print("Instructions for permanent deployment to Streamlit Cloud (free):")
    print("1. Create a GitHub repository with these files")
    print("2. Go to https://share.streamlit.io/ and sign in with GitHub")
    print("3. Click 'New app' and select your repository")
    print("4. Set the main file path to 'app.py'")
    print("5. Click 'Deploy'")
    print("-" * 50)
    run_local()
