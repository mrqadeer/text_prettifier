from ._version import get_versions

vinfo = get_versions()
version = vinfo["version"]
__version__ = vinfo.get("closest-tag", vinfo["version"])
full_version = vinfo['version']
git_revision = vinfo['full-revisionid']
release = 'dev0' not in version and '+' not in version
short_version = vinfo['version'].split("+")[0]

del get_versions, vinfo
