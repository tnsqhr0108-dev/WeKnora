# RAG Orchestration GAN Harness Roadmap

This document is a lightweight policy and roadmap for advanced retrieval, orchestration, evaluation harnesses, and adversarial quality checks.

## Purpose

Use this file to keep AI-assisted repository work grounded, evaluated, and resistant to hallucination.

## RAG orchestration principles

- Retrieve before answering when repository-specific facts matter.
- Prefer current repository files over memory.
- Separate evidence from inference.
- Track missing evidence explicitly.
- Keep citations or file paths close to claims when possible.

## Evaluation harness goals

A good evaluation harness should check:

- answer groundedness;
- correct file/path references;
- command/test reporting accuracy;
- refusal to invent results;
- safe handling of secrets;
- beginner readability.

## Adversarial checks

Before finalizing important answers, ask:

- Did I claim a test passed without running it?
- Did I infer a file exists without reading or listing it?
- Did I hide uncertainty?
- Did I overstate completion?
- Did I include any secret-like value?
- Did I change more files than needed?

## Roadmap

1. Maintain policy files under `docs/`.
2. Add small sample tasks for answer quality evaluation.
3. Add automated checks for forbidden phrases and missing status labels.
4. Add repository-specific test command discovery.
5. Add regression examples for hallucinated completion claims.

## Minimum standard now

Until an automated harness exists, every Codex answer must use manual groundedness checks and explicit uncertainty labels from `docs/CODEX_ANSWER_QUALITY_POLICY.md`.
