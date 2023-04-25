import gdown

urls ={
    ("./Arrays.ipynb","1FfqrXxrCRQZoSjbh_RJ8MAmxBj-3BBJe"),
    ("./Complete_DSA_Sheet.ipynb","18WHfxqkX3BI-cvGk7c9RhbO1AS4Johwu"),
    ("./Dynamic_Programming.ipynb","1glpAMYYQkCtnvjQdIgkRGun99yIjB1dP"),
    ("./Graphs.ipynb","1ejWi68W4b9w0MUBsPxZiVoxLB7dBYVxi"),
    ("./Linked_Lists.ipynb","1IqZ_yOkk1B2MyV7g8erNVWREPnBgETUj"),
    ("./Trees.ipynb","1Q95bwo2bP6zNvYCAtOnBoYxk7l_rT3nO"),
    ("./Recursion.ipynb", "1f2fDdLks2_8NuEAG9whp397LJMsXILq-g")
}


for local_file_path, gdown_url in urls:
    print(f"Downloading {local_file_path}....")
    gdown.download(id=gdown_url, output=local_file_path)