import atexit
import sys
import subprocess
import os


def restart_script():
    print("Restarting script...")
    try:
        # Get the current script file name
        script_name = os.path.basename(sys.argv[0])
    except Exception as e:
        print(f"Error retrieving script name: {e}")
        script_name = None

    if script_name:
        # Use subprocess to run the script again
        subprocess.Popen([sys.executable, script_name])
        
    # Exit the current process to allow the new instance to run
    sys.exit()
    
atexit.register(restart_script)


# taskkill /F /IM python.exe
