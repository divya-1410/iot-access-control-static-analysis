# Research Methodology

## 1. Study Design

This study is designed to investigate the limitations of static analyzers in detecting access-control vulnerabilities in smart contracts relevant to Internet of Things (IoT) environments.

The initial work establishes controlled test cases and a labeling framework. The full evaluation remains pending.

## 2. Research Questions

- **RQ1:** Which access-control weaknesses can be represented in the benchmark?
- **RQ2:** How effectively do selected static analyzers detect the labeled vulnerabilities?
- **RQ3:** What types of false negatives and false positives occur during evaluation?
- **RQ4:** What limitations affect the reproducibility and interpretation of the results?

## 3. Benchmark Construction

The benchmark will distinguish controlled test contracts from real-world contracts. Each case will receive a unique identifier, source type, expected label, vulnerability category, rationale, and review status.

Labels will be reviewed against the contract's actual behavior and relevant access-control requirements before evaluation.

## 4. Analyzer Selection and Configuration

The selected static analyzers, software versions, configuration options, compiler versions, and execution environment will be documented.

A tool will be included in the final comparison only when its installation and execution can be verified. Tool failures will be recorded separately from vulnerability-detection outcomes.

## 5. Evaluation Procedure

For each eligible contract:

1. Establish the expected label through manual review.
2. Run each selected analyzer using documented settings.
3. Save the raw output and execution logs.
4. Map analyzer findings to the benchmark's vulnerability categories.
5. Compare the findings against the reviewed ground truth.
6. Record unresolved cases and investigate disagreements.

## 6. Evaluation Metrics

Where the benchmark and tool outputs support them, the study will calculate:

- **Precision:** TP / (TP + FP)
- **Recall:** TP / (TP + FN)
- **F1-score:** 2 × Precision × Recall / (Precision + Recall)

Here, TP means true positives, FP means false positives, and FN means false negatives. The unit of analysis and matching rules will be defined before calculating final metrics. Undefined metrics will be reported as such rather than treated as zero.

## 7. Failure Analysis

Missed vulnerabilities and incorrect warnings will be examined to identify recurring patterns, such as missing authorization checks, incorrect assumptions about caller permissions, or mismatches between tool findings and benchmark labels.

These categories are provisional and will be refined only when supported by observed cases.

## 8. Reproducibility

The project will preserve benchmark versions, labeling decisions, analyzer outputs, tool versions, compiler settings, and evaluation scripts where permitted.

## 9. Current Status

The repository contains an initial controlled Solidity test contract and a preliminary labeling template. The complete benchmark, analyzer evaluation, and empirical results have not yet been established.

No detection rates, comparative rankings, or experimental conclusions should be reported until the corresponding work has been completed and verified.
