---
title: 'My Research Software Title'
authors:
  - name: Your Name
    affiliation: '1'
affiliations:
  - name: Your Institution
    index: 1
---

# Summary

Provide a concise summary of the software and its purpose for a broad, non-specialist audience. Explain what the software does and why it matters in a research context.

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

## Modeling Intro

This activity helped me understand how a working script can be gradually turned into a more reusable software tool. I learned how to move functions into a separate Python module, import them into a notebook, inspect them with `dir()` and `help()`, and make the same file usable from the command line with `if __name__ == "__main__":`. I also learned how tools like Ruff and git diff can help improve code quality and make automated changes easier to review.

The most useful techniques for me were separating reusable functions from notebook-specific code, using `%autoreload 2` while developing a library, and using Ruff to catch formatting issues automatically. These ideas relate directly to my research project because I already work with computational pipelines and scripts that are reused across multiple analyses. I plan to adopt more of this structure in my project code by keeping reusable functions in modules, using clearer docstrings, and running linting and formatting tools before committing changes.

## Analytical Modeling

Draft a short reflection on what you learned in the analytical modeling activities, which methods or tools were most useful, how the work relates to your project, and whether you plan to adopt any of the ideas.

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
