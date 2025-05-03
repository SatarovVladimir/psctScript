import os
import shutil

# Get the project root directory (where the script is located)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Source and destination paths (using relative paths from project root)
source_dir = os.path.join(project_root, "outputModels", "res")
dest_processed = os.path.join(project_root, "createGraphics", "LoadHeight", "modelsLoadHeight")
dest_deformation = os.path.join(project_root, "createGraphics", "StressStrain", "modelsStressStrain")

# Create destination folders if they don't exist
os.makedirs(dest_processed, exist_ok=True)
os.makedirs(dest_deformation, exist_ok=True)


def copy_files(source, pattern, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source directory not found: {source}")

    print(f"Checking files in: {source}")
    for file in os.listdir(source):
        if file.endswith(pattern):
            src_path = os.path.join(source, file)
            shutil.copy2(src_path, destination)
            print(f"✓ Copied: {file} → {destination}")


try:
    print("Starting file copy process...")
    copy_files(source_dir, "_processed_data.xlsx", dest_processed)
    copy_files(source_dir, "_deformation_results.xlsx", dest_deformation)
    print("\nOperation completed successfully!")
except FileNotFoundError as e:
    print(f"\nError: {e}")
    print("Current working directory:", os.getcwd())
    print("Please verify the paths exist:")
    print(f"- Source dir exists: {os.path.exists(source_dir)}")
    print(f"- Processed dest exists: {os.path.exists(dest_processed)}")
    print(f"- Deformation dest exists: {os.path.exists(dest_deformation)}")