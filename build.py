import os
import shutil
from flask_frozen import Freezer
from main import app

print("Starting build process...")

# Create a 'build' directory if it doesn't exist
if not os.path.exists('build'):
    os.makedirs('build')

print(f"Build directory exists: {os.path.exists('build')}")

# Copy static files to the build directory
print("Copying static files...")
shutil.copytree('static', 'build/static', dirs_exist_ok=True)

# Create .nojekyll file
print("Creating .nojekyll file...")
with open('build/.nojekyll', 'w') as f:
    pass
print('.nojekyll file created')

# Initialize Frozen-Flask
print("Initializing Freezer...")
freezer = Freezer(app)

if __name__ == '__main__':
    # Generate static files
    print("Generating static files...")
    freezer.freeze()

    print("Static site generated in the 'build' directory.")
    print("Contents of the build directory:")
    for root, dirs, files in os.walk('build'):
        level = root.replace('build', '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
