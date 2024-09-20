import os
import shutil
from flask_frozen import Freezer
from main import app

# Create a 'build' directory if it doesn't exist
if not os.path.exists('build'):
    os.makedirs('build')

# Copy static files to the build directory
shutil.copytree('static', 'build/static', dirs_exist_ok=True)

# Create .nojekyll file
with open('build/.nojekyll', 'w') as f:
    pass
print('.nojekyll file created')

# Initialize Frozen-Flask
freezer = Freezer(app)

if __name__ == '__main__':
    # Generate static files
    freezer.freeze()

    print("Static site generated in the 'build' directory.")
