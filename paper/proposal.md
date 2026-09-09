# Project Proposal

By Logan Garland

## Summary

This project will develop a reproducible workflow for retraining and evaluating TopoFormer, a machine-learning model for protein–ligand binding affinity prediction (developed here at MSU by the Wei Lab!) using an expanded training dataset enriched with membrane-transporter complexes. The goal is to determine whether increasing the representation of membrane proteins during training improves predictive performance for membrane transport systems, with particular interest in Organic Anion Transporting Polypeptides (OATPs). The semester project will focus on organizing the data-processing, model-training, and evaluation workflow so that baseline and membrane-enriched TopoFormer models can be compared systematically. Success will be evaluated using held-out binding-affinity data and standard regression metrics, while the software itself will be designed to support reproducible retraining and benchmarking.

## Overview

Accurate prediction of protein–ligand binding affinity is an important problem in computational biology and drug discovery. Machine-learning models can help estimate how strongly small molecules interact with protein targets, but their performance depends heavily on the data used for training. Many widely used protein–ligand datasets contain a large number of small soluble proteins and comparatively fewer large membrane proteins, even though membrane proteins are major pharmacological targets.

This project is motivated by Organic Anion Transporting Polypeptides (OATPs), a family of membrane transporters involved in the uptake of endogenous compounds and many clinically relevant drugs. Predicting OATP–ligand interactions is challenging because OATPs are highly polyspecific and can recognize structurally diverse compounds. Improved computational models for these systems could support studies of transporter substrate recognition, drug disposition, drug–drug interactions, and transporter engineering.

TopoFormer is a machine-learning framework that represents protein–ligand complexes using topological features and predicts binding affinity with a transformer-based model. The central question of this project is whether enriching the TopoFormer training data with additional membrane-transporter complexes can improve predictive performance for transporter systems. To address this question, I will build a reproducible workflow for augmenting the existing training data, retraining the model, and comparing its performance against the original TopoFormer baseline.

## Software or Project Description

The primary software goal of this project is to develop a reproducible workflow for extending the TopoFormer training dataset, retraining the model, and evaluating changes in predictive performance. Existing TopoFormer code will provide the underlying model architecture, while this project will focus on organizing and improving the surrounding data-processing, training, and benchmarking workflow needed for membrane-transporter-focused model development.

The workflow will include four main components: preparation of baseline and membrane-transporter-enriched datasets, generation of TopoFormer-compatible input features, reproducible model training, and evaluation of trained models using held-out test data. Configuration files and documented commands will be used where possible so that different training conditions can be compared consistently.

The intended users are researchers who want to retrain or evaluate TopoFormer on specialized protein classes or modified datasets. Although the project is motivated by OATP transporters, the workflow will be designed so that it can be adapted to other membrane-protein systems. The expected impact is a clearer and more reproducible way to test whether targeted changes in training data improve TopoFormer performance for protein classes that may be underrepresented in general protein–ligand datasets.

## Project Goals and Timeline

The project will begin by reproducing the existing TopoFormer training and evaluation workflow and documenting the baseline software and data requirements. The next phase will focus on identifying and integrating additional membrane-transporter protein–ligand data, generating compatible TopoFormer features, and retraining the model with the expanded dataset. During the final phase of the semester, I will compare the retrained model against the original baseline, refine the workflow, and improve testing and documentation.

By the first milestone, the repository will contain the initial project structure, proposal, README, and a clear plan for baseline reproduction. By the end of the semester, the goal is to have a reproducible workflow for transporter-enriched TopoFormer training and evaluation.

## Methods and Workflow

The project will use the existing TopoFormer architecture and training data as a baseline. Additional membrane-transporter protein–ligand complexes will be curated, converted into the topological feature representation required by TopoFormer, and added to the training workflow. Baseline and membrane-enriched models will then be trained and evaluated using held-out test data and standard regression metrics such as RMSE, MAE, and correlation coefficients.

The software workflow will be managed with GitHub and documented so that data preparation, training, and evaluation can be repeated consistently. Testing, configuration files, dependency documentation, and reproducible random seeds will be added where appropriate as the project develops.

## Anticipated Challenges

A primary challenge will be identifying enough membrane-transporter complexes with both suitable structural data and reliable experimental binding-affinity measurements. The amount of usable transporter-specific data may therefore limit how much the training set can be expanded. A second challenge will be avoiding data leakage between training and evaluation datasets, particularly for closely related proteins or repeated ligands. Careful dataset curation and tracking of structural and protein identifiers will be used to reduce this risk.

It is also possible that adding membrane-transporter data will not improve model performance. In that case, the project will still provide a useful reproducible framework for testing how changes in training-set composition affect TopoFormer predictions, and how to meaningfully alter the composition of training data for a large protein-ligand binding model.

## Expected Outcomes

By the end of the semester, I expect to have a reproducible workflow for preparing membrane-transporter-enriched training data, retraining TopoFormer, and comparing the resulting model against the original baseline. Success will be evaluated using held-out protein–ligand affinity data and regression metrics such as RMSE, MAE, and correlation coefficients.

A successful outcome would show either improved predictive performance for membrane-transporter systems or, if performance does not improve, a clear and reproducible assessment of how transporter-enriched training affects TopoFormer predictions.
