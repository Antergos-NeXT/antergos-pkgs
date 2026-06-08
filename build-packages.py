import yaml
import subprocess
import os
import shutil
import glob

with open("packages.yaml") as f:
    pkgs = yaml.safe_load(f)["packages"]

os.makedirs("/tmp/pkgout", exist_ok=True)

for pkg in pkgs:
    local_pkgbuild = f"packages/{pkg}/PKGBUILD"
    build_dir = f"/tmp/{pkg}"

    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    if os.path.exists(local_pkgbuild):
        shutil.copytree(f"packages/{pkg}", build_dir)
    else:
        subprocess.run(["git", "clone", f"https://aur.archlinux.org/{pkg}.git", build_dir])

    subprocess.run(["chown", "-R", "builder:builder", build_dir])
    subprocess.run(["su", "-", "builder", "-c", f"cd {build_dir} && makepkg -s --noconfirm --noprogress --skippgpcheck --skipinteg"])

    subprocess.run(f"cp {build_dir}/*.pkg.tar.zst /tmp/pkgout/ || true", shell=True)

print("Done!")
