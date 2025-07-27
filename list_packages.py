import importlib.metadata

# Get all installed packages
installed_packages = importlib.metadata.distributions()

# Print name and version
for pkg in installed_packages:
    print(f"{pkg.metadata['Name']}=={pkg.version}")