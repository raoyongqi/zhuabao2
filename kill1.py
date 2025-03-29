import psutil
import re

def kill_process_by_port(port):
    """
    Finds and kills processes listening on the given port.
    """
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Check if the process has any open connections
            if hasattr(proc, 'connections'):
                for conn in proc.connections(kind='inet'):  # 'inet' for network connections
                    if conn.laddr.port == port:
                        print(f"Killing process {proc.info['name']} with PID {proc.info['pid']} on port {port}")
                        proc.kill()
                        print(f"Process {proc.info['name']} with PID {proc.info['pid']} terminated successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # These exceptions can occur if a process ends before we access its info
            pass

# Example: kill a process using port 65003
port_to_kill = 65003
kill_process_by_port(port_to_kill)
