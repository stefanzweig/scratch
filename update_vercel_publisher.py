import pkg_resources
import importlib.metadata
import os


def find_package_location(package_name):
    try:
        package = pkg_resources.get_distribution(package_name)
        return package.location
    except pkg_resources.DistributionNotFound:
        return f"Package '{package_name}' not found."

def find_package_location_meta(package_name):
    try:
        package = importlib.metadata.distribution(package_name)
        return package.locate_file('')
    except pkg_resources.DistributionNotFound:
        return f"Package '{package_name}' not found."

package_name = 'datasette-publish-vercel'
location = find_package_location(package_name)
location_meta = find_package_location_meta(package_name)
print(location_meta)
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
new_package = package_name.replace("-", "_")
init_file = os.path.join(location_meta, new_package, "__init__.py")
vercel_cli = os.path.join(current_directory, "vercel_cli.py")
with open(vercel_cli, "r") as f:
    data = f.read()
with open(init_file, "w") as ofile:
    ofile.write(data)

