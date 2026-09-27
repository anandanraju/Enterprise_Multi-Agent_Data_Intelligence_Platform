## Enterprise Multi-Agent Data Intelligence Platform

An agentic AI-powered enterprise analytics platform that enables users to interact with structured business data and unstructured enterprise knowledge using natural language.

The platform combines Multi-Agent Systems, LangGraph, RAG, Text-to-SQL, MCP, tool calling, analytical reasoning, visualization, validation, and LLM evaluation to transform natural-language business questions into grounded, explainable analytical insights.

### Project Overview

Traditional BI systems require users to understand dashboards, filters, SQL queries, and predefined reports.

This project provides a natural-language interface where users can ask questions such as:

"Why did revenue decrease in Chennai during Q2?"

The system automatically determines which capabilities are required, retrieves relevant data, performs analysis, validates the generated insights, and produces a grounded response with supporting evidence and visualizations.

### Objectives
* Enable natural-language interaction with enterprise data
* Automate SQL query generation and execution
* Retrieve business knowledge from enterprise documents
* Combine structured and unstructured data
* Perform automated business analytics
* Generate appropriate visualizations
* Validate AI-generated analytical conclusions
* Reduce unsupported or hallucinated responses
* Provide source-aware and explainable answers
* Demonstrate production-oriented Agentic AI architecture

### Key Capabilities
1. Multi-Agent AI Architecture

The system uses specialized agents coordinated through LangGraph.

* Agents
* Supervisor Agent
* SQL Agent
* RAG Agent
* Analytics Agent
* Visualization Agent
* Validation Agent

Each agent performs a specialized task instead of relying on a single general-purpose LLM workflow.

2. Natural Language to SQL


Users can ask questions such as:

-- Which region generated the highest revenue?