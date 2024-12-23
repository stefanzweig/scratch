import pkg_resources
import importlib.metadata

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
print(location)
print(location_meta)
