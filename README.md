# Re-Pro

This repository helps you set up a reproducibility proof for your project. It's quite easy, trust me.

## About provable reproducibility

How can scientists unmistakably know whether their results can be reproduced by other people? How can reviewers verify that a certain numerical experiment published in an article is correct? And how can collaborators quickly understand how to use the source code you have written for your project? As the age-old saying in the Swiss army goes:

> Vertrauen ist gut; Kontrolle ist besser. - Trust is good; control is better.

Provable reproducibility is an initiative, which pursues the goal of making results published in articles, theses, and software packages easier to reproduce and verify. No more ambiguity, data manipulation, cherry-picked parameters, and hand-crafted results. Every figure, plot, and table in a provably reproducible project can be unequivocally traced back to where it originated from.

## Quick start

To make your GitHub project provably reproducibile, run the following command:

```bash
git pull https://github.com/FMatti/Re-Pro <preset> --allow-unrelated-histories
```

You may choose from the following presets: 

| Preset | Description |
| ------ | ------------- |
| python-latex | Python scripts and LaTeX project |
| python-latex-bibtex | Python scripts and LaTeX project with BibTeX bibliography component |
| matlab-latex | MATLAB scripts and LaTeX project |
| julia-latex  | Julia scripts and LaTeX project |

In the `.github/workflows` directory, you may have to modify the `reproduce.yml` file as follows:

- Change the `LATEX_PROJECT` variable to the name/path of your LaTeX main file (without the `.tex` extension)
- Change the `CODE_FILES` variable to the location of the code file(s) you want to execute with the pipeline (glob patterns supported)
- Change the package imports to the packages you depend on in your code
- Change the LaTeX setup to the packages/compilers your project requires 

Finally, commit and push the changes to GitHub:

```bash
git commit --all -m "add reproducibility proof"
git push
```

## Explanations

On your GitHub repository, every time you push to main branch, a pipeline will be executed. If everything goes well, a green check mark will appear next to the commit message.

![check-mark](https://github.com/FMatti/Re-Pro/assets/79205741/da1dccf2-68c0-4d54-bd65-9cda44496bcd)

You can view all the GitHub actions in the `Actions` tab. Click on one to see all the details.

![pipeline-steps](https://github.com/FMatti/Re-Pro/assets/79205741/e57afb3b-122c-4e7e-88b8-ea8c5212eec9)

This is also where you can download a ZIP archive with the generated PDF in it.

![artifacts-outcome](https://github.com/FMatti/Re-Pro/assets/79205741/950966f0-8b0d-49a6-877f-05215369aa09)

Once you publish your GitHub repository, everyone can inspect your code and the steps used to generate your results. If something goes wrong, a red cross appears and you can inspect the action as above to see where something went wrong.

## Common issues

Unless you are using some extraordinary dependencies or features in your project, your repository should now be configured for provable reproducibility. Some common problems which are encountered by people trying to set up a reproducibility proof are:

- Ìf the branch you want to run the reproducibility proof on is not called `main`, you'll need to modify the `branches:` key at the top of the `reproduce.yml` file.
- If your code files or LaTeX project is located in subdirectories, relative imports may not work any longer, hence you'll need to manually specify the working directory by adding  `
  working-directory: [PATH]` below the commands which run the code.

## Example

The `main` branch of this repository (which you are currently viewing) serves as an example for a provably reproducible project. It includes a

- Python script called `plot.py` which downloads and saves a matrix (`matrix.npz`) from the internet, analyzes its principal components, and visualizes them in a plot which is saved as `plot.pgf`.

- LaTeX project `main.tex` with a bibliography `bibliography.bib` which produces a PDF in which the generated plot `plot.pgf` is included.

![example-project](https://github.com/FMatti/Re-Pro/assets/79205741/ba8ea68a-7150-4fbb-a313-a9ab6d564fb5)

## The Re-Pro badge

The Re-Pro badge is the seal of reproducibility which can be displayed in a document. It certifies that a document was indeed produced based on the given commit.

[Image of badge]

## Advanced usage

### Commit and push changes to repository

If you want to commit and push the generated changes from the reproducibility proof to your repository, add write-permissions to the build:

```yaml
jobs:
  build:
    permissions:
      contents: write
```

Subsequently you can add the following step to your action (make sure to replace `[FILES]` by the space-separated filepaths of the files you want to be changed):

```yaml
- name: Commit and push generated files to repository
    run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
        git add [FILES]
        git commit -m "reproduce thesis"
        git push
```

### Synchronizing GitHub repositories with Overleaf

Another advantage of tracking your code in a GitHub repository is that you can view and edit your project from Overleaf. The process for setting this up is described in the [Overleaf guide on GitHub Synchronisation](https://www.overleaf.com/learn/how-to/GitHub_Synchronization).

### About PGF plots

This example repository also serves as a demonstration of how matplotlib plots are to be exported and included in LaTeX projects. Any other way than using .pgf files for this purpose should be pursued as a criminal offence.
