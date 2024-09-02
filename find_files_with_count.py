import os
import glob
from datetime import datetime

def get_modification_date(filepath):
    """Return the modification date of a file in 'YYYY-MM-DD' format."""
    mod_time = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

def find_files_by_date(directory):
    """Find all files in the directory and subdirectories, sorted by modification date."""
    files_by_date = {}

    # Use glob to match all files in the directory recursively
    for file in glob.glob(os.path.join(directory, '**'), recursive=True):
        if os.path.isfile(file):
            mod_date = get_modification_date(file)
            if mod_date in files_by_date:
                files_by_date[mod_date].append(file)
            else:
                files_by_date[mod_date] = [file]

    return files_by_date

def write_results_to_file(filename, files_by_date):
    """Write the results to a file sorted by the latest modification date."""
    with open(filename, 'w') as f:
        if not files_by_date:
            f.write("No files found in the directory.\n")
            return

        # Sort dates in descending order to find the latest date
        sorted_dates = sorted(files_by_date.keys(), reverse=True)
        latest_date = sorted_dates[0]
        latest_files = files_by_date[latest_date]

        # Write the latest modification date and corresponding files
        f.write(f"Latest modification date: {latest_date}\n")
        f.write(f"Count of files modified on this date: {len(latest_files)}\n")
        f.write("Files modified on this date:\n")
        
        for file in latest_files:
            f.write(f"{file}\n")

if __name__ == "__main__":
    # Use the current working directory
    directory = os.getcwd()
    
    # Get all files sorted by their modification date
    files_by_date = find_files_by_date(directory)
    
    # Write results to result.log
    write_results_to_file('result.log', files_by_date)
