import urllib.request
import tarfile
import os
import tempfile
import shutil

import scipy as sp
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc("text", usetex=True)
matplotlib.rcParams["pgf.texsystem"] = "pdflatex"
matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.size"] = 10

def download_matrix(url, save_path="matrices", save_name=None):
    """
    Download a matrix from an online matrix market archive.

    Parameters
    ----------
    url : str
        The URL, e.g. https://www.[...].com/matrix.tar.gz.
    save_path : str
        The path under which the matrix should be saved.
    save_name : str or None
        The filename of the matrix. When None, name is inferred from url.
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    try:
        # Download the archive containing the matrix
        file_name = os.path.join(temp_dir, "archive.tar.gz")
        archive_file_path, _ = urllib.request.urlretrieve(url, file_name)

        # Open the archive
        with tarfile.open(archive_file_path, "r:gz") as tar:
            # Extract only the ".mtx" files
            mtx_members = [m for m in tar.getmembers() if m.name.endswith(".mtx")]
            tar.extractall(path=temp_dir, members=mtx_members)

            # Convert and save matrices as scipy.sparse.matrix
            for m in mtx_members:
                matrix = sp.io.mmread(os.path.join(temp_dir, m.name))
                if save_name is None:
                    save_name = os.path.splitext(os.path.basename(m.name))[0]
                try:
                    sp.sparse.save_npz(os.path.join(save_path, save_name), matrix)
                except:
                    continue

    finally:
        # Clean up: Delete the temporary directory and its contents
        shutil.rmtree(temp_dir)

# Download sparse matrix from suitesparse collection
download_matrix("https://suitesparse-collection-website.herokuapp.com/MM/VDOL/orbitRaising_1.tar.gz", ".", "matrix.npz")
A = sp.sparse.load_npz("matrix.npz")

# Extract principal components of matrix
u, _, _ = sp.sparse.linalg.svds(A, k=2)
pc = (u.T @ A)

# Visualize principal components
plt.figure(figsize=(3, 3))
plt.scatter(pc[0], pc[1], color="#2F455C")
plt.savefig("plot.pgf", bbox_inches="tight")
