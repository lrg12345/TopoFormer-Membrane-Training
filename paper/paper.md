---
title: 'TopoFormer Membrane Training: Reproducible Analysis of Membrane Transporter-Ligand Affinity Predictions'
authors:
  - name: Logan Garland
    affiliation: '1'
affiliations:
  - name: Michigan State University
    index: 1
---

# Summary

This project develops reproducible analysis tools supporting the evaluation and eventual retraining of TopoFormer for membrane-transporter protein-ligand systems. The current software parses structure-level binding-affinity predictions, aggregates predictions across replicate protein-ligand structures, and generates standardized ligand-level statistics. Automated tests, reference validation data, and documented command-line workflows provide a reproducible foundation for future comparisons between baseline and membrane-transporter-enriched models.

# Statement of need

Describe the problem that the software addresses and why it is important. Explain who the intended users are and how the software fits into the broader research landscape.

# State of the field

Briefly describe related software or methods in the field and explain how your work compares to or builds on them. If relevant, explain what gap your project addresses.

# Software design

Describe the main design choices, architecture, or workflow decisions that shape the software. Focus on meaningful trade-offs and why the chosen approach is appropriate for the research problem.

# Research impact

Summarize the current or expected impact of the software. This can include reproducible analyses, adoption by others, or evidence of significance in the research workflow. Keep this specific and realistic rather than promotional.

# Project evolution and lessons learned

Use this section to draft short reflections from each in-class activity. These notes can later be refined into the final report and should connect the course activities to your project.

## Reproducibility and Repository Review

As part of the Milestone 4 documentation and reproducibility pass, I tested the project in an isolated copy of the repository with a separately created Conda environment on the MSU HPCC. This test used the included example data rather than relying on private research files or previously generated intermediate outputs.

The independent workflow successfully generated API documentation using pdoc, passed all 10 automated tests, and reproduced the reference OATP1B3 prediction summary. Specifically, 28 structure-level predictions were aggregated into three ligand-level summaries, with numerical results matching the committed reference within floating-point tolerance.

The initial review exposed a reproducibility issue: Ruff scanned the project-local Conda environment and reported errors from third-party dependencies. Adding `.envs/` to the Ruff exclusion configuration resolved the issue, allowing `make check` to run successfully in the isolated environment.

This exercise reinforced the importance of testing installation and execution instructions independently of the development environment. It also highlighted the value of distributing small example datasets, documenting expected outputs, and providing automated validation commands. A true fresh Git clone on another operating system remains to be tested.

## Modeling Intro

This activity helped me understand how a working script can be gradually turned into a more reusable software tool. I learned how to move functions into a separate Python module, import them into a notebook, inspect them with `dir()` and `help()`, and make the same file usable from the command line with `if __name__ == "__main__":`. I also learned how tools like Ruff and git diff can help improve code quality and make automated changes easier to review.

The most useful techniques for me were separating reusable functions from notebook-specific code, using `%autoreload 2` while developing a library, and using Ruff to catch formatting issues automatically. These ideas relate directly to my research project because I already work with computational pipelines and scripts that are reused across multiple analyses. I plan to adopt more of this structure in my project code by keeping reusable functions in modules, using clearer docstrings, and running linting and formatting tools before committing changes.

## Analytical Modeling

This assignment helped me think more carefully about analytical modeling as a process rather than just a final equation. I learned how symbolic tools such as SymPy can be used to define and manipulate model components, while numerical and statistical tools such as NumPy, pandas, and statsmodels are useful for exploring noisy data, estimating parameters, and evaluating model fit. The most useful part for me was seeing how residuals, parameter recovery, and model comparison can reveal problems that are not obvious from a single summary statistic. 

This connects well to my own research, where I work with computational models of protein–ligand interactions and often need to determine whether an apparent relationship reflects a meaningful signal or noise in the data. I can see myself using synthetic data, parameter-recovery tests, residual analysis, and model comparison more deliberately when validating computational pipelines or relating molecular features to experimental outcomes. Going forward, I plan to adopt more of these diagnostic and reproducibility practices rather than relying only on model performance metrics.

## Physical Modeling

Draft a short reflection on what you learned in the physical modeling activities, which methods or tools were most useful, how the work relates to your project, and whether you plan to adopt any of the ideas.

## Data-Driven Modeling

Draft a short reflection on what you learned in the data-driven modeling activities, which methods or tools were most useful, how the work relates to your project, and whether you plan to adopt any of the ideas.

# AI usage disclosure

Describe whether generative AI tools were used in the development of the software, documentation, or manuscript. If no AI tools were used, state that clearly. If they were used, describe the nature of the assistance and how the results were checked.

# Acknowledgements

List any contributors, funding sources, or support that should be acknowledged.

# References

Add references to related software, methods, and relevant literature.
