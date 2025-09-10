# Making a release

To make a new release of arctans, follow the following steps:

1) Checkout the `main` branch and `git pull`, then checkout a new branch called `release-v[x].[y].[z]`
   (where `[x]`, `[y]`, and `[z]` are defined in the next step):
   ```bash
   git checkout main
   git pull
   git checkout -b release-v[x].[y].[z]
   ```

2) Update the version number in `pyproject.toml`.
   The version numbers have the format `[x].[y].[z]`. If you are releasing a major
   version, you should increment `[x]` and set `[y]` and `[z]` to 0.
   If you are releasing a minor version, you should increment `[y]` and set `[z]`
   to zero. If you are releasing a bugfix, you should increment `[z]`.

3) Commit your changes and push to GitHub, open a pull request to merge changes back into main, and merge the
   pull request.

4) [Create a release on GitHub](https://github.com/mscroggs/arctans/releases/new) from the `main` branch.
   The release tag and title should be `v[x].[y].[z]` (where `[x]`, `[y]` and `[z]` are as in step 2).
   In the "Describe this release" box, you should bullet point the main changes since the last
   release.
