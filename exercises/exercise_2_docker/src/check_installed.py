import sys
import pkg_resources

# Print Python version
print("Python version:", sys.version)

# Print installed packages
print("\nInstalled packages:")
installed_packages = pkg_resources.working_set
for package in installed_packages:
    print(f"{package.project_name}=={package.version}")
