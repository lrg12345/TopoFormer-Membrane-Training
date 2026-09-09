# TopoFormer Membrane Training

This repository contains a semester-long CMSE 802 research software project focused on retraining and evaluating TopoFormer with additional membrane-transporter protein-ligand data. 

## Project Goal

TopoFormer is a machine-learning model for protein–ligand binding-affinity prediction. This project asks whether enriching its existing training dataset with additional membrane-transporter complexes can improve predictive performance for transporter systems, with particular interest in Organic Anion Transporting Polypeptides (OATPs). 

The primary software goal is to develop a reproducible workflow for:

1. Preparing baseline and membrane-transporter-enriched training data,
2. Generating TopoFormer-compatible features,
3. Retraining the model, and
4. Comparing model performance using held-out test data. 

## Repository Structure
- `topoformer_membrane/` — Python code developed for the project
- `paper/` — project proposal and eventual JOSS-style manuscript
- `scripts/` — project and repository utility scripts
- `guides/` — supporting documentation from the course template
- `environment.yml` — software environment specification
- `makefile` — convenience commands for common development tasks

Large training outputs will not be stored directly in this repository due to size limitations, but a separate link to them will make them accessible to users. 

## Project Status

Milestone 1 establishes the project scope, repository structure, and initial proposal. The current proposal is available in `paper/proposal.md.`

## Planned Workflow 

The project will first reproduce the existing TopoFormer training and evaluation workflow to establish a baseline. Additional membrane-transporter training examples will then be incorporated into the workflow, followed by model retraining and comparison against the original baseline.

Model performance will be evaluated using held-out binding-affinity data and regression metrics including RMSE, MAE, and correlation coefficients.

## Software Setup 

Dependency and environment requirements will be updated as the TopoFormer training workflow is incorporated into this repository. The repository includes the course template's `environment.yml` and Make workflow as an initial software-engineering scaffold.

## Next Step

The next planned step is to reproduce the existing TopoFormer baseline training and evaluation workflow and identify the code, data, and dependencies required to make that workflow reproducible within this project.