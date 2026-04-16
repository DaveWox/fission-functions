# Fission Functions

This repository contains example serverless functions designed to run on **Fission**, a Kubernetes‑native serverless platform.  
Functions are defined declaratively and deployed using GitOps-friendly workflows (for example with Argo CD).

---

## What is Fission?

**Fission** is an open‑source **serverless framework for Kubernetes**.

It allows you to:
- Deploy functions without managing servers
- Automatically scale functions based on demand
- Run functions inside Kubernetes using familiar tooling
- Support multiple runtimes (Node.js, Python, Go, etc.)
- Integrate cleanly with GitOps and CI/CD pipelines

Fission runs entirely inside your Kubernetes cluster, giving you:
- Full control over networking and security
- Portable workloads
- No provider lock‑in

---

## Repository Structure

This repository uses Kustomize to manage Fission resources in a declarative and GitOps‑friendly way.
Resources are split by concern into environments, functions and triggers.

### environments/
Defines Fission runtime environments (for example Node.js, Python)
Each is defined within it's own yaml file and then referenced by a function.


### functions/
Contains function source code and Fission function definitions.

* main.py
  * The function source code - entry point
* hello.zip
  * The ZIP file is the delivery mechanism for your source code, Fission expects a deployable artifact.
* package.yaml
  * Binds source code to a Fission environment
* function.yaml
  * Defines the Fission Function resource (timeouts, resources, env vars)
* kustomization.yaml
  * Tells Kustomzie there are resources to deploy and build within the directory

Each function lives in its own directory to keep ownership and changes clear.


### triggers/
Defines how functions are invoked.

* HTTP triggers
* Event triggers (if applicable)



### Root kustomization.yaml
The top‑level kustomization.yaml composes:

* Environments
* Functions
* Triggers

This allows tools like Argo CD to deploy the entire platform declaratively.
