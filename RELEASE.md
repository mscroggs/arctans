# Making a release

To make a new release of arctans, follow the following steps:

1) Open a pull request to `main` to update the version numbers in `pyproject.toml` and
   `arctans/__init__.py` to `[x].[y].[z]`.
   If you are releasing a major version, you should increment `[x]` and set `[y]` and `[z]` to 0.
   If you are releasing a minor version, you should increment `[y]` and set `[z]` to zero.
   If you are releasing a bugfix, you should increment `[z]`.

2) [Create a release on GitHub](https://github.com/mscroggs/arctans/releases/new) from the `main` branch.
   The release tag and title should be `v[x].[y].[z]` (where `[x]`, `[y]` and `[z]` are as in step 2).
   In the "Describe this release" box, you should bullet point the main changes since the last
   release.

3) Open a pull request to `main` to update the version number in `pyproject.toml` and
   `arctans/__init__.py` to `[x].[y].[z]-dev`.
