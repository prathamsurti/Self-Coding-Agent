import re
from typing import Dict, List
import logging

def parse_log_file(log_file_path: str) -> Dict[str, List[str]]:
    """
    Reads a log file and categorizes entries by log level.
    
    Args:
        log_file_path (str): Path to the log file
        
    Returns:
        Dict[str, List[str]]: Dictionary with log levels as keys and lists of log messages as values
    """
    # Initialize dictionary to store categorized logs
    log_categories = {
        'error': [],
        'info': [],
        'warning': [],
        'debug': [],
        'critical': []
    }
    
    # Regular expression pattern to match log entries
    log_pattern = r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3})\s+-\s+(\w+)\s+-\s+(.*)'
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.match(log_pattern, line.strip())
                if match:
                    # Extract timestamp, level, and message
                    timestamp, level, message = match.groups()
                    level = level.lower()
                    
                    # Add to appropriate category
                    if level in log_categories:
                        log_entry = {
                            'timestamp': timestamp,
                            'message': message
                        }
                        log_categories[level].append(log_entry)
                    
        return log_categories
    
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        return log_categories
    except Exception as e:
        logging.error(f"Error parsing log file: {str(e)}")
        return log_categories

# Example usage
def analyze_logs(log_file_path: str) -> None:
    """
    Analyzes and prints log statistics from the parsed log file.
    
    Args:
        log_file_path (str): Path to the log file
    """
    log_data = parse_log_file(log_file_path)
    
    print("Log Analysis Summary:")
    print("-------------------")
    for level, entries in log_data.items():
        print(f"{level.upper()} entries: {len(entries)}")
        if entries:
            print("Latest entry:", entries[-1]['message'])
        print()