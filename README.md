# Re-Pro

This repository helps you set up a reproducibility proof for your project. It's pretty simple, trust me.

## About provable reproducibility

There is an age-old saying in the Swiss army:

> Vertrauen ist gut; Kontrolle ist besser.

> Trust is good; checking is better.

How can scientists unmistakably know whether their results can be reproduced by other people? How can reviewers verify that a certain numerical experiment in an article is correct? And how can collaborators quickly understand how to use the source code you have written for your project?

Provable reproducibility is an initiative, which pursues the goal of making results published in articles, theses, and software packages easy to reproduce and verify. No more ambiguity, data manipulation, cherry-picked parameters, and hand-crafted results. Every figure, plot, and table in a provably reproducible project can be unequivocally traced back to where it originated from.

## Quick start

To add provable reproducibility to your GitHub repository, run the following command:

```[bash]
git pull https://github.com/FMatti/Re-Pro <preset>
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
- Change the `PYTHON_SCRIPT` variable to the location of the Python script(s) you want to execute with the pipeline (glob patterns supported)
- Change the Python package imports to the packages you use in your Python scripts
- Change the LaTeX setup to the packages/compilers your project requires

Finally, commit and push the changes to GitHub:

```[bash]
git commit --all -m "add reproducibility proof"
git push
```

## Explanations

On your GitHub repository, every time you push to main branch, a pipeline will be executed. If everything goes well, a green check mark will appear next to the commit message.

[Check mark image]

You can view all the GitHub actions in the Actions tab. Click on one to see all the details. This is also where you can download a ZIP archive with the generated PDF in it.

[PDF artifact generated.]

If something goes wrong, a red cross appears and you can click it and display more details about where the failure happened.

[Failed image]

## Example

This repository serves as an example for how a provably reproducible project may look like. [Elaborate more in detail what is done]

## The Re-Pro badge

The Re-Pro badge is the seal of reproducibility which can be displayed in a document. It certifies that a document was indeed produced based on the given commit.

[Image of badge]

## Extended setup

Unless you are using some extraordinary dependencies or features in your project, your repository should now be configured for provable reproducibility.

- Non-default main branch -> change in `reproduce.yml`.
- Add packages in TexLive installation
- Commit to repository using

```[bash]
...

jobs:
  build:
    permissions:
      contents: write
...
```
and subsequently adding the step
```[bash]
...

- name: Commit and push generated files to repository
    run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
        git add [FILES]
        git commit -m "reproduce thesis"
        git push
```

## About PGF plots

This example repository also serves as a demonstration of how matplotlib plots are to be exported and included in LaTeX projects. Any other way than using .pgf files for this purpose should be pursued as a criminal offence.

## Opening GitHub repository with Overleaf

Another advantage of tracking your code in a GitHub repository is that you can view and edit your project from Overleaf. The process for setting this up is described in the [Overleaf guide on GitHub Synchronisation](https://www.overleaf.com/learn/how-to/GitHub_Synchronization).
