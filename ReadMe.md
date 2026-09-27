# Enterprise Multi-Agent Data Intelligence & Decision Support Platform

> An agentic AI-powered enterprise analytics platform that enables users to interact with structured business data and unstructured enterprise knowledge using natural language.

---

## Overview

The **Enterprise Multi-Agent Data Intelligence & Decision Support Platform** is a production-oriented Generative AI application designed to help business users analyze enterprise data through natural-language queries.

Instead of requiring users to manually write SQL queries, navigate dashboards, or search through business documents, the platform uses a **multi-agent architecture** to understand the user's question, determine the required tools, retrieve relevant information, perform analytical operations, validate the results, and generate a grounded response.

The system combines:

- Generative AI
- Large Language Models (LLMs)
- Multi-Agent Systems
- LangGraph
- LangChain
- Retrieval-Augmented Generation (RAG)
- Text-to-SQL
- Model Context Protocol (MCP)
- Tool Calling
- Semantic Search
- Vector Databases
- AI-powered Analytics
- Automated Visualization
- Response Validation
- Self-Correction
- LLM Evaluation
- FastAPI
- Docker
- AWS Bedrock

---

## Problem Statement

Traditional enterprise analytics systems generally require users to:

1. Understand database structures
2. Write SQL queries
3. Navigate BI dashboards
4. Know business terminology
5. Search through multiple documents
6. Manually combine structured and unstructured information

This creates a gap between business questions and actionable insights.

For example, a business user may ask:

> **"Why did revenue decrease in Chennai during Q2?"**

Answering this question may require:

- Querying transactional data
- Comparing revenue across periods
- Identifying major contributing customers or products
- Retrieving the company's revenue definitions
- Reviewing business documentation
- Performing statistical analysis
- Creating visualizations
- Validating the final conclusion

The proposed platform automates this workflow using specialized AI agents.

---

# Project Objectives

The primary objectives of this project are:

- Enable natural-language interaction with enterprise data
- Convert natural-language questions into SQL queries
- Retrieve information from enterprise documents using RAG
- Combine structured and unstructured data
- Perform automated business analytics
- Generate context-aware visualizations
- Coordinate multiple specialized AI agents
- Validate AI-generated SQL and analytical conclusions
- Implement self-correction mechanisms
- Provide grounded and explainable responses
- Integrate enterprise tools through MCP
- Evaluate LLM and RAG performance
- Provide a production-oriented GenAI architecture
- Support deployment using Docker and AWS services

---

# Core Capabilities

## 1. Multi-Agent AI Architecture

The platform uses a **LangGraph-based multi-agent architecture**.

Specialized agents are responsible for individual tasks.

### Agents

| Agent | Responsibility |
|---|---|
| Supervisor Agent | Understands the request and coordinates the workflow |
| SQL Agent | Generates, validates, and executes SQL queries |
| RAG Agent | Retrieves relevant enterprise knowledge |
| Analytics Agent | Performs analytical calculations |
| Visualization Agent | Selects and generates suitable charts |
| Validation Agent | Validates results and detects unsupported conclusions |

### High-Level Workflow

```text
                         User
                           |
                           v
                  +----------------+
                  |   Supervisor   |
                  |     Agent      |
                  +-------+--------+
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    +-----------+   +-----------+   +-------------+
    | SQL Agent |   | RAG Agent |   |  Analytics  |
    |           |   |           |   |    Agent    |
    +-----+-----+   +-----+-----+   +------+------+
          |               |                |
          v               v                v
    PostgreSQL        Vector DB         Pandas
          |               |                |
          +---------------+----------------+
                          |
                          v
                 +------------------+
                 | Visualization    |
                 | Agent            |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Validation Agent |
                 +--------+---------+
                          |
                    +-----+-----+
                    |           |
                   PASS        FAIL
                    |           |
                    v           v
              Final Answer   Correction

              